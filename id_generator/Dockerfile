FROM python:3.8

WORKDIR /id_generator

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5002

ENTRYPOINT ['python', 'service_three.py']