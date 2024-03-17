FROM python:3.12

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt --no-cache-dir

COPY .env .

CMD ["python", "main.py"]
