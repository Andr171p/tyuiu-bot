from typing import Literal

from pydantic import BaseModel


class DeliveredResponse(BaseModel):
    info: Literal[
        "notification delivered",
        "notification is not delivered"
    ]


class SuccessfullyDeliveredResponse(DeliveredResponse):
    info = "notification delivered"


class UnsuccessfullyDeliveredResponse(DeliveredResponse):
    info = "notification is not delivered"


class DeliveredResponsePresenter:
    def __init__(self, is_delivered: bool) -> None:
        self._is_delivered = is_delivered

    def present(self) -> DeliveredResponse:
        if self._is_delivered:
            return SuccessfullyDeliveredResponse()
        return UnsuccessfullyDeliveredResponse()
