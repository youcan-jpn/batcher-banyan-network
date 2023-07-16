class Sorter2x2:
    @staticmethod
    def sort_(data: list[int], asc: bool) -> list[int]:
        if len(data) != 2:
            raise ValueError("input length has to be 2")
        reverse = not asc
        return sorted(data, reverse=reverse)
