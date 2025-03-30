import requests
from typing import List, Dict
import ssl
import urllib3

class SecurityChecker:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.vulnerabilities: List[Dict] = []

    def check_ssl(self) -> bool:
        try:
            response = requests.get(self.base_url, verify=True)
            return True
        except ssl.SSLError:
            self.vulnerabilities.append({
                "type": "SSL",
                "description": "Invalid SSL certificate"
            })
            return False

    def check_headers(self) -> List[str]:
        response = requests.get(self.base_url)
        headers = response.headers
        missing_headers = []
        
        security_headers = {
            'Strict-Transport-Security',
            'X-Content-Type-Options',
            'X-Frame-Options',
            'X-XSS-Protection',
        }
        
        for header in security_headers:
            if header not in headers:
                missing_headers.append(header)
                self.vulnerabilities.append({
                    "type": "Missing Header",
                    "description": f"Missing security header: {header}"
                })
        
        return missing_headers

    def check_common_vulnerabilities(self):
        # Basic SQL injection check
        params = {"id": "1' OR '1'='1"}
        response = requests.get(f"{self.base_url}", params=params)
        if "error" in response.text.lower():
            self.vulnerabilities.append({
                "type": "SQL Injection",
                "description": "Possible SQL injection vulnerability"
            })

    def get_security_report(self) -> Dict:
        return {
            "vulnerabilities": self.vulnerabilities,
            "total_issues": len(self.vulnerabilities),
            "security_score": 100 - (len(self.vulnerabilities) * 10)
        }
