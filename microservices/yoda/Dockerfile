FROM python

WORKDIR /usr/src/app

# install requirements
# this way when you build you won't need to install again
# and since COPY is cached we don't need to wait
COPY app/src/requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

COPY app /usr/src/app
RUN export GOOGLE_APPLICATION_CREDENTIALS="/usr/src/app/conf/project-secret.json"

# App port number is configured through the gunicorn config file
CMD ["gunicorn", "--config", "./conf/gunicorn_config.py", "src:app"]
