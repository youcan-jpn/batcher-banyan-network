class BitSorter2x2:
    @staticmethod
    def sort_(data: list[str | None], target_bit: int) -> list[str | None]:
        """
        Parameters
        ----------
        data : list[str | None]
            eg) ['0010', None, '0101']
        target_bit : int
            check i-th bit in data (i=target_bit, 0-indexed)
            0th bit of '1010' is 1
            2nd bit of '1010' is 1
        """
        if data[0] is None and data[1] is None:
            return [None, None]

        if data[0] is None:
            b1, d1 = data[1][target_bit], data[1]
            b2, d2 = None, None
        elif data[1] is None:
            b1, d1 = data[0][target_bit], data[0]
            b2, d2 = None, None
        else:
            b1, d1 = data[0][target_bit], data[0]
            b2, d2 = data[1][target_bit], data[1]

        if b1 == b2:
            raise ValueError(f"HOL detected: i: {target_bit}, {data[0]}, {data[1]}")

        if b1 == "1":
            return [d2, d1]
        elif b1 == "0":
            return [d1, d2]
        else:
            raise ValueError("data is not given in binary")
