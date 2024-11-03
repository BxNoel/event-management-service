FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN ls /app  # Add this to verify contents
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
