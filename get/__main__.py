import httpx
import rich

client = httpx.Client()

r = client.get("http://httpbin.org/json")
rich.print(f"Response: {r.json()}")
rich.print(f"[bold magenta]Cookies: {client.cookies}[/bold magenta]")


response = client.request("GET", "http://httpbin.org/cookies", cookies={}).json()
rich.print(f"Response: {response}")
