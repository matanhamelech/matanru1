import socket
import asyncio
import time
t=time.time()
port=0
async def scan(i: int):
    """
    check if a port for a socket is valid and save it as global i if True
    :param i: the port for the socket to try and connect with
    """
    try:
        global port
        await asyncio.open_connection("127.0.0.1",i)
        print(f"{i} found")
        port=i
    except:
        print(f"{i} not found")


async def main():
    """
    use scan() to find out which port is valid for a server, then connect with valid port.
    """
    await asyncio.gather(*[scan(i) for i in range(10)])
    x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    x.connect(('127.0.0.1',port))
asyncio.run(main())


x=time.time()-t
print(x)
