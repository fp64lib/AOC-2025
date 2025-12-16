# AOC 2025-10b
# least number of button flips
test=0
debug=0
day="10b"

from math import ceil
from scipy.optimize import linprog
from numpy import transpose
#from aoc import *

filename = "AOC-2025-" + day[:len(day)-1]
if test:
    filename += "-test"
filename += ".txt"
print( day, filename )

total = 0

def makeColumn(button, n):
    # create an indicator column for A_eq matrix
    # with 1s where the button influences the joltage
    vector = [0] * n
    for b in button: 
        vector[b] = 1 
    return vector

def solve( buttons, joltages ):
    numButtons = len(buttons)
    numJolt = len(joltages)
    
    # see comment at end of file for explanation
    c = [1] * numButtons
    b_eq = joltages 
    A_eq = [makeColumn(button, numJolt) for button in buttons]
    A_eq = transpose(A_eq)
    if debug > 1:
        print( "c", c, "b_eq", b_eq )
        print( "A_eq^T\n", A_eq )
    res = linprog( c, A_eq=A_eq, b_eq=b_eq, integrality=c )
    if debug > 1:
        print( "res:", res )
    count = ceil(res.fun)

    return count

with open( filename, "r" ) as file:
    for line in file:
        # lights can be ignored for part 2

        # parse buttons
        if debug:
            print( line )
        parts = line.split()
        if debug > 1:
            print( parts )
        buttons =[]
        for p in parts[1:-1]:
            b = list(map( int, p.strip("()").split(",") ))
            if debug > 1:
                print( b )
            buttons.append( b )

        # parse joltages
        joltages = list(map( int, parts[-1].strip("{}").split(",") ))
        if debug > 1:
            print( joltages )
            
        count = solve( buttons, joltages )
        total += count
        print( total, count )
        
print( day, "Answer is", total )

# from https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html
# scipy.optimize.linprog
# linprog(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=(0, None), [...], integrality=None)
# minimize
#           c @ x
# such that
#           A_ub @ x <= b_ub
#           A_eq @ x == b_eq
#           lb <= x <= ub
# Note that by default lb = 0 and ub = None. Other bounds can be specified with bounds
# Parameters:	
# c     1-D array
#       The coefficients of the linear objective function to be minimized.
# A_ub  2-D array, optional
#       The inequality constraint matrix. Each row of A_ub specifies the coefficients of a linear inequality constraint on x.
# b_ub  1-D array, optional
#       The inequality constraint vector. Each element represents an upper bound on the corresponding value of A_ub @ x.
# A_eq  2-D array, optional
#       The equality constraint matrix. Each row of A_eq specifies the coefficients of a linear equality constraint on x.
# b_eq  1-D array, optional
#       The equality constraint vector. Each element of A_eq @ x must equal the corresponding element of b_eq.
# bounds sequence, optional
#        (min, max) pairs for each element in x, defining the bounds on that parameter. Use None for one of min or max when there is no bound in that direction. By default bounds are (0, None) (non-negative) If a sequence containing a single tuple is provided, then min and max will be applied to all variables in the problem.
# integrality 1-D array or int, optional
#       Indicates the type of integrality constraint on each decision variable.
#       0 : Continuous variable; no integrality constraint.
#       1 : Integer variable; decision variable must be an integer within bounds.
# Returns:
# res   OptimizeResult
#       A scipy.optimize.OptimizeResult consisting of the fields below. Note that the return types of the fields may depend on whether the optimization was successful, therefore it is recommended to check OptimizeResult.status before relying on the other fields:
#       x   1-D array
#           The values of the decision variables that minimizes the objective function while satisfying the constraints.
#       fun float
#           The optimal value of the objective function c @ x.
#
# For our problem:
# c         our button presses
# A_ub      not used
# b_ub      not used
# A_eq      our matrix, where each column represents one button, and each column represents a light/joltage application, being 1 when the button changes modifies that light/joltage
#           IMPORTANT: A must be transposed to match dimensions
# b_eq      our target joltage values
# bounds    not used
# integrality list of 1s, as we only can press a button completely or not

