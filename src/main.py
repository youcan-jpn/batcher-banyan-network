from components.batcher_network import BatcherNetwork


def main():
    ins = [0, 1, 3, 2, 4, 7, 6, 5, 8, 10, 12, 15, 11, 13, 14, 9]
    print("input: ", ins)
    bn = BatcherNetwork(len(ins), ins)
    out = bn.transmit()
    print("output: ", out)

    return


if __name__ == "__main__":
    main()
