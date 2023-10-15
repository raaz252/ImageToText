import pathlib
import io
import uuid
from fastapi import (
    FastAPI,
    Request,
    HTTPException,
    Depends,
    File,
    UploadFile)
from fastapi.responses import HTMLResponse,FileResponse
from fastapi.templating import Jinja2Templates
from devenv.debug import Settings,getSettings
from PIL import Image
import pytesseract

BASE_DIR=pathlib.Path(__file__).parent

#print(BASE_DIR / "templates"
UploadDir= BASE_DIR / "uploads"
print(UploadDir)
app=FastAPI()
templates=Jinja2Templates(directory=str(BASE_DIR / "templates"))
print(templates)

@app.get("/",response_class=HTMLResponse)
def home_view(request:Request,settings:Settings = Depends(getSettings)):
    return templates.TemplateResponse("home.html",{"request":request,"abc":123 })

@app.post("/")
async def img_prediction_view(file:UploadFile = File(...),settings:Settings = Depends(getSettings)):
    bytes_str = io.BytesIO(await file.read())
    """
    To upload files in the destination we can do this
    dest = UploadDir/ file.filename
    but it will create problem as user continuously upload same file .
    To solve this problem we can do import uuid and pathlib
    """
    try:
        img = Image.open(bytes_str)
    except:
        raise HTTPException(detail="Invalid Image",status_code=400)
    preds=pytesseract.image_to_string(img)
    predictions=[x for x in preds.split('\n')]
    return {"result":predictions,"original":preds}


@app.post("/img-echo",response_class=FileResponse)
async def img_echo_view(file:UploadFile = File(...),settings:Settings = Depends(getSettings)):
    if not settings.echo_active:
        raise HTTPException(detail="Invalid Endpoint",status_code=400)
    UploadDir.mkdir(exist_ok=True)
    bytes_str = io.BytesIO(await file.read())
    """
    To upload files in the destination we can do this
    dest = UploadDir/ file.filename
    but it will create problem as user continuously upload same file .
    To solve this problem we can do import uuid and pathlib
    """
    try:
        img = Image.open(bytes_str)
    except:
        raise HTTPException(detail="Invalid Image",status_code=400)
    fname = pathlib.Path(file.filename)
    fext = fname.suffix
    dest= UploadDir/f"{uuid.uuid1()}{fext}"
    img.save(dest)
    return dest
