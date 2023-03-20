
FROM python:3.8
COPY my_app.py /
COPY model.data-00000-of-00001 /
COPY model.index /
ADD requirements.txt /   
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt   
