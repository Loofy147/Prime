# app/backend/services/model_adapter.py
import redis
import json
import os
from abc import ABC, abstractmethod
import hashlib
import uuid

# Connect to Redis
redis_url = os.environ.get("REDIS_URL", "redis://redis:6379")
redis_client = redis.from_url(redis_url)

class ModelAdapter(ABC):
    @abstractmethod
    def _get_response(self, prompt: str, context_ids: list):
        pass

    def query(self, prompt: str, context_ids: list):
        # Create a unique key for the prompt and context
        cache_key = f"query:{hashlib.sha256((prompt + str(context_ids)).encode()).hexdigest()}"

        # Check cache first
        cached_result = redis_client.get(cache_key)
        if cached_result:
            return json.loads(cached_result)

        # If not in cache, get the response from the model
        answer, provenance = self._get_response(prompt, context_ids)

        # Cache the result
        redis_client.set(cache_key, json.dumps((answer, provenance)), ex=3600) # Cache for 1 hour

        return answer, provenance

class OpenAIAdapter(ModelAdapter):
    def _get_response(self, prompt: str, context_ids: list):
        # Placeholder for OpenAI API call
        answer = f"OpenAI response for: {prompt}"
        provenance = [{"id": str(uuid.uuid4()), "type": "internal_note", "cursor": "line 5", "confidence": 0.9, "snippet_hash": "abcde12345"}]
        return answer, provenance

class SelfHostAdapter(ModelAdapter):
    def _get_response(self, prompt: str, context_ids: list):
        # Placeholder for self-hosted model inference
        answer = f"Self-hosted response for: {prompt}"
        provenance = [{"id": str(uuid.uuid4()), "type": "internal_note", "cursor": "line 10", "confidence": 0.8, "snippet_hash": "fghij67890"}]
        return answer, provenance

def get_model_adapter(adapter_name: str) -> ModelAdapter:
    if adapter_name == "openai":
        return OpenAIAdapter()
    elif adapter_name == "selfhost":
        return SelfHostAdapter()
    else:
        raise ValueError("Invalid model adapter")
