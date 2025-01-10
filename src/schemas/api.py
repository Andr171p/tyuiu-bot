from pydantic import BaseModel


class ResponseData(BaseModel):
    status: str
    answer: str


class ResponseSchema(BaseModel):
    data: ResponseData
