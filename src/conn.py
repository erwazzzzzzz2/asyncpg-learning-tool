import os

import asyncpg


async def create_conn(database="postgres"):
    return await asyncpg.connect(
        host=os.environ.get("DB_HOST"),
        port=os.environ.get("DB_PORT"),
        user=os.environ.get("DB_USER"),
        database=database,
        password=os.environ.get("DB_PASS"),
    )
