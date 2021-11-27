FROM python:3.8

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5003

ENTRYPOINT ['python', 'service_four.py']