from dataclasses import dataclass
from typing import Optional
from uuid import UUID


@dataclass
class QvaPayTransactionData:
    wallet: str
    value: float
    coin: str
    price: float
    transaction_id: int
    transaction_uuid: UUID
    transaction_url: str
    redirect_url: Optional[str] = None

    def __post_init__(self):
        self.value = float(self.value)
        self.price = float(self.price)
        self.transaction_id = int(self.transaction_id)
        self.transaction_uuid = UUID(str(self.transaction_uuid))


@dataclass
class QvaPayTransactionResponse:
    result: str
    data: QvaPayTransactionData

    @staticmethod
    def from_json(json_dict: dict) -> "QvaPayTransactionResponse":
        """
        Crea una instancia de QvaPayTransactionResponse desde un JSON.
        """
        data = QvaPayTransactionData(**json_dict["data"])
        return QvaPayTransactionResponse(result=json_dict["result"], data=data)
