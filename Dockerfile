FROM python:3.11

COPY ./requirements.txt /opt

RUN pip install -r /opt/requirements.txt

COPY ./pyproject.toml /opt/pyproject.toml
COPY ./dash_otel /opt/dash_otel

RUN pip install /opt/

CMD ["python", "-m", "dash_otel"]