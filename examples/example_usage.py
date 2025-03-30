from api_testing_framework.core.test_generator import TestGenerator, APIEndpoint
from api_testing_framework.core.mock_handler import MockHandler
from api_testing_framework.core.load_tester import LoadTester
from api_testing_framework.core.doc_generator import DocGenerator
from api_testing_framework.core.security_checker import SecurityChecker

# An example of using a test generator
test_gen = TestGenerator("https://api.example.com")
test_gen.add_endpoint(APIEndpoint(
    method="GET",
    path="/users",
    params={"page": 1},
    headers={"Authorization": "Bearer token"}
))
test_code = test_gen.generate_tests()

# An example of using a mock server
mock_handler = MockHandler()
mock_handler.add_mock("/users", "GET", {
    "users": [{"id": 1, "name": "John"}]
})
mock_server_code = mock_handler.generate_mock_server()

# An example of load testing
async def run_load_test():
    load_tester = LoadTester("https://api.example.com/users")
    await load_tester.run_load_test()
    stats = load_tester.get_statistics()
    print(stats)

# Example of documentation generation
doc_gen = DocGenerator()
doc_gen.add_endpoint(
    path="/users",
    method="GET",
    description="Get list of users",
    params={"page": "Page number"},
    response={"users": [{"id": "int", "name": "string"}]}
)
docs = doc_gen.generate_markdown()

# Example of a security check
security = SecurityChecker("https://api.example.com")
security.check_ssl()
security.check_headers()
security.check_common_vulnerabilities()
report = security.get_security_report()

if __name__ == "__main__":
    print("Generated test code:", test_code)
    print("\nGenerated mock server:", mock_server_code)
    print("\nGenerated documentation:", docs)
    print("\nSecurity report:", report)
