FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python scrapper/main.py

EXPOSE 5000
CMD ["flask", "--app", "app", "run", "-h", "0.0.0.0"]
