# API-Testing-Framework
<p>We really appreciate the contribution of everyone who uses this framework. If you want to help us make it even better, you can: Make a donation to support the development <a href="https://www.donationalerts.com/r/nikoral666">DONATE</a></p>
<img src="https://img.shields.io/badge/CoffeeScript-2F2625?logo=coffeescript&logoColor=fff"> 
<p>The API Testing Framework is a platform for automating API testing.</p>
<p>It allows you to:</p>
<p>- Generate tests based on API descriptions.<br />- Create mock servers for test isolation.<br />- Perform load testing.<br />- Generate API documentation.<br />- Check API security.</p>
<h3 id="usage"><strong>Usage</strong></h3>
<ol>
<li><strong>Example usage:</strong>&nbsp;Open and run&nbsp;<code class="">examples/example_usage.py</code>. This script demonstrates the basic features of the framework. Make sure you have added&nbsp;<code class="">print()</code>&nbsp;statements to see the output.</li>
<li><strong>Test generation and execution:</strong>&nbsp;Generate tests using&nbsp;<code class="">TestGenerator</code>&nbsp;in&nbsp;<code class="">examples/example_usage.py</code>. Place the generated test code in the&nbsp;<code class="">tests/test_api.py</code>&nbsp;file. Run tests using&nbsp;<code class="">pytest</code>.</li>
<li><strong>Mock server usage:</strong>&nbsp;Generate mock server code using&nbsp;<code class="">MockHandler</code>&nbsp;in&nbsp;<code class="">examples/example_usage.py</code>. Run the generated code (e.g., using Flask). Make sure your code to run the Mock server is inside the&nbsp;<code class="">if __name__ == "__main__":</code>&nbsp;block.</li>
<li><strong>Load testing:</strong>&nbsp;Use&nbsp;<code class="">LoadTester</code>&nbsp;in&nbsp;<code class="">examples/example_usage.py</code>&nbsp;to perform load testing. Make sure you are running asynchronous code correctly (using&nbsp;<code class="">asyncio.run()</code>).</li>
<li><strong>Documentation generation:</strong>&nbsp;Use&nbsp;<code class="">DocGenerator</code>&nbsp;in&nbsp;<code class="">examples/example_usage.py</code>&nbsp;to generate documentation in Markdown format.</li>
<li><strong>Security check:</strong>&nbsp;Use&nbsp;<code class="">SecurityChecker</code>&nbsp;in&nbsp;<code class="">examples/example_usage.py</code>&nbsp;to check the API's security.</li>
</ol>erated code (e.g., using Flask). Make sure your code to run the Mock server is inside the&nbsp;<code class="">if __name__ == "__main__":</code>&nbsp;block.</li>
<li><strong>Load testing:</strong>&nbsp;Use&nbsp;<code class="">LoadTester</code>&nbsp;in&nbsp;<code class="">examples/example_usage.py</code>&nbsp;to perform load testing. Make sure you are running asynchronous code correctly (using&nbsp;<code class="">asyncio.run()</code>).</li>
<li><strong>Documentation generation:</strong>&nbsp;Use&nbsp;<code class="">DocGenerator</code>&nbsp;in&nbsp;<code class="">examples/example_usage.py</code>&nbsp;to generate documentation in Markdown format.</li>
<li><strong>Security check:</strong>&nbsp;Use&nbsp;<code class="">SecurityChecker</code>&nbsp;in&nbsp;<code class="">examples/example_usage.py</code>&nbsp;to check the API's security.</li>
</ol>
