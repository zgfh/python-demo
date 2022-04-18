FROM python:3.7-alpine

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY ./app.py /app.py

EXPOSE 8080

CMD ["python", "/app.py"]