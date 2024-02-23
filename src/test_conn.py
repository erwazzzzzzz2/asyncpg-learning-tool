import asyncio
import os

import asyncpg


async def test_conn():
    connection = await asyncpg.connect(
        host=os.environ.get("DB_HOST"),
        port=os.environ.get("DB_PORT"),
        user=os.environ.get("DB_USER"),
        database="postgres",
        password=os.environ.get("DB_PASS"),
    )
    version = connection.get_server_version()
    print(f"Connected! Postgres version is {version}")
    await connection.close()


asyncio.run(test_conn())
