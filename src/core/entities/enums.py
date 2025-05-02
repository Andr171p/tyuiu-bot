from enum import Enum, auto


class SharingContactStatus(Enum):
    SUCCESS = auto()  # contact created and user registered
    ALREADY_SHARED = auto()  # contact already created and user registered
    NOT_REGISTERED = auto()  # contact created and user not registered
    ERROR = auto()  # error while create contact
