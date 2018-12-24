import sys
import csv

# Class used in order to manage the board cells. 
class Cell():
    def __init__(self, typeCell = "variable", topright = 0, bottomleft = 0):
        self.type = typeCell
        self.value = 0
        self.topright = topright
        self.bottomleft = bottomleft

# Class used in order to solve the problem as a generic CSP problem.
# It represents the white cells
class variable():
    def __init__(self, r , c):
        self.constrain = []
        self.c = c
        self.r = r
        self.domain = [1,2,3,4,5,6,7,8,9]

# It represents the diagonal cells which are the constraints that the variables has to satisfy
class constrain():
    def __init__(self, summ, variables):
        self.variables = variables
        self.sum = summ
    
# This is the more important class. It represent the board object.
# It has the cells and then can be converted as CSP notation, a graph with variables (which are the nodes)
# And archs (which are the constraints)
class board():
    def __init__(self, n_row = 12, n_col = 12, load = False, name = ""):
        if not load:
            self.n_row = n_row
            self.n_col = n_col
            print("not loaded")
            self.Cell = [[Cell() for row in range(n_col) ]for col in range(n_row)]
        else:
            self.load(name)
        
    # Function that show the board int the terminal
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
                        if self.Cell[row][col].type == "variable":
                            if self.Cell[row][col].value == 0 or i == 2:
                                print("|    |", end = "")
                            else:
                                print("|  %d |" % self.Cell[row][col].value, end = "")
                        elif self.Cell[row][col].type == "fill":
                            print("|----|", end = "")
                        elif self.Cell[row][col].type == "constraints":
                            if i == 1 and (self.Cell[row][col].topright != 0):
                                if self.Cell[row][col].topright > 9:
                                    print('|\_%d|' %self.Cell[row][col].topright, end = "")
                                else:
                                    print('|\__%d|' %self.Cell[row][col].topright, end = "")
                            if i == 1 and (self.Cell[row][col].topright == 0):
                                print('|\---|', end = "")
                            if i == 2 and (self.Cell[row][col].bottomleft != 0):
                                if self.Cell[row][col].bottomleft > 9:
                                    print('|%d \|' %self.Cell[row][col].bottomleft, end = "")
                                else:
                                    print('| %d \|' %self.Cell[row][col].bottomleft, end = "")
                            if i == 2 and (self.Cell[row][col].bottomleft == 0):
                                print('|---\|', end = "")
                    if (i == 1 or i == 2) and (col != 0):
                        if self.Cell[row][col].type == "variable":
                            if self.Cell[row][col].value == 0 or i == 2:
                                print("    |", end = "")
                            else:
                                print("  %d |" % self.Cell[row][col].value, end = "")
                        elif self.Cell[row][col].type == "fill":
                            print("----|", end = "")
                        elif self.Cell[row][col].type == "constraints":
                            if i == 1 and (self.Cell[row][col].topright != 0):
                                if self.Cell[row][col].topright > 9:
                                    print('\_%d|' %self.Cell[row][col].topright, end = "")
                                else:
                                    print('\__%d|' %self.Cell[row][col].topright, end = "")
                            if i == 1 and (self.Cell[row][col].topright == 0):
                                print('\---|', end = "")
                            if i == 2 and (self.Cell[row][col].bottomleft != 0):
                                if self.Cell[row][col].bottomleft > 9:
                                    print('%d \|' %self.Cell[row][col].bottomleft, end = "")
                                else:
                                    print(' %d \|' %self.Cell[row][col].bottomleft, end = "")
                            if i == 2 and (self.Cell[row][col].bottomleft == 0):
                                print('---\|', end = "")
                
                    
                if (i != 0) or (row == 0):
                    print("")

    # function that helps the user who want to add a new kakuro board to the database
    def fill(self):
        for r in range(self.n_row):
            for c in range(self.n_col):
                self.Cell[r][c].type = "variable" 
        print("First: tell the black boxes:")
        for r in range(self.n_row): 
            inp = input("Row number %d write the coumn nubers which are black:" %r).split()
            for c in inp:
                self.Cell[r][int(c)].type = "fill" 
        print("Now tell the constraints coordinate in the top right position (later their value will be asked)")
        for r in range(self.n_row): 
            inp = input("Row number %d write the coumn nubers which are targhet for the row:" %r).split()
            for c in inp:
                toprightvalue = input("The value")
                self.Cell[r][int(c)].type = "constraints" 
                self.Cell[r][int(c)].topright = int(toprightvalue.split()[0]) 
        print("Now tell the constraints coordinate in the top bottom-left (later their value will be asked)")
        for r in range(self.n_row): 
            inp = input("Row number %d write the coumn nubers which are targhet for the row:" %r).split()
            for c in inp:
                toprightvalue = input("The value")
                self.Cell[r][int(c)].type = "constraints" 
                self.Cell[r][int(c)].bottomleft = int(toprightvalue.split()[0]) 
    
    def save(self, name):
        table = [[self.encode(r, c) for c in range(self.n_col)] for r in range(self.n_row)]
        writer = csv.writer(open("../KakuroStored/"+name+".csv", 'w'))
        for results in table:
            writer.writerow(results)
        
    # function usefull for saving the bord in a CSV file. It translate the cells type and value into numbers     
    def encode(self, r, c):
        if self.Cell[r][c].type == "variable":
            return 0
        if self.Cell[r][c].type == "fill":
            return -1
        else:
            return (int(self.Cell[r][c].bottomleft)*100) + int(self.Cell[r][c].topright)

    def decode(self, value):
        if int(value) == 0:
            return ["variable", 0, 0]
        if int(value) == -1:
            return ["fill", 0, 0]
        else:
            return (["constraints", int(value)%100, int(value)/100])

    def load(self, name):
        reader = csv.reader(open(name, 'r'))
        table = list(reader)
        self.n_col = len(table[0])
        self.n_row = len(table)
        self.Cell = [[Cell() for row in range(self.n_col) ]for col in range(self.n_row)]
        for r in range(self.n_row):
            for c in range(self.n_col):
                decoded = self.decode(table[r][c])
                self.Cell[r][c].type = decoded[0] 
                self.Cell[r][c].topright = int(decoded[1])
                self.Cell[r][c].bottomleft = int(decoded[2])
    

    '''
    NOW This is the algorithm part of this project. 
    It implements:
    1) It translate the board into two structures. The variables and the constraints.
    -> they will be used in order to find a solution
    2) Find the solution
    -> This is obtained with problem reduction strategies (because kakuro must have just one solution):
    # 1) Node consistency -> each cells has a domain. Each domains can't have value bigger than the constraint 
    # 2) General Arch consistency -> every tuple of variable satisfy the costraints (double cells) we will apply an algorithm similar to AC-3 algorithm
        which works for dual arch consistency but the concept is the same

    '''
   
    
    # This function translate the problem to CSP notation, with variables and constrain
    def toCSP(self):
        # 1 fill the variables
        self.variables = []
        for r in range(self.n_row):
            for c in range(self.n_col):
                if self.Cell[r][c].type == "variable":
                    self.variables.append(variable(r, c))
        self.constraints = []
        # 2 fill the constraints
        for r in range(self.n_row):
            for c in range(self.n_col):
                if self.Cell[r][c].type == "constraints":
                    if self.Cell[r][c].topright != 0:
                        # look right
                        rightConstr = []
                        for i in range(1, self.n_col - c):
                            if self.Cell[r][c+i].type == "variable":
                                rightConstr.append(c+i)
                            else:
                                break
                        if rightConstr:
                            variables = []
                            for col2 in rightConstr: 
                                for var in self.variables:
                                    if (var.r == r and var.c == col2):
                                        variables.append(var)
                            constr = constrain(self.Cell[r][c].topright, variables)
                            self.constraints.append(constr)
                            for var in variables:
                                    var.constrain.append(constr)
                    # bottown constraints
                    if self.Cell[r][c].bottomleft != 0:
                        # look down
                        downConstr = []
                        for i in range(1, self.n_row - r):
                            if self.Cell[r + i][c].type == "variable":
                                downConstr.append(r + i)
                            else:
                                break
                        if downConstr:
                            variables = []
                            for row2 in downConstr: 
                                for var in self.variables:
                                    if (var.r == row2 and var.c == c):
                                        variables.append(var)
                            constr = constrain(self.Cell[r][c].bottomleft, variables)
                            self.constraints.append(constr)
                            for var in variables:
                                    var.constrain.append(constr)

    
    def nodeConsistency(self):
        # very easy. For each constraints remove from the variables' domain value which can't be solution
        # aka variable has to be lower than the constraints value
        for constrain in self.constraints:
            if constrain.sum < 10:
                for var in constrain.variables:
                    topp = var.domain[-1]
                    if topp >= constrain.sum:
                        for x in range(constrain.sum, topp + 1):
                            var.domain.remove(x)

    # the most important function for the solver.
    # It find the value in the domain that satisfy the constrain
    def GeneralArchConsistency(self):
        queue = [None]*len(self.constraints)
        queue[:] = self.constraints[:]
        while queue:
            constrain = queue[0]
            for index, variable in enumerate(constrain.variables):
                toremove = []
                for D in variable.domain:
                    if not (findSolutionPossibleSolution(constrain, D, index)):
                        toremove.append(D)
                        for constr in  variable.constrain:
                            if constr != constrain and (not (constr in queue)):
                                queue.append(constr)
                for rm in toremove:
                    variable.domain.remove(rm)
                if not variable.domain:
                    print("Problem without solutions. \n")
                    print("Variable at row: %d column: %d has no solution"%(variable.r, variable.c))
                    sys.exit()

            queue.pop(0)   

    def solve(self):
        for row in range(self.n_row):
            for col in range(self.n_col):
                if self.Cell[row][col].type == "variable":
                    self.Cell[row][col].value = self.findValue(row, col)
        self.print()
    
    def findValue(self, row, colomn):
        for var in self.variables:
            if var.c == colomn and var.r == row:
                if len(var.domain)>1:
                    print("PROBLEM! it doesn't exists a unique solution")
                    sys.exit()
                var.value = var.domain[0]
                return var.value


def findSolutionPossibleSolution(constrain, D, index):
    domains = []
    used = [D]
    for i in range(len(constrain.variables)):
        if i != index:
            domains.append(constrain.variables[i].domain)
    summ = constrain.sum - D
    if findSolution(summ, domains, used):
        return True
    return False

# function that search a solution in the array using different numbers
# function that search a solution in the array using different numbers
def findSolution(summ, domains, used):
    if summ < 0:
        return False
    if len(domains) == 1:
        #print(domains)
        #search the solution
        if summ in used:
            return False
        if summ in domains[0]:
            return True
        return False
    #print(used)
    for d in domains[0]:
        u = used[:]
        u.append(d)
        #print(d)
        #print("d = %d and it is %d that it is not in used" %(d, not(d in used)), used)
        if not(d in used):
            if findSolution(summ - d, domains[1:], u):
                return True
    return False
            



