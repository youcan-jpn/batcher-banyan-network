# Local Library
from .bit_sorter_2x2 import BitSorter2x2

# class BitSorter:
#     @staticmethod
#     def sort_(data: list[str | None], switch_num_per_group: int, target_bit: int):
#         n = len(data)

#         # shuffle exchange
#         # detail is described in sorter_2x2.py
#         n_half = int(n / 2)
#         mid = int(n_half / 2)
#         shuffled = [""]*n
#         for i in range(n_half):
#             for p in range(2):
#                 if i < mid:
#                     np = 2 * i
#                 else:
#                     np = 2 * (i - mid) + 1
#                 ni = p

#                 shuffled[int(ni*n_half) + np] = data[2*i+p]

#         from_next_layer = [""] * n
#         from_next_layer[:n_half] = BitSorter.sort_(data=shuffled[:n_half], target_bit=target_bit+1)
#         from_next_layer[n_half:] = BitSorter.sort_(data=shuffled[n_half:], target_bit=target_bit+1)
#         return from_next_layer


class BitSorter:
    @staticmethod
    def sort_(data: list[str | None], target_bit: int = 0):
        n = len(data)
        n_half = int(n / 2)
        mid_s_id = int(n / (2 * 2))

        if n == 2:
            return BitSorter2x2.sort_(data=data, target_bit=target_bit)
        elif n % 2 != 0:
            raise ValueError(f"'n' must be even: given {n}")
        else:
            l1_input = [""] * n
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
                data[2 * i : 2 * (i + 1)] = BitSorter2x2.sort_(
                    data=l1_input[2 * i : 2 * (i + 1)], target_bit=target_bit
                )

            next_input = [""] * n
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

            out = [0 for _ in range(n)]
            # pass to next bitonic sorter (size: n/2)
            out[:n_half] = BitSorter.sort_(next_input[:n_half], target_bit=target_bit + 1)
            out[n_half:] = BitSorter.sort_(next_input[n_half:], target_bit=target_bit + 1)

            return out
