from typing import Optional, List, Self

from pydantic import BaseModel, model_validator


class Content(BaseModel):
    text: str
    image_url: Optional[str] = None
    image_base64: Optional[str] = None

    @model_validator(mode="after")
    def check_images(self) -> Self:
        if self.image_url and self.image_base64:
            raise ValueError("Only one image must be set")
        return self


class NotificationOne(BaseModel):
    phone_number: Optional[str] = None
    user_id: Optional[str] = None
    content: Content

    @model_validator(mode="after")
    def check_contacts(self) -> Self:
        if not self.phone_number and not self.user_id:
            raise ValueError(f"Either phone_number or user_id must be provided")
        elif self.phone_number and self.user_id:
            raise ValueError(f"Only one value must be set")
        return self


class NotificationAll(BaseModel):
    content: Content


class NotificationBatch(BaseModel):
    phone_numbers: Optional[List[str]] = None
    user_ids: Optional[List[str]] = None
    content: Content

    @model_validator(mode="after")
    def check_contacts(self) -> Self:
        if not self.phone_numbers and not self.user_ids:
            raise ValueError(f"Either phone_number or user_id must be provided")
        elif self.phone_numbers and self.user_ids:
            raise ValueError(f"Only one value must be set")
        return self
