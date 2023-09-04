from dotenv import load_dotenv
from os import getenv


load_dotenv()

RABBITMQ_DEFAULT_USER = getenv("RABBITMQ_DEFAULT_USER") or "user"
RABBITMQ_DEFAULT_PASS = getenv("RABBITMQ_DEFAULT_PASS") or "password"
RABBITMQ_DEFAULT_PORT = int(getenv("RABBITMQ_DEFAULT_PORT", "5672")) or 5672
RABBITMQ_DEFAULT_HOST = getenv("RABBITMQ_DEFAULT_HOST") or "localhost"
PECHINCHOU_API_HOME = getenv("PECHINCHOU_API_HOME") or "fail"
MAGALU_QUEUE = getenv("MAGALU_QUEUE") or "magalu-item"
AMAZON_QUEUE = getenv("AMAZON_QUEUE") or "amazon-colly"