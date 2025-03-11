from aioquic.asyncio.client import connect
import asyncio
import time

async def quic_client(host='127.0.0.1', port=5003):
    async with connect(host, port) as protocol:
        start = time.time()
        data = await protocol.receive()
        end = time.time()
        print(f"QUIC Transfer Time: {end - start:.2f} seconds")

asyncio.run(quic_client())
