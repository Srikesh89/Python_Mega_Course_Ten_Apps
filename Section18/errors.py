#syntax errors
print(1)
int(9)
# int 9     #can't use number as variable AND int is a function
print(2)
# print 3    #missing paran

#runtime errors
a = 3
b = '2'
print(int(2.5))
print(a*b,sep='')
# print(a+b)    #TypeError
# print(c)        #NameError: c not defined
# print(3/0)      #ZeroDivisionError
 
def divide(a,b):
    try:
        return a/b
    except:
        return "unable to divide"

print(divide(2,2))
print(divide(2,0))