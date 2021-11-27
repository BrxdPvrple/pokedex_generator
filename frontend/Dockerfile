FROM python:3.8

WORKDIR /frontend

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ['python', 'service_one.py']