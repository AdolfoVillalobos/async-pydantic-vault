import asyncio
import nest_asyncio
from async_pydantic_vault.typing import NatsStreamingEnv
from dotenv import load_dotenv


async def main():

    nats_credentials = NatsStreamingEnv()
    print(nats_credentials)


nest_asyncio.apply()
load_dotenv(".env")
asyncio.run(main())
