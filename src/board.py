import random
import csv

class square():
    def __init__(self, typesquare = "empty", topright = None, bottomleft = None):
        self.type = typesquare
        self.value = 0
        self.domanin = [1,2,3,4,5,6,7,8,9]
        self.topright = topright
        self.bottomleft = bottomleft


# types are "empty", "tofill", "target".
# empty can have value from 1 to 9, tofill can't have target
class board():
    def __init__(self, n_row, n_col, load = False):
        if not load:
            self.n_row = n_row
            self.n_col = n_col
            self.square = [[square() for row in range(n_col) ]for col in range(n_row)]
        else:
            self.load("table.csv")
        

    def print(self):
        for row in range(self.n_row):
            for i in range(4):
                for col in range(self.n_col):
                    #the cell in the top-left position (0,0)
                    if (i == 0 or i == 3) and (row == 0) and (col == 0):
                        print("+----+",end='')
                    if (i == 0 or i == 3) and (row == 0) and (col != 0):
                        print("----+",end='')
                    if ( i == 3) and (row != 0) and (col != 0):
                        print("----+",end='')
                    if ( i == 3)  and (row != 0) and (col == 0):
                        print("+----+",end='')
                    if (i == 1 or i == 2) and (col == 0):
                        if self.square[row][col].type == "empty":
                            print("|    |", end = "")
                        elif self.square[row][col].type == "fill":
                            print("|----|", end = "")
                        elif self.square[row][col].type == "target":
                            if i == 1 and (self.square[row][col].topright != 0):
                                if self.square[row][col].topright > 9:
                                    print('|\_%d|' %self.square[row][col].topright, end = "")
                                else:
                                    print('|\__%d|' %self.square[row][col].topright, end = "")
                            if i == 1 and (self.square[row][col].topright == 0):
                                print('|\---|', end = "")
                            if i == 2 and (self.square[row][col].bottomleft != 0):
                                if self.square[row][col].bottomleft > 9:
                                    print('|%d \|' %self.square[row][col].bottomleft, end = "")
                                else:
                                    print('| %d \|' %self.square[row][col].bottomleft, end = "")
                            if i == 2 and (self.square[row][col].bottomleft == 0):
                                print('|---\|', end = "")
                    if (i == 1 or i == 2) and (col != 0):
                        if self.square[row][col].type == "empty":
                            print("    |", end = "")
                        elif self.square[row][col].type == "fill":
                            print("----|", end = "")
                        elif self.square[row][col].type == "target":
                            if i == 1 and (self.square[row][col].topright != 0):
                                if self.square[row][col].topright > 9:
                                    print('\_%d|' %self.square[row][col].topright, end = "")
                                else:
                                    print('\__%d|' %self.square[row][col].topright, end = "")
                            if i == 1 and (self.square[row][col].topright == 0):
                                print('\---|', end = "")
                            if i == 2 and (self.square[row][col].bottomleft != 0):
                                if self.square[row][col].bottomleft > 9:
                                    print('%d \|' %self.square[row][col].bottomleft, end = "")
                                else:
                                    print(' %d \|' %self.square[row][col].bottomleft, end = "")
                            if i == 2 and (self.square[row][col].bottomleft == 0):
                                print('---\|', end = "")
                
                    
                if (i != 0) or (row == 0):
                    print("")

    def fill(self):
        for r in range(self.n_row):
            for c in range(self.n_col):
                self.square[r][c].type = "empty" 
        print("First: tell the black boxes:")
        for r in range(self.n_row): 
            inp = input("Row number %d write the coumn nubers which are black:" %r).split()
            for c in inp:
                self.square[r][int(c)].type = "fill" 
        print("Now tell the target coordinate in the top right position (later their value will be asked)")
        for r in range(self.n_row): 
            inp = input("Row number %d write the coumn nubers which are targhet for the row:" %r).split()
            for c in inp:
                toprightvalue = input("The value")
                self.square[r][int(c)].type = "target" 
                self.square[r][int(c)].topright = int(toprightvalue) 
        print("Now tell the target coordinate in the top right position (later their value will be asked)")
        for r in range(self.n_row): 
            inp = input("Row number %d write the coumn nubers which are targhet for the row:" %r).split()
            for c in inp:
                toprightvalue = input("The value")
                self.square[r][int(c)].type = "target" 
                self.square[r][int(c)].bottomleft = int(toprightvalue) 
    
    def save(self):
        table = [[self.encode(r, c) for c in range(self.n_col)] for r in range(self.n_row)]
        writer = csv.writer(open("table.csv", 'w'))
        for results in table:
            writer.writerow(results)
        
    def encode(self, r, c):
        if self.square[r][c].type == "empty":
            return 0
        if self.square[r][c].type == "fill":
            return -1
        else:
            return (self.square[r][c].bottomleft*100) + self.square[r][c].topright

    def decode(self, value):
        if int(value) == 0:
            return ["empty", None, None]
        if int(value) == -1:
            return ["fill", None, None]
        else:
            return (["target", int(value)%100, int(value)/100])

    def load(self, name):
        reader = csv.reader(open(name, 'r'))
        table = list(reader)
        self.n_col = len(table[0])
        self.n_row = len(table)
        self.square = [[square() for row in range(self.n_col) ]for col in range(self.n_row)]
        for r in range(self.n_row):
            for c in range(self.n_col):
                decoded = self.decode(table[r][c])
                self.square[r][c].type = decoded[0] 
                self.square[r][c].bottomleft = decoded[1]
                self.square[r][c].topright = decoded[2]
        

    



        
    #def solve(self):
