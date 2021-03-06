#!/usr/bin/python3
#####################################
#
# Title:  Kakuro Solver as CSP problem
# Author: Mario Bonsembiante
# Date:   jan 2019
#
#####################################
import board

def main():
    row = int(input("how many rows do you want? "))
    columns = int(input("how many columns do you want? "))
    sq = board.board(int(row), int(columns))
    sq.fill()
    sq.print()
    answ = input("is this one the board you want to create?(1 OR 0) ")
    while bool(answ) == False:
        sq.fill()
        answ = input("is this one the board you want to create? ")
        sq.print()
    name = input("Write the name you want to give it? ")
    sq.save(name)
    

if __name__ == "__main__":
    main()