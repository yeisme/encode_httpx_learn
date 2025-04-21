import logging
import httpx
import rich

logging.basicConfig(
    format="%(levelname)s [%(asctime)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("log/log.txt", mode="w"),
    ],
)

response = httpx.get("https://httpbin.org/get")
rich.print(response.json())
