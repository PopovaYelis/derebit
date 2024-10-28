FROM python:3.9-slim

WORKDIR /project

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD (uvicorn api:app --host 0.0.0.0 --port 5050 &) && python main.py
