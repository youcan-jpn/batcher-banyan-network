# Local Library
from .bitonic_sorter import BitonicSorter


class BatcherNetwork:
    def __init__(self, n: int, data: list[int]):
        self.n = n
        self.data = data
        self.current_size = 2

    def transmit(self):
        while self.current_size <= self.n:
            bitonic_sorter_num = int(self.n / self.current_size)
            out = [0] * self.n

            for sorter_id in range(bitonic_sorter_num):
                out[sorter_id * self.current_size : (sorter_id + 1) * self.current_size] = BitonicSorter.sort_(
                    data=self.data[sorter_id * self.current_size : (sorter_id + 1) * self.current_size],
                    asc=sorter_id % 2 == 0,
                )

            self.current_size *= 2
            self.data = out

        return self.data
