FROM python:3.13-alpine

WORKDIR /app

RUN pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp

COPY server.py .

EXPOSE 3000

CMD ["python", "server.py"]