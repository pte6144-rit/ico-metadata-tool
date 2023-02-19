import sys


def main():
    if len(sys.argv) != 2:
        print("Incorrect number of arguments")
        return
    with open(sys.argv[1], 'rb') as fd:
        if fd.read(2) != b'\x00\x00':
            print("Irregular header bytes")
        filetype = fd.read(2)
        if filetype == b'\x01\x00':
            print("ICO image")
        elif filetype == b'\x02\x00':
            print("CUR image")
        else:
            print("Irregular file type")
        num = int.from_bytes(fd.read(2), 'little')
        print(f"This file contains {num} image(s)")
        for i in range(num):
            width = int.from_bytes(fd.read(1), 'little')
            height = int.from_bytes(fd.read(1), 'little')
            print(f"Image #{i+1} is {width}x{height} pixels")
            fd.read(6)
            print(f"Image #{i+1} is {int.from_bytes(fd.read(4), 'little')} bytes")
            fd.read(4)


if __name__ == "__main__":
    main()
