FROM python:3

ADD app.py /

RUN pip install pymongo

CMD ["python", "./app.py"]
