import os


def verify_filesize(filename: str, size: int) -> bool:
    if not os.path.exists(filename):
        return True
    if os.path.getsize(filename) < size:
        return True
    return False


if verify_filesize("/tmp/big.txt", 10) is False:
    print("file exceeds limit")
