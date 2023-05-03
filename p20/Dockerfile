FROM python:3.10-slim

WORKDIR /app

RUN pip install flask

COPY . .

ENTRYPOINT ["python", "app.py"]

# just for example
CMD ["9"]