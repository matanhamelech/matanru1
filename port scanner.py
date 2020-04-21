import socket
import asyncio
def scan(adress):
    """
    tries to connect to an adress with different ports, if succeeds returns the port
    :param adress: the adress to which the socket tries to connect
    :return: valid port to adress
    """
    x=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for num in range(145,155):
        try:
            a,b=x.connect((adress,num))
            l=num
            return l
        except:
            pass


def main():
    """
    activate scan() and connects to the '127.0.0.1' and the port returned
    """
    port=scan('127.0.0.1')
    x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    x.connect(('127.0.0.1',port))
main()