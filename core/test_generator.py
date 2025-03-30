import requests
from typing import Dict, List, Optional
import json
from dataclasses import dataclass

@dataclass
class APIEndpoint:
    method: str
    path: str
    params: Optional[Dict] = None
    body: Optional[Dict] = None
    headers: Optional[Dict] = None

class TestGenerator:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.endpoints: List[APIEndpoint] = []

    def add_endpoint(self, endpoint: APIEndpoint):
        self.endpoints.append(endpoint)

    def generate_tests(self) -> str:
        test_code = """import pytest
import requests

"""
        for endpoint in self.endpoints:
            test_code += self._generate_test_for_endpoint(endpoint)
        return test_code

    def _generate_test_for_endpoint(self, endpoint: APIEndpoint) -> str:
        test_name = f"test_{endpoint.method.lower()}_{endpoint.path.replace('/', '_')}"
        test_code = f"""
def {test_name}():
    url = "{self.base_url}{endpoint.path}"
    response = requests.{endpoint.method.lower()}(
        url,
        params={endpoint.params},
        json={endpoint.body},
        headers={endpoint.headers}
    )
    assert response.status_code in [200, 201]
    assert response.json() is not None
"""
        return test_code
