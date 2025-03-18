import aiofiles
from pathlib import Path
from typing import Union


async def write_file(file_path: Union[Path, str], data: bytes) -> None:
    async with aiofiles.open(
        file=file_path,
        mode="wb"
    ) as file:
        await file.write(data)
