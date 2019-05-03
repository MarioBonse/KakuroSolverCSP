#!usr/bin/python3
#####################################
#
# Title:  Kakuro Solver as CSP problem
# Author: Mario Bonsembiante
# Date:   jan 2019
#
#####################################
import board
import time
import sys

def main():
    if len(sys.argv)==1:
        name = "input"
    else:
        name = sys.argv[1]
    try:
        sq = board.board(load = True, name = "../KakuroStored/"+name+".txt", web = True)
    except:
        sq = board.board(load = True, name = "KakuroStored/"+name+".txt", web = True)
    sq.print()
    print("\n\n THE SOLUTION IS:")
    start = time.time()
    sq.solve()
    print("in %.10f seconds" %(time.time()- start))
    name = input("What name would you like to give to it? ")
    sq.save(name)

    
if __name__ == "__main__":
    main()