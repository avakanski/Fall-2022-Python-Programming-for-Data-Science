FROM jupyter/scipy-notebook

RUN mkdir model
ENV MODEL_DIR=/home/jovyan/model
ENV MODEL_FILE=clf.joblib

COPY train.py ./train.py
COPY inference.py ./inference.py

RUN python train.py

CMD [ "python", "./inference.py"]