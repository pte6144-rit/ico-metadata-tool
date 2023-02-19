import sys


def main():
    if len(sys.argv) != 2:
        print("Please provide one filepath as a commandline argument")
        return
    with open(sys.argv[1], 'rb') as fd:
        if fd.read(2) != b'\x00\x00':                               # Should always be 0
            print("Irregular header bytes")
        filetype = fd.read(2)                                       # Determines a icon or static cursor file
        if filetype == b'\x01\x00':
            print("ICO image")
        elif filetype == b'\x02\x00':
            print("CUR image")
        else:
            print("Irregular file type")
        num = int.from_bytes(fd.read(2), 'little')                  # Determines the number of images contained
        print(f"This file contains {num} image(s)")
        for i in range(num):
            width = int.from_bytes(fd.read(1), 'little')
            height = int.from_bytes(fd.read(1), 'little')
            print(f"Image #{i+1} is {width}x{height} pixels")       # Prints the pixel size field
            fd.read(6)  # Contains color metadata and, in cursors only, an offset from the focus to the top left
            print(f"Image #{i+1} is {int.from_bytes(fd.read(4), 'little')} bytes")  # Prints the byte size field
            fd.read(4)  # These 4 bytes store the offset from the beginning of the file to the image.
                        # The image could either be a png or bitmap. Usually a png. Pngs will still have
                        # their headers, but bitmaps will not.


if __name__ == "__main__":
    main()
