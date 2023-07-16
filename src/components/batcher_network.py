from .bitonic_sorter import BitonicSorter


class BatcherNetwork:
    def __init__(self, n: int, data: list[int]):
        self.n = n
        self.data = data
        self.current_size = 2

    def transmit(self):
        while self.current_size <= self.n:
            bitonic_sorter_num = int(self.n / self.current_size)
            next_layer_data = [0 for _ in range(self.n)]

            for i in range(bitonic_sorter_num):
                for j in range(self.current_size):
                    if j < self.current_size/2:
                        next_layer_data[2*j+i*self.current_size] = self.data[j+i*self.current_size]
                    else:
                        next_layer_data[2*j-self.current_size+1+i*self.current_size] = self.data[j+i*self.current_size]

            out = [0 for _ in range(self.n)]

            for sorter_id in range(bitonic_sorter_num):
                out[sorter_id*self.current_size:(sorter_id+1)*self.current_size] = BitonicSorter.sort_(data=next_layer_data[sorter_id*self.current_size:(sorter_id+1)*self.current_size], asc=sorter_id%2 == 0)

            self.current_size *= 2
            self.data = out

        return self.data
