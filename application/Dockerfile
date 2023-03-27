FROM python:3.8-alpine

COPY requirements.txt /app/requirements.txt
COPY app/ /app
WORKDIR /app
RUN pip install --no-cache-dir -r /app/requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
