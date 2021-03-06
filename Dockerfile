FROM python:2.7-slim

RUN apt-get update && apt-get install -qq -y \
    build-essential libpq-dev --no-install-recommends

ENV INSTALL_PATH /fantasyapp
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

VOLUME ["/fantasyapp/fantasyapp/static"]

RUN pip install --editable .

CMD gunicorn -c "python:config.gunicorn" "fantasyapp.app:create_app()"
