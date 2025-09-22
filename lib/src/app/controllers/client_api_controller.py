from lib.src.app.models.client import Client
from requests import get
import traceback
from lib.src.config.api_config import ApiConfig
from lib.utils.exceptions.api_exceptions import ApiException

class ClientApiController:
    @staticmethod
    async def find_all() -> list[Client] | None:
        try:
            url = ApiConfig.URL + "/clients"
            print(url)
            response = get(url, headers=ApiConfig.HEADERS)
            if response.status_code == 200:
                # print("Response JSON:", response.json())
                return [Client.from_dict(data) for data in response.json()]
            else:
                raise ApiException("Failed to fetch clients", status_code=response.status_code)
        except Exception as e:
            print(f"Error fetching clients: {e}")
            traceback.print_exc()
            return None

    async def find_by_id(self, id: str):
        try:
            response = get(ApiConfig.URL + f"/clients/{id}", headers=ApiConfig.HEADERS)
            response.raise_for_status()
            return Client(**response.json())
        except Exception as e:
            print(f"Error fetching client by ID {id}: {e}")
            raise ApiException("Failed to fetch client", status_code=500)

    async def create(self, data: dict):
        pass

    async def update(self, id: str, data: dict):
        pass

    async def delete(self, id: str):
        pass