# 1.1 implemant a recursive function to caculate the factorial of a given number .


def fact_rec(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rec(n-1)

number = 4

rec = fact_rec(number)

print("the factorial of {} is {}".format(number,res))