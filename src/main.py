# Standard Library
import random

# First Party Library
from components.banyan_network import BanyanNetwork
from components.batcher_network import BatcherNetwork


def main():
    ins = list(range(8))
    ins[3] = float("INF")
    random.shuffle(ins)

    print("input: ", ins)
    ban = BatcherNetwork(len(ins), ins)
    out1 = ban.transmit()
    print("Batcher Network output:")
    print(out1)
    out1 = inf2none(data=out1)
    byn = BanyanNetwork(data=out1)
    out2 = byn.transmit()
    print("Banyan Network output:")
    print(out2)
    print("Decimalized Output")
    print(decimalize(out2))

    return


def inf2none(data: list[int | None]):
    while float("INF") in data:
        data[data.index(float("INF"))] = None
    return data


def decimalize(data: list[int | None]):
    return list(map(lambda x: int(x, 2) if x is not None else None, data))


if __name__ == "__main__":
    main()
