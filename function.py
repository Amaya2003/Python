# create user defined function in python.
def function (): # to define a user defined function we use "def" keyword.
    print("Hello to python bootcamp")
    print("fees for the course is: ")

function () # this is used to revoke the function or to call function defined by user . 
print(1000)
function () # we can call same function multiple times.

# defining functions and passing parameters and receiving arguments.
def fun_arg(x): #parameters are received as an arguments. 
    print(x+1)

fun_arg(10) #we pass parameter to the functions, and we called the function to be executed.
 
# using multiple parameters and arguments:
def fun_multi(x,y):
    print(x+y)

fun_multi(10,20)

# functions above are all with no return statement now let us define function returning some value:
def func_return(x,y):
    x=x+y
    return x
i=func_return(10,20) # i will store the value retured by the function ie x+y.
print(i)