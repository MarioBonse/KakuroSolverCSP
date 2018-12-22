import random
import csv

class square():
    def __init__(self, typesquare = "variable", topright = None, bottomleft = None):
        self.type = typesquare
        self.value = 0
        self.topright = topright
        self.bottomleft = bottomleft
        self.domanin = [1,2,3,4,5,6,7,8,9]

class variable():
    def __init__(self, r , c):
        self.c = c
        self.r = r
        self.value = 0
        self.domanin = [1,2,3,4,5,6,7,8,9]

class constrain():
    def __init__(self, summ, variables):
        self.variables = variables
        self.sum = summ
    


        




# types are "variable", "tofill", "constraints".
# variable can have value from 1 to 9, tofill can't have constraints
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
                        if self.square[row][col].type == "variable":
                            print("|    |", end = "")
                        elif self.square[row][col].type == "fill":
                            print("|----|", end = "")
                        elif self.square[row][col].type == "constraints":
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
                        if self.square[row][col].type == "variable":
                            print("    |", end = "")
                        elif self.square[row][col].type == "fill":
                            print("----|", end = "")
                        elif self.square[row][col].type == "constraints":
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
                self.square[r][c].type = "variable" 
        print("First: tell the black boxes:")
        for r in range(self.n_row): 
            inp = input("Row number %d write the coumn nubers which are black:" %r).split()
            for c in inp:
                self.square[r][int(c)].type = "fill" 
        print("Now tell the constraints coordinate in the top right position (later their value will be asked)")
        for r in range(self.n_row): 
            inp = input("Row number %d write the coumn nubers which are targhet for the row:" %r).split()
            for c in inp:
                toprightvalue = input("The value")
                self.square[r][int(c)].type = "constraints" 
                self.square[r][int(c)].topright = int(toprightvalue) 
        print("Now tell the constraints coordinate in the top right position (later their value will be asked)")
        for r in range(self.n_row): 
            inp = input("Row number %d write the coumn nubers which are targhet for the row:" %r).split()
            for c in inp:
                toprightvalue = input("The value")
                self.square[r][int(c)].type = "constraints" 
                self.square[r][int(c)].bottomleft = int(toprightvalue) 
    
    def save(self):
        table = [[self.encode(r, c) for c in range(self.n_col)] for r in range(self.n_row)]
        writer = csv.writer(open("table.csv", 'w'))
        for results in table:
            writer.writerow(results)
        
    def encode(self, r, c):
        if self.square[r][c].type == "variable":
            return 0
        if self.square[r][c].type == "fill":
            return -1
        else:
            return (self.square[r][c].bottomleft*100) + self.square[r][c].topright

    def decode(self, value):
        if int(value) == 0:
            return ["variable", None, None]
        if int(value) == -1:
            return ["fill", None, None]
        else:
            return (["constraints", int(value)%100, int(value)/100])

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
    
    # in order to make the game easier we do some problem reduction strategies:
    # 1) Node consistency -> each cells has a domani with numbers values lower than the column targhet value
    # 2) Arch consistency -> every couple of variable satisfy the costraints (double cells) we will apply AC-3 algorithm
    # 3) Generalized arch concistency -> the same as before with 3 and 4 variable considered
    
    # This function translate the problem to CSP notation, with variables and constrain
    def toCSP(self):
        # 1 fill the variables
        self.variables = []
        for r in range(self.n_row):
            for c in range(self.n_col):
                if self.square[r][c].type == "variable":
                    self.variables.append(variable(r, c))
        self.constraints = []
        # 2 fill the constraints
        for r in range(self.n_row):
            for c in range(self.n_col):
                if self.square[r][c].type == "constraints":
                    if self.square[r][c].topright != 0:
                        # look up
                        upConstr = []
                        for i in range(1, r + 1):
                            if self.square[r - i][c].type == "variable":
                                upConstr.append(r - i)
                            else:
                                break
                        if not upConstr:
                            for row2 in upConstr: 
                                variables = []
                                for var in self.variables:
                                    if (var.r == row2 and var.c == c):
                                        variables.append(var)
                            self.constraints.append(constrain(self.square[r][c].topright, variables))
                        # look right
                        rightConstr = []
                        for i in range(1, self.n_col - c - 1):
                            if self.square[r][c+i].type == "variable":
                                rightConstr.append(c+i)
                            else:
                                break
                        if not rightConstr:
                            for col2 in rightConstr: 
                                variables = []
                                for var in self.variables:
                                    if (var.r == r and var.c == col2):
                                        variables.append(var)
                            self.constraints.append(constrain(self.square[r][c].topright, variables))
                    # bottown down constraints
                    if self.square[r][c].bottomleft != 0:
                        # look down
                        downConstr = []
                        for i in range(1, self.n_row - r - 1):
                            if self.square[r + i][c].type == "variable":
                                downConstr.append(r + i)
                            else:
                                break
                        if not downConstr:
                            for row2 in downConstr: 
                                variables = []
                                for var in self.variables:
                                    if (var.r == row2 and var.c == c):
                                        variables.append(var)
                            self.constraints.append(constrain(self.square[r][c].bottomleft, variables))
                        # look left
                        leftConstr = []
                        for i in range(1, c + 1):
                            if self.square[r][c-i].type == "variable":
                                leftConstr.append(c-i)
                            else:
                                break
                        if not leftConstr:
                            for col2 in leftConstr: 
                                variables = []
                                for var in self.variables:
                                    if (var.r == r and var.c == col2):
                                        variables.append(var)
                            self.constraints.append(constrain(self.square[r][c].bottomleft, variables))
    
    def nodeConsistency(self):
        # very easy. For each constraints remove from his domain variables which can't be solution
        # aka variable has to be lower than the constraints value
        for constrain in self.constraints:
            if constrain.sum < 10:
                for variable in constrain.variables:
                    variable.domain.pop(range(constrain.sum, 10))

    '''
    def ArchConcistency(self):
        for constrain in self.constraints:
            for index, variable in enumerate(constrain.variables):
                for D in variable.domain:
    '''
    def GeneralArchConsistency(self):
        queue = self.constraints
        while queue:
            constrain = queue[0]
            for index, variable in enumerate(constrain.variables):
                for D in variable.domain:
                    if not findSolutionPossibleSolution(constrain, D, index):
                        variable.domain.remove(D)

            queue.pop(0)   

def findSolutionPossibleSolution(constrain, D, index):
    domains = []
    for i in range(len(constrain.variables)):
        if i != index:
            domains.append(constrain.variables[i].domain)
    summ = constrain.sum - D
    if findSolution(summ, domains):
        return True
    return False

def findSolution(summ, domains):
    if summ < 0:
        return False
    print(domains)
    if len(domains) == 1:
        print(domains)
        #search the solution
        for d in domains[0]:
            if summ - int(d) == 0:
                return True
        return False
    for d in domains[0]:
        if findSolution(summ- d, domains[1:]):
            return True
    return False
            




