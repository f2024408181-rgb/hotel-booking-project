from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional
from models import BookingModel

from database import booking_collection

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/book", response_class=HTMLResponse)
async def book_hotel(
    request: Request,
    full_name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    check_in: str = Form(...),
    check_out: str = Form(...),
    room_type: str = Form(...),
    guests: Optional[int] = Form(None),
    requests: Optional[str] = Form(None)
):
    booking_data = {
        "full_name": full_name,
        "email": email,
        "phone": phone,
        "check_in": check_in,
        "check_out": check_out,
        "room_type": room_type,
        "guests": guests,
        "requests": requests
    }

    booking_collection.insert_one(booking_data)

    return templates.TemplateResponse(
        request=request,
        name="success.html",
        context={
            "full_name": full_name,
            "room_type": room_type,
            "check_in": check_in,
            "check_out": check_out,
            "guests": guests
        }
    )
