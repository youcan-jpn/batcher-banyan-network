# Standard Library
import random

# First Party Library
from components.batcher_network import BatcherNetwork


def main():
    ins = list(range(32))
    random.shuffle(ins)

    print("input: ", ins)
    bn = BatcherNetwork(len(ins), ins)
    out = bn.transmit()
    print("output: ", out)

    return


if __name__ == "__main__":
    main()
