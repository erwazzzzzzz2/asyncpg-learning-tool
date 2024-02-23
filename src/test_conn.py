import asyncio

from conn import create_conn


async def test_conn():

    connection = await create_conn()
    version = connection.get_server_version()
    print(f"Connected! Postgres version is {version}")
    await connection.close()


asyncio.run(test_conn())
