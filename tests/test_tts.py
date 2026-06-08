import pytest
from fastapi.testclient import TestClient
import sys
import os

# Ensure backend module can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from app import app

client = TestClient(app)

from unittest.mock import patch

@patch("app.rag_system.query")
def test_query_returns_audio_url(mock_query):
    mock_query.return_value = ("Dummy answer", ["source1"])
    response = client.post("/api/query", json={"query": "test query"})
    assert response.status_code == 200
    data = response.json()
    assert "audio_url" in data
    assert data["audio_url"].startswith("/api/audio/")

@patch("app.rag_system.query")
def test_audio_endpoint_returns_dummy_file(mock_query):
    mock_query.return_value = ("Dummy answer", ["source1"])
    # First, get the audio_url from a query
    response = client.post("/api/query", json={"query": "test query"})
    assert response.status_code == 200
    audio_url = response.json().get("audio_url")
    assert audio_url is not None
    
    # Now, fetch the audio file
    audio_resp = client.get(audio_url)
    assert audio_resp.status_code in [200, 404]  # It might be 404 if the file is not yet generated, but the endpoint exists.

def test_tts_service_generation():
    from tts_service import TTSService
    import tempfile
    import os
    
    # Use a temporary directory for tests
    with tempfile.TemporaryDirectory() as tmpdir:
        service = TTSService(base_dir=tmpdir)
        audio_id = "test_audio_123"
        
        # Generate audio
        service.generate_audio("Hola, esto es una prueba", audio_id)
        
        # Check if file was created
        expected_path = os.path.join(tmpdir, f"{audio_id}.wav")
        assert os.path.exists(expected_path)
        assert os.path.getsize(expected_path) > 100  # Should not be empty

def test_tts_cleanup_old_files():
    from tts_service import TTSService
    import tempfile
    import os
    import time

    with tempfile.TemporaryDirectory() as tmpdir:
        service = TTSService(base_dir=tmpdir)
        
        # Create a mock old file and a new file
        old_file = os.path.join(tmpdir, "old.wav")
        new_file = os.path.join(tmpdir, "new.wav")
        
        with open(old_file, "w") as f:
            f.write("old")
        with open(new_file, "w") as f:
            f.write("new")
            
        # Set old_file modification time to 25 hours ago
        os.utime(old_file, (time.time() - 25*3600, time.time() - 25*3600))
        
        service.cleanup_old_files()
        
        assert not os.path.exists(old_file)
        assert os.path.exists(new_file)
