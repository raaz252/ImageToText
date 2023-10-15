# Use an official Python runtime as a parent image
FROM python:3.11-slim

COPY ./app /app
COPY ./devenv ./devenv
COPY ./requirements.txt /requirements.txt

RUN apt-get update && \
    apt-get install -y \
        build-essential \
        python3-dev \
        python3-setuptools \
        tesseract-ocr \
        make \
        gcc \
    && python3 -m pip install -r requirements.txt \
    && apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Expose the port that the FastAPI application will run on (change to the port used in your FastAPI app)
EXPOSE 8000

# Command to run your FastAPI application using Uvicorn
CMD ["gunicorn","-k","uvicorn.workers.UvicornWorker","app.main:app","--bind", "0.0.0.0:8000"]
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
