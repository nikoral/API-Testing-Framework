from typing import List, Dict
import yaml

class DocGenerator:
    def __init__(self):
        self.endpoints: List[Dict] = []

    def add_endpoint(self, 
                    path: str, 
                    method: str, 
                    description: str,
                    params: Dict = None,
                    response: Dict = None):
        self.endpoints.append({
            "path": path,
            "method": method,
            "description": description,
            "parameters": params or {},
            "response": response or {}
        })

    def generate_markdown(self) -> str:
        doc = "# API Documentation\n\n"
        
        for endpoint in self.endpoints:
            doc += f"## {endpoint['path']}\n\n"
            doc += f"Method: `{endpoint['method']}`\n\n"
            doc += f"Description: {endpoint['description']}\n\n"
            
            if endpoint['parameters']:
                doc += "### Parameters:\n```json\n"
                doc += yaml.dump(endpoint['parameters'])
                doc += "```\n\n"
            
            if endpoint['response']:
                doc += "### Response:\n```json\n"
                doc += yaml.dump(endpoint['response'])
                doc += "```\n\n"
        
        return doc
