from pydantic import BaseModel


class NotificationSchema(BaseModel):
    text: str


class NotifyByPhoneNumberSchema(NotificationSchema):
    phone_number: str
    
    
class NotifyAllSchema(NotificationSchema):
    pass