FROM python:3.8

WORKDIR /region_generator

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5001

ENTRYPOINT ['python', 'service_two.py']