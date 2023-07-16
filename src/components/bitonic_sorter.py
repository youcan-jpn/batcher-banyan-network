from .sorter_2x2 import Sorter2x2


class BitonicSorter:
    @staticmethod
    def sort_(data: list[int], asc: bool):
        n = len(data)
        center = int(n/2)

        if n == 2:
            return Sorter2x2.sort_(data=data, asc=asc)
        elif n % 2 != 0:
            raise ValueError(f"'n' must be even: given {n}")
        else:
            # sort each input pairs
            for i in range(center):
                data[2*i:2*(i+1)] = Sorter2x2.sort_(
                    data=data[2*i:2*(i+1)], asc=asc
                )

            print("after 1st layer: ", str(data))

            next_input = [0 for _ in range(n)]
            # shuffle exchange
            for i in range(n):
                if i < center and i % 2 != 0:
                    next_input[i] = data[i+center-1]
                elif i >= center and i % 2 == 0:
                    next_input[i] = data[i-center+1]
                else:
                    next_input[i] = data[i]

            print("after shuffle exchange: ", next_input)

            out = [0 for _ in range(n)]
            # pass to next bitonic sorter (size: n/2)
            out[:center] = BitonicSorter.sort_(next_input[:center], asc=asc)
            out[center:] = BitonicSorter.sort_(next_input[center:], asc=asc)

            return out
