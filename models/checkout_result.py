from enum import Enum

from pydantic import BaseModel


class LoginStatus(str, Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class CheckoutStatus(str, Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class CheckoutResult(BaseModel):
    login_status: LoginStatus
    cart_status: str
    checkout_status: CheckoutStatus
    total_update_status: str
    confirmation_message: str
