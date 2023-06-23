import os
from pathlib import Path


def readsets(path) -> set:
    with path.open(mode="r") as f:
        memos = f.readlines()
    memos = {m.strip(os.linesep) for m in memos}
    return memos


def print_memos(memos) -> None:
    tex = ("\n").join(sorted(memos))
    if tex:
        print(tex)


class PyMemo:
    def __init__(self) -> None:
        self.path = Path.home() / ".pymemo"
        self.path.touch(exist_ok=True)

    def show(self) -> None:
        memos = readsets(self.path)
        print_memos(memos)

    def clear(self) -> None:
        with self.path.open("r+") as f:
            f.truncate(0)

    def write(self, *chars) -> None:
        memos = readsets(self.path)
        for c in chars:
            memos.add(c)
        memos = ("\n").join(sorted(memos))
        self.clear()
        with self.path.open(mode="r+") as f:
            f.writelines(memos)

    def find(self, *chars) -> None:
        memos = readsets(self.path)
        for c in chars:
            memos = {m for m in memos if c in m}
        print_memos(memos)

    def delete(self, *chars) -> None:
        memos = readsets(self.path)
        for c in chars:
            memos.discard(c)
        self.clear()
        for m in memos:
            self.write(m)
