from dataclasses import dataclass
from typing import Any, List
from uuid import UUID

# from dateutil.parser import parse


@dataclass
class UserInfo:
    """
    QvaPay user info
    """

    id: UUID
    username: str
    name: str
    lastname: str
    email: str
    bio: str
    balance: float
    satoshis: int
    phone: str
    phone_verified: bool
    kyc: bool
    golden_check: bool
    golden_expire: str
    p2p_enabled: bool
    cover: str
    image: str
    average_rating: float
    latest_transactions: List[Any]

    def __post_init__(self):
        self.id = UUID(str(self.id))
        self.username = str(self.username)
        self.name = str(self.name)
        self.lastname = str(self.lastname)
        self.email = str(self.email)
        self.bio = str(self.bio)
        self.balance = float(self.balance)
        self.satoshis = int(self.satoshis)
        self.phone = str(self.phone)
        self.phone_verified = bool(self.phone_verified)
        self.kyc = bool(self.kyc)
        self.golden_check = bool(self.golden_check)
        self.golden_expire = str(self.golden_expire)
        self.p2p_enabled = bool(self.p2p_enabled)
        self.cover = str(self.cover)
        self.image = str(self.image)
        self.average_rating = float(self.average_rating)
        self.latest_transactions = list(self.latest_transactions or [])

    @staticmethod
    def from_json(json: Any) -> "UserInfo":
        """
        Create a UserInfo instance from a JSON dict.
        """

        json["id"] = json["uuid"]
        del json["uuid"]
        return UserInfo(**json)
