from client import RequestsClient
from config import settings


ping_url = settings.api_url + "ping"

client = RequestsClient(
    url=ping_url, headers={"x-cg-api-key": settings.api_token}, params={}
)
response = client.get()
print(response)
