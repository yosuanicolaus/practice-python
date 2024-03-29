import random

# pair programming with Antoine
# what is the probability that out of the 32 chess pieces he have,
# we got a matching pairs of magnets for all of them except for the king pieces
# answer: 2% ~ question is, is it a miracle?

# we made 2 version of this program
# one with the monte carlo method (which is this file)
# the other written in rust for simulating every possible combinations (2**32)


def discriminate(pieces: list):
    # all match
    disrepancy_pawns = abs(sum(pieces[:8]) - sum(pieces[8:16]))
    disrepancy_knights = abs(sum(pieces[16:18]) - sum(pieces[18:20]))
    disrepancy_bishops = abs(sum(pieces[20:22]) - sum(pieces[22:24]))
    disrepancy_rooks = abs(sum(pieces[24:26]) - sum(pieces[26:28]))
    disrepancy_queens = abs(sum(pieces[28:29]) - sum(pieces[29:30]))
    disrepancy_kings = abs(sum(pieces[30:31]) - sum(pieces[31:32]))

    return (
        sum(
            (
                disrepancy_pawns,
                disrepancy_knights,
                disrepancy_bishops,
                disrepancy_rooks,
                disrepancy_queens,
                disrepancy_kings,
            )
        )
        <= 1
    )


def main():
    miracle = 0
    test_count = 100_000

    for _ in range(test_count):
        pieces = [random.randint(0, 1) for _ in range(32)]
        if discriminate(pieces):
            miracle += 1

    print(miracle / test_count)


if __name__ == "__main__":
    main()
