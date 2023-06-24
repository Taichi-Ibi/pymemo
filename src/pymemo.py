import os
from pathlib import Path


class PyMemo:
    path = Path.cwd().parent / "data" / "pymemo.txt"

    def __init__(self) -> None:
        self.path.touch(exist_ok=True)
        self.memos = readsets(self.path)

    def show(self) -> None:
        printm(self.memos)

    def find(self, *chars) -> None:
        printm(match(self.memos, chars))

    def write(self, *chars) -> None:
        self.memos = self.memos | set(chars)
        writesets(self.path, self.memos)

    def clear(self) -> None:
        writeblank(self.path)
        self.memos = set()

    def delete(self, *chars) -> None:
        self.memos = self.memos - match(self.memos, chars)
        writeblank(self.path)
        self.write(*self.memos)


def match(memos, chars) -> set:
    _memos = memos
    for c in chars:
        _memos = {m for m in _memos if c in m}
    return _memos


def writesets(path, memos) -> None:
    _memos = ("\n").join(sorted(memos))
    with path.open(mode="r+") as f:
        f.writelines(_memos)


def writeblank(path) -> None:
    with path.open("r+") as f:
        f.truncate(0)


def readsets(path) -> set:
    with path.open(mode="r") as f:
        memos = f.readlines()
    memos = {m.strip(os.linesep) for m in memos}
    return memos


def printm(memos) -> None:
    tex = ("\n").join(sorted(memos))
    if tex:
        print(tex)
