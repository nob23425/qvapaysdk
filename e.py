import os
from pprint import pp

from dotenv import load_dotenv

from qvapay.client import QvaPayClient

# carga el .env desde la carpeta actual
load_dotenv()

token = os.environ.get("QVAPAY_BEARER_TOKEN")


with QvaPayClient(token) as client:
    # ser_info = client.get_info()
    user = client.get_info()
    pp(user.balance)
