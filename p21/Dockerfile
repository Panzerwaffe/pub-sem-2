FROM python:3.10-slim

WORKDIR /

RUN pip install flask
RUN pip install flask_sqlalchemy

COPY . .

ENTRYPOINT ["python"]

CMD ["wsgi.py"]