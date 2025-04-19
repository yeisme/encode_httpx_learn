from httpx import post
import rich

r = post("https://httpbin.org/post", data={"key": "value"})
rich.print(r.json())
