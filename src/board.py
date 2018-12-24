import random
import csv

class square():
    def __init__(self, typesquare = "variable", topright = 0, bottomleft = 0):
        self.type = typesquare
        self.value = 0
        self.topright = topright
        self.bottomleft = bottomleft
        self.domain = [1,2,3,4,5,6,7,8,9]

class variable():
    def __init__(self, r , c):
        self.constrain = []
        self.c = c
        self.r = r
        self.value = 0
        self.domain = [1,2,3,4,5,6,7,8,9]

class constrain():
    def __init__(self, summ, variables):
        self.variables = variables
        self.sum = summ
    
# types are "variable", "tofill", "constraints".
# variable can have value from 1 to 9, tofill can't have constraints
class board():
    def __init__(self, n_row = 12, n_col = 12, load = False, name = ""):
        if not load:
            self.n_row = n_row
            self.n_col = n_col
            print("not loaded")
            self.square = [[square() for row in range(n_col) ]for col in range(n_row)]
        else:
            self.load(name)
        

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
                            if self.square[row][col].value == 0 or i == 2:
                                print("|    |", end = "")
                            else:
                                print("|  %d |" % self.square[row][col].value, end = "")
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
                            if self.square[row][col].value == 0 or i == 2:
                                print("    |", end = "")
                            else:
                                print("  %d |" % self.square[row][col].value, end = "")
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
                self.square[r][int(c)].topright = int(toprightvalue.split()[0]) 
        print("Now tell the constraints coordinate in the top bottom-left (later their value will be asked)")
        for r in range(self.n_row): 
            inp = input("Row number %d write the coumn nubers which are targhet for the row:" %r).split()
            for c in inp:
                toprightvalue = input("The value")
                self.square[r][int(c)].type = "constraints" 
                self.square[r][int(c)].bottomleft = int(toprightvalue.split()[0]) 
    
    def save(self, name):
        table = [[self.encode(r, c) for c in range(self.n_col)] for r in range(self.n_row)]
        writer = csv.writer(open(name+".csv", 'w'))
        for results in table:
            writer.writerow(results)
        
    def encode(self, r, c):
        if self.square[r][c].type == "variable":
            return 0
        if self.square[r][c].type == "fill":
            return -1
        else:
            return (int(self.square[r][c].bottomleft)*100) + int(self.square[r][c].topright)

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
        self.square = [[square() for row in range(self.n_col) ]for col in range(self.n_row)]
        for r in range(self.n_row):
            for c in range(self.n_col):
                decoded = self.decode(table[r][c])
                self.square[r][c].type = decoded[0] 
                self.square[r][c].topright = int(decoded[1])
                self.square[r][c].bottomleft = int(decoded[2])
    
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
                        '''
                        upConstr = []
                        for i in range(1, r + 1):
                            if self.square[r - i][c].type == "variable":
                                upConstr.append(r - i)
                            else:
                                break
                        if upConstr:
                            variables = []
                            for row2 in upConstr: 
                                for var in self.variables:
                                    if (var.r == row2 and var.c == c):
                                        variables.append(var)
                            constr = constrain(self.square[r][c].topright, variables)
                            self.constraints.append(constr)
                            for var in variables:
                                    var.constrain.append(constr)
                        '''
                        # look right
                        rightConstr = []
                        for i in range(1, self.n_col - c):
                            if self.square[r][c+i].type == "variable":
                                rightConstr.append(c+i)
                            else:
                                break
                        if rightConstr:
                            variables = []
                            for col2 in rightConstr: 
                                for var in self.variables:
                                    if (var.r == r and var.c == col2):
                                        variables.append(var)
                            constr = constrain(self.square[r][c].topright, variables)
                            self.constraints.append(constr)
                            for var in variables:
                                    var.constrain.append(constr)
                    # bottown constraints
                    if self.square[r][c].bottomleft != 0:
                        # look down
                        downConstr = []
                        for i in range(1, self.n_row - r):
                            if self.square[r + i][c].type == "variable":
                                downConstr.append(r + i)
                            else:
                                break
                        if downConstr:
                            variables = []
                            for row2 in downConstr: 
                                for var in self.variables:
                                    if (var.r == row2 and var.c == c):
                                        variables.append(var)
                            constr = constrain(self.square[r][c].bottomleft, variables)
                            self.constraints.append(constr)
                            for var in variables:
                                    var.constrain.append(constr)
                        # look left
                        '''
                        leftConstr = []
                        for i in range(1, c + 1):
                            if self.square[r][c-i].type == "variable":
                                leftConstr.append(c-i)
                            else:
                                break
                        if leftConstr:
                            variables = []
                            for col2 in leftConstr: 
                                for var in self.variables:
                                    if (var.r == r and var.c == col2):
                                        variables.append(var)
                            constr = constrain(self.square[r][c].bottomleft, variables)
                            self.constraints.append(constr)
                            for var in variables:
                                    var.constrain.append(constr)
                        '''
    
    def nodeConsistency(self):
        # very easy. For each constraints remove from his domain variables which can't be solution
        # aka variable has to be lower than the constraints value
        for constrain in self.constraints:
            if constrain.sum < 10:
                for var in constrain.variables:
                    topp = var.domain[-1]
                    if topp >= constrain.sum:
                        for x in range(constrain.sum, topp + 1):
                            var.domain.remove(x)

    '''
    def ArchConcistency(self):
        for constrain in self.constraints:
            for index, variable in enumerate(constrain.variables):
                for D in variable.domain:
    '''
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
                    return False

            queue.pop(0)   

    def solve(self):
        for row in range(self.n_row):
            for col in range(self.n_col):
                if self.square[row][col].type == "variable":
                    self.square[row][col].value = self.findValue(row, col)
        self.print()
    
    def findValue(self, row, colomn):
        for var in self.variables:
            if var.c == colomn and var.r == row:
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
            



