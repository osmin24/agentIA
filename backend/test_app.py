import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

from app import app

client = TestClient(app)

@patch('app.rag_system.query')
def test_query_validation_too_long(mock_query):
    long_query = "a" * 1001
    response = client.post("/api/query", json={"query": long_query})
    assert response.status_code == 400
    assert "demasiado larga" in response.json()["detail"].lower()

@patch('app.rag_system.query')
@patch('app.rag_system.session_manager.create_session')
def test_query_validation_valid(mock_create_session, mock_query):
    mock_create_session.return_value = "session_1"
    mock_query.return_value = ("Test answer", ["Source 1"])
    
    valid_query = "hola"
    response = client.post("/api/query", json={"query": valid_query})
    
    assert response.status_code == 200
    data = response.json()
    assert data["answer"] == "Test answer"

@patch('app.rag_system.query')
@patch('app.rag_system.session_manager.create_session')
def test_logging_is_used(mock_create_session, mock_query, caplog):
    import logging
    caplog.set_level(logging.INFO)
    
    mock_create_session.return_value = "session_1"
    mock_query.return_value = ("Test answer", ["Source 1"])
    
    response = client.post("/api/query", json={"query": "test query"})
    
    assert "Received query" in caplog.text
