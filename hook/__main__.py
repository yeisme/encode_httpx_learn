import httpx


def log_request(request):
    print(f"请求事件钩子: {request.method} {request.url} - 等待响应")


def log_response(response):
    request = response.request
    print(
        f"响应事件钩子: {request.method} {request.url} - 状态码 {response.status_code}"
    )


client = httpx.Client(
    event_hooks={"request": [log_request], "response": [log_response]}
)

response = client.get("https://httpbin.org/get")
print(response.text)
