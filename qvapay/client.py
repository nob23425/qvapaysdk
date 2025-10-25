from dataclasses import dataclass

from httpx import Client

from .models.balance import QvaPayTransactionResponse
from .models.info import UserInfo

# from httpx._config import DEFAULT_TIMEOUT_CONFIG
# from httpx._types import TimeoutTypes
from .utils import validate_response


@dataclass
class QvaPayClient:
    bearer_token: str
    # timeout : TimeoutTypes = field(default= DEFAULT_TIMEOUT_CONFIG)

    def __post_init__(self):
        self.auth_params = self.bearer_token
        self.headers = {
            "Authorization": f"Bearer {self.auth_params}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self.base_url = "https://api.qvapay.com"

        self.sync_client = Client(base_url=self.base_url, headers=self.headers, timeout=5)

    def __enter__(self):
        return self

    def __exit__(self, exc_t, exc_v, exc_tb) -> None:
        self.close()

    def close(self) -> None:
        self.sync_client.close()

    def get_info(self):
        response = self.sync_client.get("user")
        validate_response(response)
        return UserInfo.from_json(response.json())

    def topup_balance(self, pay_method: str, amount: int):
        params = {"pay_method": "BTCLN", "amount": 2}
        response = self.sync_client.post("topup", params=params)
        validate_response(response)
        return QvaPayTransactionResponse.from_json(response.json())
