from flask import (
    Blueprint,
    redirect,
    request,
    flash,
    url_for,
    render_template
)

from flask_login import login_required, current_user
from sqlalchemy import text

from fantasyapp.blueprints.admin.models import Dashboard
from fantasyapp.blueprints.user.decorators import role_required
from fantasyapp.blueprints.user.models import User
from fantasyapp.blueprints.game.models.driver import Driver
from fantasyapp.blueprints.game.models.game import Game
from config import settings
from fantasyapp.blueprints.admin.forms import (
    SearchForm,
    BulkDeleteForm,
    UserForm,
    UpdateGameForm
)

admin = Blueprint('admin', __name__,
                  template_folder='templates', url_prefix='/admin')


@admin.before_request
@login_required
@role_required('admin')
def before_request():
    """ Protect all of the admin endpoints. """
    pass


# Dashboard -------------------------------------------------------------------
@admin.route('')
def dashboard():
    group_and_count_users = Dashboard.group_and_count_users()
    group_and_count_races = Dashboard.group_and_count_races()

    return render_template('admin/page/dashboard.html',
                           group_and_count_users=group_and_count_users,
                           group_and_count_races=group_and_count_races)


# Users -----------------------------------------------------------------------
@admin.route('/users', defaults={'page': 1})
@admin.route('/users/page/<int:page>')
def users(page):
    search_form = SearchForm()
    bulk_form = BulkDeleteForm()

    sort_by = User.sort_by(request.args.get('sort', 'created_on'),
                           request.args.get('direction', 'desc'))
    order_values = '{0} {1}'.format(sort_by[0], sort_by[1])

    paginated_users = User.query \
        .filter(User.search(request.args.get('q', ''))) \
        .order_by(User.role.asc(), text(order_values)) \
        .paginate(page, 50, True)

    return render_template('admin/user/index.html',
                           form=search_form, bulk_form=bulk_form,
                           users=paginated_users)


@admin.route('/users/edit/<int:id>', methods=['GET', 'POST'])
def users_edit(id):
    user = User.query.get(id)
    form = UserForm(obj=user)

    if form.validate_on_submit():
        if User.is_last_admin(user,
                              request.form.get('role'),
                              request.form.get('active')):
            flash('You are the last admin, you cannot do that.', 'danger')
            return redirect(url_for('admin.users'))

        form.populate_obj(user)

        if not user.username:
            user.username = None

        user.save()

        flash('User has been saved successfully.', 'success')
        return redirect(url_for('admin.users'))

    return render_template('admin/user/edit.html', form=form, user=user)


@admin.route('/users/bulk_delete', methods=['POST'])
def users_bulk_delete():
    form = BulkDeleteForm()

    if form.validate_on_submit():
        ids = User.get_bulk_action_ids(request.form.get('scope'),
                                       request.form.getlist('bulk_ids'),
                                       omit_ids=[current_user.id],
                                       query=request.args.get('q', ''))

        delete_count = User.bulk_delete(ids)

        flash('{0} user(s) were scheduled to be deleted.'.format(delete_count),
              'success')
    else:
        flash('No users were deleted, something went wrong.', 'danger')

    return redirect(url_for('admin.users'))


# Games ---------------------------------------------------------------------
@admin.route('/games/edit', methods=['GET', 'POST'])
def games_edit():
    form = UpdateGameForm()
    form.driver.choices = [(row.id, row.name) for row in Driver.query.all()]
    form.race.choices = [(key, value['name']) for key, value in settings.RACES.items()]

    if form.validate_on_submit():
        driver = int(request.form.get('driver'))
        race = request.form.get('race')
        laps_led = int(request.form.get('laps_led'))
        fastest_laps = int(request.form.get('fastest_laps'))
        differential = int(request.form.get('differential'))
        finish = int(request.form.get('finish'))
        points = Dashboard.calculate_points(laps_led, fastest_laps, differential, finish)

        # Set game instance params
        params = {
            'laps_led': laps_led,
            'fastest_laps': fastest_laps,
            'differential': differential,
            'finish': finish,
            'total_points': points
        }

        # Save and commit the selected driver to game object
        update_count = Game.bulk_update(driver, race, params)

        if update_count:
            flash('{0} games(s) were scheduled to be updated.'.format(update_count),
                  'success')
            return redirect(url_for('admin.games_edit'))
        else:
            flash('No games where updated', 'warning')
            return redirect(url_for('admin.games_edit'))

    return render_template('admin/game/update.html', form=form)
