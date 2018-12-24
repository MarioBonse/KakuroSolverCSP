#!/usr/bin/python3
import board
import sys
def main():
    if len(sys.argv)==1:
        name = "test_2"
    else:
        name = sys.argv[1]
    try:
        sq = board.board(load = True, name = "../KakuroStored/"+name+".csv")
    except:
        sq = board.board(load = True, name = "KakuroStored/"+name+".csv")
    sq.print()
    sq.toCSP()
    sq.nodeConsistency()
    sq.GeneralArchConsistency()
    print("\n\n")
    sq.solve()
    print("\n")


if __name__ == "__main__":
    main()