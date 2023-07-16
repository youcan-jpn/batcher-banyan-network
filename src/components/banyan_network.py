# Local Library
from .bit_sorter import BitSorter


class BanyanNetwork:
    def __init__(self, data: list[int]):
        omit_none = list(filter(lambda x: x is not None, data))
        digit = len(bin(max(omit_none))) - 2
        self.data = list(map(lambda s: format(s, f"0{digit}b") if s is not None else None, data))

    def transmit(self):
        return BitSorter.sort_(self.data)
