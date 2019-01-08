

from os import environ

HTTP_PROVIDER_URL = environ.get("HTTP_PROVIDER_URL")
WS_PROVIDER_URL = environ.get("WS_PROVIDER_URL")

ALLOWED_ORIGIN_SUFFIXES = environ.get("ALLOWED_ORIGIN_SUFFIXES",
                                      "localhost").split(",")

ED_CONTRACT_ADDR = '0x51a2b1a38ec83b56009d5e28e6222dbb56c23c22'
with open('etherdelta.abi.json') as f:
    import json
    ED_CONTRACT_ABI = json.load(f)
ED_WS_SERVERS = [
    "wss://api.ndex.market/socket.io/?EIO=3&transport=websocket",
]

POSTGRES_HOST = "postgres"
POSTGRES_DB = environ.get("POSTGRES_DB")
POSTGRES_USER = environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = environ.get("POSTGRES_PASSWORD")

FRONTEND_CONFIG_FILE = "https://ndex.market/config/main.json"
STOPPED_TOKENS = (
    "0x86fa049857e0209aa7d9e616f7eb3b3b78ecfdb0",  # EOS: https://block.one/news/community-reminder-eos-token-registration-and-freeze/
    "0x7e9e431a0b8c4d532c745b1043c7fa29a48d4fba",  # eosDAC: https://twitter.com/eosdac/status/1002657571197673475?lang=en
    "0xa5fd1a791c4dfcaacc963d4f73c6ae5824149ea7",  # JNT: https://t.me/jibrel_network/129713
)
