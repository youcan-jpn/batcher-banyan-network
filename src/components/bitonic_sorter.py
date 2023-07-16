# Local Library
from .sorter_2x2 import Sorter2x2


class BitonicSorter:
    @staticmethod
    def sort_(data: list[int], asc: bool):
        n = len(data)
        n_half = int(n / 2)
        mid_s_id = int(n / (2 * 2))

        if n == 2:
            return Sorter2x2.sort_(data=data, asc=asc)
        elif n % 2 != 0:
            raise ValueError(f"'n' must be even: given {n}")
        else:
            l1_input = [0] * n
            # shuffle exchange
            for l1_id in range(n_half):
                for port in range(2):
                    if l1_id < mid_s_id:
                        next_port = 2 * l1_id
                    else:
                        next_port = 2 * (l1_id - mid_s_id) + 1
                    next_sorter_id = port

                    l1_input[int(next_sorter_id * n / 2) + next_port] = data[2 * l1_id + port]

            # sort each input pairs
            for i in range(n_half):
                data[2 * i : 2 * (i + 1)] = Sorter2x2.sort_(data=l1_input[2 * i : 2 * (i + 1)], asc=asc)

            next_input = [0 for _ in range(n)]
            # shuffle exchange
            # l1 is comprised of n/2 2x2-switches with different l1_id (0 to n/2-1)
            # each 2x2-switch has two ports
            # next layer is comprised of 2 (n/2 x n/2)-switches with differenct next_sorter_id (0 or 1)
            # each (n/2 x n/2)-switch has n/2 ports
            for l1_id in range(n_half):
                for port in range(2):
                    if l1_id < mid_s_id:
                        next_port = 2 * l1_id
                    else:
                        next_port = 2 * (l1_id - mid_s_id) + 1
                    next_sorter_id = port

                    next_input[int(next_sorter_id * n / 2) + next_port] = data[2 * l1_id + port]

            print("after shuffle exchange: ", next_input)

            out = [0 for _ in range(n)]
            # pass to next bitonic sorter (size: n/2)
            out[:n_half] = BitonicSorter.sort_(next_input[:n_half], asc=asc)
            out[n_half:] = BitonicSorter.sort_(next_input[n_half:], asc=asc)

            return out
