FROM python:3.7.5-slim

COPY requirements.txt ./requirements.txt
COPY mnist_train.py ./mnist_train.py
COPY mnist_inference.py ./mnist_inference.py

RUN pip install -r requirements.txt
RUN python mnist_train.py

CMD [ "python", "./mnist_inference.py" ]