FROM python:3.9-slim
RUN pip install prometheus_client psutil
COPY exporter.py .
EXPOSE 8000
CMD ["python", "exporter.py", "--host", "0.0.0.0"]