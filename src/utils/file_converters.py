from io import BytesIO

from fastapi import UploadFile


async def get_upload_file_bytes(file: UploadFile) -> BytesIO:
    file_bytes = await file.read()
    return BytesIO(file_bytes)
