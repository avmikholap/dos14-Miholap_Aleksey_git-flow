FROM python:3.11-buster

RUN pip install poetry && useradd -d /home/authz -U -m -u 1111 authz

USER authz

WORKDIR /home/authz/git

COPY --chown=authz:authz . .

RUN poetry install

ENTRYPOINT ["poetry", "run"]

CMD ["python", "main.py"]