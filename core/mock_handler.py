from typing import Dict, Any
import json

class MockHandler:
    def __init__(self):
        self.mocks: Dict[str, Any] = {}

    def add_mock(self, endpoint: str, method: str, response: Dict):
        key = f"{method.upper()}:{endpoint}"
        self.mocks[key] = response

    def get_mock(self, endpoint: str, method: str) -> Dict:
        key = f"{method.upper()}:{endpoint}"
        return self.mocks.get(key, {"error": "Mock not found"})

    def generate_mock_server(self) -> str:
        server_code = """
from flask import Flask, jsonify

app = Flask(__name__)
"""
        for key, response in self.mocks.items():
            method, endpoint = key.split(":")
            server_code += f"""
@app.route('{endpoint}', methods=['{method}'])
def mock_{endpoint.replace('/', '_')}():
    return jsonify({response})
"""
        return server_code
