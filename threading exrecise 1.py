from pathlib import Path
from threading import Event, Thread

STRING = "synchronization"
FILE = Path.cwd() / "file.txt"
printed_odd = Event()
printed_even = Event()


def write_even():
    for char in STRING[1::2]:
        printed_odd.wait()
        print(char)
        printed_even.set()
        printed_odd.clear()


def main():
    even_printer = Thread(target=write_even)
    even_printer.start()

    printed_even.set()

    for char in STRING[::2]:
        printed_even.wait()
        print(char)
        printed_odd.set()
        printed_even.clear()

    even_printer.join()


if __name__ == '__main__':
    main()