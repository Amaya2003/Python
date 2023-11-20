# understand loop and iteration variable 

# for Repeating steps or a set of code we use loops
n=5
while n>0:
    print(n)
    n=n-1
print("Loop exited")
print(n) 

#zero trip loop, in this case the condition of the loop is not satisfied hence the set of code in the loop is not executed 
n=5
while n<5:
    print(n)
    n=n-1
print("Loop exited")
print(n) # value of n will remain same since we havent entered the loop.

#infinity loop ie there is no iterative variable hence we cannot exit the loop due to condition will not be false in any iteration.

#n=5
#while n>0: #to execute infinite loop remove # symboll for whole while loop.
    #print("Hello","Dear") #since we do not have a iteration variable hence it will not false the condition mentioned therefore this loop will execute infinte times.
    #print("Pyton")
#print("Loop exited")
#print(n)

#use of break statement in loops to exit the loops
n=5
while n>0:
    print(n)
    n=n-1
    if n == 2: #loop will iterate till 3 and then "if" condition will be satisfied and loop will be exited due to "break " statement
        break

print("Loop exited")
print(n)

# using continue statement to skip a particular iteration.
n=5
while n>0:
    print(n)
    n=n-1
    if n==3:
        n=n-1
       # continue # due to this we will skip the iteration for n=3
print("Loop exited 1")
print(n)
