class ApiConfig:
    URL: str = "http://127.0.0.1:8000/sistema_estoque_api/v1"
    HEADERS: dict[str, str] = {
        "Content-Type": "application/json",
    }