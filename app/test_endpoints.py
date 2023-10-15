from fastapi.testclient import TestClient
from fastapi import HTTPException
from app.main import app,BASE_DIR
import pytest
import shutil
from PIL import Image,ImageChops
import io

client = TestClient(app)


def test_invalid_file_upload_error():
    response = client.post("/") # requests.post("") # python requests
    assert response.status_code == 422
    assert  "application/json" in response.headers['content-type']

def test_prediction_upload():
    uploads_folder = BASE_DIR / "uploads"
    img_path= BASE_DIR / "images"
    for path in img_path.glob('*'):
        try:
            img=Image.open(path)
        except:
            img=None
        response = client.post("/",files={"file":open(path,'rb')})
        print(response.headers['content-type'])
        if img is  None:
            assert response.status_code == 400
        else:
            assert response.status_code == 200
            data=response.json()
            assert len(data.keys())==2

"""
@pytest.fixture
def cleanup_uploads():
    uploads_folder = BASE_DIR / "uploads"
    yield uploads_folder  # Provide the uploads folder path to the test
    # After the test is complete, delete the contents of the uploads folder
    shutil.rmtree(uploads_folder)
"""

def test_echo_upload():
    uploads_folder = BASE_DIR / "uploads"
    img_path= BASE_DIR / "images"
    for path in img_path.glob('*'):
        try:
            img=Image.open(path)
        except:
            img=None
        response = client.post("/img-echo",files={"file":open(path,'rb')})
        print(response.headers)
        if img is  None:
            assert response.status_code == 400
        else:
            assert response.status_code == 200
            r_stream=io.BytesIO(response.content)
            echo_img=Image.open(r_stream)
            difference = ImageChops.difference(img,echo_img).getbbox()
            assert difference is None
    shutil.rmtree(uploads_folder)


