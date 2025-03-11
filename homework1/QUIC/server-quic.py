from aioquic.asyncio import serve
from aioquic.asyncio.protocol import QuicConnectionProtocol
from aioquic.quic.configuration import QuicConfiguration
import asyncio

class QuicServerProtocol(QuicConnectionProtocol):
    async def stream(self, stream_id):
        file_size = 500 * 1024 * 1024
        data = b'0' * file_size
        self._quic.send_stream_data(stream_id, data, end_stream=True)

async def quic_server(host="0.0.0.0", port=5003):
    configuration = QuicConfiguration(is_server=True)
    await serve(host, port, configuration=configuration, create_protocol=QuicServerProtocol)

asyncio.run(quic_server())
