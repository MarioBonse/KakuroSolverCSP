#!/usr/bin/python3
import board

def main():
    try:
        sq = board.board(load = True, name = "../KakuroStored/test_2.csv")
    except:
        sq = board.board(load = True, name = "KakuroStored/test_2.csv")
    sq.print()
    sq.toCSP()
    sq.nodeConsistency()
    sq.GeneralArchConsistency()
    print("\n\n")
    sq.solve()
    print("\n")


if __name__ == "__main__":
    main()