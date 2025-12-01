FROM python:3.11-slim

WORKDIR /app

COPY src/contador.py .

# el contenedor ejecuta el script
CMD ["python", "contador.py"]

