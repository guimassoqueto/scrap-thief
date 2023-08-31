from dotenv import load_dotenv
from os import getenv


load_dotenv()

RABBITMQ_DEFAULT_USER = getenv("RABBITMQ_DEFAULT_USER") or "user"
RABBITMQ_DEFAULT_PASS = getenv("RABBITMQ_DEFAULT_PASS") or "password"
RABBITMQ_DEFAULT_PORT = int(getenv("RABBITMQ_DEFAULT_PORT", "5672")) or 5672
RABBITMQ_DEFAULT_HOST = getenv("RABBITMQ_DEFAULT_HOST") or "localhost"
RABBITMQ_SEND_QUEUE = getenv("RABBITMQ_SEND_QUEUE") or "amazon-colly"
PECHINCHOU_API_HOME = getenv("PECHINCHOU_API_HOME") or "fail"