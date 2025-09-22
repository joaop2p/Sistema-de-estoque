import os
import sys
import unittest
from unittest.mock import patch, Mock
from datetime import datetime

# Garantir que o diretório raiz do projeto esteja no sys.path para permitir imports "lib.src..."
CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from lib.src.app.controllers.client_api_controller import ClientApiController
from lib.src.config.api_config import ApiConfig
from lib.src.app.models.client import Client
from lib.utils.exceptions.api_exceptions import ApiException


class TestClientApiController(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.controller = ClientApiController()

    @patch("lib.src.app.controllers.api_controller.get")
    async def test_find_all_success(self, mock_get):
        # Arrange
        fake_clients = [
            {
                "name": "Alice",
                "email": "alice@example.com",
                "phone": "+5511999999999",
                "status": "Active",
                "created_at": datetime(2025, 1, 1, 12, 0, 0),
                "updated_at": datetime(2025, 1, 2, 12, 0, 0),
                "photo": None,
                "id": 1,
                "conection_status": "online",
            },
            {
                "name": "Bob",
                "email": "bob@example.com",
                "phone": "+5511888888888",
                "status": "Inactive",
                "created_at": datetime(2025, 2, 1, 9, 0, 0),
                "updated_at": datetime(2025, 2, 3, 10, 30, 0),
                "photo": None,
                "id": 2,
                "conection_status": "offline",
            },
        ]

        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.json = Mock(return_value=fake_clients)
        mock_get.return_value = mock_response

        # Act
        result = await ClientApiController.find_all()

        # Assert
        mock_get.assert_called_once_with(
            ApiConfig.URL + "/clients",
            headers=ApiConfig.HEADERS,
        )
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        self.assertTrue(all(isinstance(c, Client) for c in result))
        self.assertEqual(result[0]._name, "Alice")
        self.assertEqual(result[1]._email, "bob@example.com")

    @patch("lib.src.app.controllers.api_controller.get")
    async def test_find_by_id_success(self, mock_get):
        # Arrange
        client_data = {
            "name": "Carol",
            "email": "carol@example.com",
            "phone": "+5511777777777",
            "status": "Pending",
            "created_at": datetime(2025, 3, 1, 8, 0, 0),
            "updated_at": datetime(2025, 3, 1, 8, 30, 0),
            "photo": None,
            "id": 3,
            "conection_status": "away",
        }

        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.json = Mock(return_value=client_data)
        mock_get.return_value = mock_response

        # Act
        result = await self.controller.find_by_id("3")

        # Assert
        mock_get.assert_called_once_with(
            ApiConfig.URL + f"/clients/3",
            headers=ApiConfig.HEADERS,
        )
        self.assertIsInstance(result, Client)
        self.assertEqual(result._name, "Carol")
        self.assertEqual(result._id, 3)

    @patch("lib.src.app.controllers.api_controller.get")
    async def test_find_all_error_raises_api_exception(self, mock_get):
        # Arrange
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = Exception("HTTP error")
        mock_get.return_value = mock_response

        # Act / Assert
        with self.assertRaises(ApiException) as ctx:
            await ClientApiController.find_all()

        self.assertEqual(getattr(ctx.exception, "status_code", None), 500)


if __name__ == "__main__":
    unittest.main()
