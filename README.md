# ImageToText
Use images to extract text from it usinf FastAPI

# Image to Text Microservice

A FastAPI microservice for extracting  text from images.It is deployed at [https://imagetotext-042d.onrender.com/](https://imagetotext-042d.onrender.com/).

## Endpoints
### `GET:Home View`
The normal home page with some changes and response as an HTML template .
Endpoint:`https://imagetotext-042d.onrender.com/`

### `POST:Image Prediction View`
This endpoint takes a photo as input and provides the extracted text as results.
Endpoint: `https://imagetotext-042d.onrender.com/`

### `POST:Img-Echo View`
This endpoint is used for validation testing using pytest. It echoes back the uploaded image for validation purposes.
Endpoint: `https://imagetotext-042d.onrender.com/img-echo`

## Swagger UI Documentation

The API endpoints are documented using Swagger UI. You can explore and test the endpoints by visiting [https://imagetotext-042d.onrender.com/docs](https://imagetotext-042d.onrender.com/docs).

## Getting Started

To run this microservice locally for development or testing, you can follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/raaz252/ImageToText.git
   cd ImageToText
   ```
# Pytest for FastAPI Image-to-Text Microservice

This pytest suite is designed to test a FastAPI microservice that converts images to text. The microservice is expected to handle file uploads, perform OCR (Optical Character Recognition), and provide echo functionality for image validation.

## Test Setup

To run these tests, you need to have Python and pytest installed. You can install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```
**The tests are designed to work with the provided FastAPI application located in app.main. The BASE_DIR variable is expected to point to the base directory of your project, and the TestClient class from fastapi.testclient is used for simulating HTTP requests.**

### Test Descriptions
```py
test_invalid_file_upload_error
```
This test checks for error handling when an invalid file is uploaded.
It sends a POST request to the root endpoint ("/") without a valid file.
It expects a response status code of 422 and "application/json" in the response headers.

```py
test_prediction_upload
```
This test uploads images from the "images" folder and checks the microservice's prediction functionality.
It iterates through the image files in the "images" folder and attempts to open each image.
For valid images, it sends a POST request to the root endpoint ("/") with the image file.
It checks if the response status code is 200 and the JSON response contains two keys.
For invalid images, it sends a POST request and checks for a 400 status code.
```py
test_echo_upload
```
This test validates the image echo functionality.
It uploads images from the "images" folder to the "/img-echo" endpoint.
It verifies that the response status code is 200.
It compares the uploaded image with the echoed image to ensure they are identical.