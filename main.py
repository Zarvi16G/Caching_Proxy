from fastapi import FastAPI, Request, HTTPException
import uvicorn
import argparse, httpx, redis, json

# Parse arguments from CLI
parser = argparse.ArgumentParser(description="Caching Proxy Arguments")
parser.add_argument("--port", type=int, help="Specify the port number")
parser.add_argument("--origin", type=str, help="Specify the URL")
parser.add_argument("--clear-cache", action="store_true", help="Clear cache")

args = parser.parse_args()

def clear_cache():
    """Function to clear the cache."""
    r.flushdb()  # Assuming `delete_all` is the method to clear the cache
    print("Cache cleared!")



r = redis.Redis(host='localhost', port=6379, db=0)

app = FastAPI()

async def fetch_and_cache(url: str, path, request):
    target_url = f"{url}/{path}"

    async with httpx.AsyncClient() as client:
        response = await client.get(target_url)
        headers = dict(request.headers)
        headers.pop("host", None)  # Remove the original host header

        response = await client.request(
            method=request.method,
            url=target_url,
            headers=headers,
            params=request.query_params,
        )

            # Return the response from the target origin
        # Extract response components
        status_code = response.status_code
        headers = dict(response.headers)

        dict_format = {
            "status_code": status_code,
            "headers": headers,
        }

        json_format = json.dumps(dict_format, indent=4)
        # Store in cache
        r.set(args.origin, json_format)

        return dict_format
        

async def get_cached_response(url: str):
    return_request = r.get(url)
    if return_request is not None:
        deserialized_request = json.loads(return_request)
        return deserialized_request
    else:
        return None

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy(request: Request, path: str):
    print(f"Incoming request: {request.method} {path}")
    # Retrieve from cachec
    cached_response = await get_cached_response(args.origin)
    if cached_response:
        print("XCache: HIT")
        return cached_response
        
    else:
        response = await fetch_and_cache(args.origin, path, request)
        print("XCache: MISS")
        return response

def start_server():
    if args.clear_cache:
        clear_cache()
    else: 
        uvicorn.run("main:app", host="0.0.0.0", port=args.port, reload=True)


if __name__ == "__main__":
    start_server()