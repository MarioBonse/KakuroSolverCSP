# KakuroSolverCSP
Solver of the japanese game kakuro viewed as CSP problem.
You can write your problem, using the file createBoard.py.
For the game rules of the game you can see <a href = "https://en.wikipedia.org/wiki/Kakuro">the wiki page on Kakuro</a>.
## Algorithm
The algorithm exceed the rules that the sum over a row must equal to the value on the left and the sum over a column must be equal to the value on the bottom of the cells with the diagonal and one or two numbers. The numbers on each rows and columns has also to be unique.
The solution it's also unique.
This is an example of a problem:
<div>
  <img src="https://github.com/MarioBonse/KakuroSolverCSP/blob/master/images/kakuroUnsolved.png" width="320" height="400" />
  </div>
In order to find the numbers that solves the problem we will works in three steps:  

1) The board expressed as a matrix is translated to another structure (an hypergraph). It represents the empty cells as  "variables type" with a domain which is originally [1,2,3,4,5,6,7,8,9] (aka range(1,10)). They are the nodes of the hypergraph. Then there is another object, the constraints, which are a lists of variables with a number that is the sum that the variables have to reach. It's like the hyper-arch of the hypergraph. The constain ha also an implicit rule, that the variables have to be different on each constrain.  

2) Reduce the domains of the variables with the "Node consistency" technique. A variable can't be higher or equal to the sum that has to reach so we can delete the elements in the domains which are greater than the sum.  

3) Reduce the domain again (now we will arrive with just one element for each domain, and this is the result).
We make a structure made of constraints. For each of them we will try to find if fo each variables in the constraints each element in the variable's domain has a solution with other element from the domains of the other variables of the same constraint. If the solution doesn't exists we will delete the element from the domain and add again in the structure all the constraints that the variable has. It's seems a messy but it isn't.

## Result
This is the result of the game showed before:
<div>
  <img src="https://github.com/MarioBonse/KakuroSolverCSP/blob/master/images/kakuroSolved.png" width="320" height="400" />
  </div>
It solves also much bigger puzzles as:
<div>
  <img src="https://github.com/MarioBonse/KakuroSolverCSP/blob/master/images/kakuro30x30.png" width="320" height="400" />
  </div>

## How to run it
It's very very simple. There are not dependencies, you just need python3.
Then go to src directory and add your kakuro puzzle with the command
```
cd src
python3 createBoard.py
```
Then solve it with the command 
```
python3 main.py
```
and it runs the default example.
You can run the example you have entered with 
```
python3 main.py <examplename>
```
That's all

## Author
* **Mario Bonsembiante** :nerd_face: - [MarioBonse](https://github.com/MarioBonse)
