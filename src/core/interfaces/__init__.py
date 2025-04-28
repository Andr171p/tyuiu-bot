__all__ = (
    "Sender",
    "UserRegistration",
    "ChatAssistant",
    "UserRepository",
    "ContactRepository"
)

from src.core.interfaces.senders import Sender
from src.core.interfaces.rest import ChatAssistant, UserRegistration
from src.core.interfaces.repositories import UserRepository, ContactRepository
