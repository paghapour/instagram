FROM python:alpine3.15
RUN pip install pymongo
CMD [ "python" , "main.py" ]
COPY main.py /main.py