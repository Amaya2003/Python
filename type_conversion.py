# to check for the type of the data/value allocated
i=42
print(type(i))

#to conver integer to float
i= float(99)/100 # converts 99 (integer value) to float value
print(i)
print(type(i))

# float to integer
i=int(0.99) # converts 0.99 (float value ) to integer value
i=i*100
print(i)
print(type(i))

# lets see what happens if we dont convert 0.99 to integer 
i=0.99/100
i=i*100
print(i)
print(type(i)) # we can observe that output is still in float data type. 

# Terefore to convert the data type ie from integer to float or vice versa we use concept of type casting.

#example
i=(1+2* float(3)/4-5)
print(i)
print(type(i))

# converting string datatypr to integer:

s='123'
print(s)
print(type(s))
# print(s+1) : here this will not work since s is string datatype and 1 is integer, we have to convert s to integer datatype.
i=int(s)
print(i)
print(type(i))

#converting string to integer datatype:

integer=321
print(integer)
print(type(integer))
string=str(integer)
print(string)
print(type(string))

# NOTE: we cn only convert string if it consists integers in it or else it will show traceback.
 