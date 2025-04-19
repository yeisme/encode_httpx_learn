import httpx
import asyncio
import rich


async def main():
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/get")
        rich.print(r.json())


asyncio.run(main())
