from dataclasses import dataclass, field
from os import environ
from dotenv import load_dotenv
from .errors import QvaPayError

# carga el .env desde la carpeta actual
load_dotenv()


@dataclass
class QvaPayAuth:
    qvapay_bearer_token = field(default=environ["QVAPAY_BEARER_TOKEN"])

    def __post_init__(self):
        if not self.qvapay_bearer_token:
            raise QvaPayError(0, "token bearer no found")
