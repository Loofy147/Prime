# app/tests/test_main.py

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.backend.main import app

client = TestClient(app)

def test_query_unauthorized():
    response = client.post("/v1/query", json={"user_id": "test", "prompt": "hello"})
    assert response.status_code == 401

@patch('app.backend.main.get_db_connection')
@patch('app.backend.services.model_adapter.redis_client')
def test_query_authorized(mock_redis_client, mock_get_db_connection):
    # Mock Redis
    mock_redis_client.get.return_value = None
    mock_redis_client.set.return_value = None

    # Mock DB connection
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_get_db_connection.return_value.__enter__.return_value = mock_conn
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

    response = client.post(
        "/v1/query",
        json={"user_id": "test", "prompt": "hello"},
        headers={"Authorization": "Bearer fake-super-secret-token"}
    )
    assert response.status_code == 200
    assert "answer" in response.json()
    assert "provenance" in response.json()
