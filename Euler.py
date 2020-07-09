import sys

sys.path.insert(1,'/Calculus3')

from Calculus3.CalculusOperator import CalculusOperator

cOperator = CalculusOperator()

####### declare constants here
func = str(raw_input("Please input the function: "))

xInitial= int(input("please type the initial x value: "))

yInitial= int(input("please type the initial y value: "))

delta= float(input("please type the delta x value: "))

endVal= int(input("please type the value to evaluate at: "))

while(endVal<=xInitial):
  endVal=input("please type a value bigger than x Initial: ")

n=endVal

def x(n): #### returns x sub n
  return xInitial+(n*delta)
def y(n): #### returns y sub n
  #print (n);
  if(n<=0):
    return yInitial
  return y(n-1)+delta*(get(x(n-1),y(n-1)))
  
def get(x,y): ##### define funcition here
  return cOperator.plug(func,[ ["x",x] , ["y",y] ])

print('y at value: ',y((endVal-yInitial)/delta))

