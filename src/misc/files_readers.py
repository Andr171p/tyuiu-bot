import aiofiles
from pathlib import Path


async def read_txt(file_path: Path | str) -> str:
    async with aiofiles.open(
        file=file_path,
        mode="r",
        encoding="utf-8"
    ) as file:
        return await file.read()
