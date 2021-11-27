FROM python: 3.8

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5002

ENTRYPOINT ['python', 'service_three.py']