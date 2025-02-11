from typing import Optional
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import tempfile
import os
from telegram_service import TelegramConfig, TelegramService

app = FastAPI()

@app.post("/send_message")
async def send_message(
    username: str = Form(...),
    message: str = Form(...),
    photo: UploadFile = File(None)  
):
    tmp_file_path = None
    try:
        if photo:
            file_bytes = await photo.read()
            suffix = os.path.splitext(photo.filename)[1] if photo.filename else ""
            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
                tmp_file.write(file_bytes)
                tmp_file_path = tmp_file.name

        tg_service = TelegramService(config=TelegramConfig())
        await tg_service.send_file_or_msg(
            username=username,
            message=message,
            photo_path=tmp_file_path or None
        )
        return {"status": "success", "detail": "Сообщение отправлено"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка при отправке: {e}")
    finally:
        if tmp_file_path:
            try:
                os.remove(tmp_file_path)
            except Exception:
                pass
