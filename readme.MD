<h1 align="center"> 🚀 Caching Proxy with FastAPI </h1><p align="center"> <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis"> </p><p align="center"> This project is a <strong>caching proxy</strong> built using <strong>FastAPI</strong>. It acts as an intermediary between clients and an origin server, caching responses to improve performance and reduce load on the origin server. </p>
✨ Features
<ul> <li><strong>Caching</strong>: Caches responses from the origin server to serve repeated requests faster.</li> <li><strong>Flexible Routing</strong>: Supports multiple HTTP methods (<code>GET</code>, <code>POST</code>, <code>PUT</code>, <code>DELETE</code>, <code>PATCH</code>) and dynamic paths.</li> <li><strong>Cache Hit/Miss Logging</strong>: Logs cache hits and misses for debugging and monitoring.</li> <li><strong>Easy Setup</strong>: Simple setup using Python and FastAPI.</li> </ul>
🎯 Purpose
The purpose of this project is to:

<ol> <li>Demonstrate how to build a caching proxy using FastAPI.</li> <li>Improve response times for repeated requests by serving cached data.</li> <li>Reduce the load on the origin server by handling requests locally when possible.</li> </ol>
🛠️ Setup Instructions
Prerequisites
Python 3.7 or higher

<code>pip</code> (Python package manager)

Steps
<ol> <li> <strong>Clone the Repository</strong>: <pre><code>git clone https://github.com/Zarvi16G/Caching_Proxy.git cd your-repo-name</code></pre> </li> <li> <strong>Set Up a Python Virtual Environment</strong>: <pre><code>python -m venv env source env/bin/activate # On Windows: env\Scripts\activate</code></pre> </li> <li> <strong>Install Dependencies</strong>: <ul> <li>Create a <code>requirements.txt</code> file with the following content: <pre><code>fastapi uvicorn httpx redis </code></pre> </li> <li>Install the dependencies: <pre><code>pip install -r requirements.txt</code></pre> </li> </ul> </li> <li> <strong>Run the Application</strong>: <ul> <li>Start the proxy server with the desired port and origin server: <pre><code>python main.py --port 3000 --origin http://dummyjson.com</code></pre> </li> <li>The application will be available at <code>http://127.0.0.1:3000</code>.</li> </ul> </li> <li> <strong>Test the Proxy</strong>: <ul> <li>Send a request to the proxy: <pre><code>curl http://127.0.0.1:3000/products</code></pre> </li> <li>Check the logs to see if the response is served from the cache or fetched from the origin server.</li> </ul> </li> </ol>
⚙️ Configuration
Command-Line Arguments
You can configure the proxy using the following command-line arguments:

<code>--port</code>: The port on which the proxy server will run (default: <code>8000</code>).

<code>--origin</code>: The origin server URL (e.g., <code>http://dummyjson.com</code>).

Example:

<pre><code>python main.py --port 3000 --origin http://dummyjson.com</code></pre>
🔄 Handling Double Requests
When running the application, you may notice <strong>double requests</strong> in the logs. For example:

<pre><code>Incoming request: GET /products XCache: HIT Incoming request: GET /favicon.ico XCache: HIT</code></pre>
Why This Happens
The first request (<code>/products</code>) is the actual request from the client.

The second request (<code>/favicon.ico</code>) is automatically sent by the browser to fetch the favicon (the icon displayed in the browser tab).

How It's Handled
The proxy handles both requests independently.

If the response is cached, it will return the cached response (<code>XCache: HIT</code>).

If the response is not cached, it will fetch the response from the origin server and cache it (<code>XCache: MISS</code>).

To ignore or handle <code>favicon.ico</code> requests differently, you can modify the <code>proxy</code> function in <code>main.py</code>.

🚦 Example Usage
Start the Proxy
<pre><code>python main.py --port 3000 --origin http://dummyjson.com</code></pre>
Send a Request
<pre><code>curl http://127.0.0.1:3000/products</code></pre>
Example Response (from <code>http://dummyjson.com/products</code>)
json
Copy
{
  "products": [
    {
      "id": 1,
      "title": "iPhone 9",
      "description": "An apple mobile which is nothing like apple",
      "price": 549,
      "discountPercentage": 12.96,
      "rating": 4.69,
      "stock": 94,
      "brand": "Apple",
      "category": "smartphones",
      "thumbnail": "https://dummyjson.com/image/i/products/1/thumbnail.jpg",
      "images": [
        "https://dummyjson.com/image/i/products/1/1.jpg",
        "https://dummyjson.com/image/i/products/1/2.jpg",
        "https://dummyjson.com/image/i/products/1/3.jpg",
        "https://dummyjson.com/image/i/products/1/4.jpg",
        "https://dummyjson.com/image/i/products/1/thumbnail.jpg"
      ]
    },
    ...
  ],
  "total": 100,
  "skip": 0,
  "limit": 30
}
Logs
<pre><code>Incoming request: GET /products XCache: MISS Incoming request: GET /favicon.ico XCache: HIT</code></pre>
🤝 Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

📜 License
This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.

🙏 Acknowledgments
<a href="https://fastapi.tiangolo.com/">FastAPI</a> for the awesome web framework.

<a href="https://www.uvicorn.org/">Uvicorn</a> for the ASGI server.

<a href="https://dummyjson.com/">DummyJSON</a> for providing a test API.
