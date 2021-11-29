FROM python:3.8

WORKDIR /pokedex_info

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5003

ENTRYPOINT ['python', 'service_four.py']