import pytest
import anthropic
from unittest.mock import patch, MagicMock
from ai_generator import AIGenerator

def test_anthropic_rate_limit_error():
    generator = AIGenerator("fake_key", "fake_model")
    
    with patch.object(generator.client.messages, 'create') as mock_create:
        # Create a mock response for the exception
        mock_response = MagicMock()
        mock_response.status_code = 429
        
        mock_create.side_effect = anthropic.RateLimitError(
            message="Rate limit exceeded",
            response=mock_response,
            body={}
        )
        
        response = generator.generate_response("hola")
        assert "El servicio está experimentado alta demanda" in response

def test_anthropic_api_connection_error():
    generator = AIGenerator("fake_key", "fake_model")
    
    with patch.object(generator.client.messages, 'create') as mock_create:
        mock_request = MagicMock()
        
        mock_create.side_effect = anthropic.APIConnectionError(
            message="Connection error",
            request=mock_request
        )
        
        response = generator.generate_response("hola")
        assert "El servicio está experimentado alta demanda" in response
