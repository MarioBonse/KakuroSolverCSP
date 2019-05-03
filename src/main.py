#!/usr/bin/python3
#####################################
#
# Title:  Kakuro Solver as CSP problem
# Author: Mario Bonsembiante
# Date:   jan 2019
#
#####################################
import board
import sys
import time

def main():
    if len(sys.argv)==1:
        name = "test_10(30x30!)"
    else:
        name = sys.argv[1]
    try:
        sq = board.board(load = True, name = "../KakuroStored/"+name+".csv")
    except:
        sq = board.board(load = True, name = "KakuroStored/"+name+".csv")
    sq.print()
    print("\n\n THE SOLUTION IS:")
    start = time.time()
    sq.solve()
    print("in %.10f seconds" %(time.time()- start))


if __name__ == "__main__":
    main()