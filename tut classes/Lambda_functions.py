# Lambda functions are lightweight functions performing onr specific task.
#syntax is
# x = lambda var_name: a + b

x = lambda a,b : a + b
print(x(4,6))

def add(x,y):
    return x + y

times_two = lambda func: 2 * func

print(times_two(add(5,8)))