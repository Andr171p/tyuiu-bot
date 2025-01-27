from pydantic import BaseModel


class SendByPhoneNumberParams(BaseModel):
    phone_number: str
    text: str


class SendAllParams(BaseModel):
    text: str
