# Use an official Python runtime as a parent image
FROM python:3.11.1

# Set environment variables to prevent buffering and auto flush
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /imagetotext

# Copy the requirements file into the container at /app
COPY requirements.txt /imagetotext//

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the entire project directory into the container at /app
COPY . /imagetotext/

# Expose the port that the FastAPI application will run on (change to the port used in your FastAPI app)
EXPOSE 8000

# Command to run your FastAPI application using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
