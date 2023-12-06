# Recursion calls the same functions within itself, creating a call stack (FILO)
def callstack_model(value):
    call_stack = []
    while value > 0:
        call_stack.append({"input": value})
        print("Call Stack: ", call_stack)
        value -= 1
    print("------ Base case reached ------")
    while len(call_stack) != 0:
        print("Popping {} from call stack".format(call_stack.pop()))
        print("Call stack: ", call_stack)

# callstack_model(4)
#############################################################################
# Nth Fibonacci Sequence 

def fibonacci_iterative(n):
    a = 0
    b = 1
    if n < 0: print("Incorrect Input")
    elif n == 0: return a
    elif n == 1: return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b


def fibonacci_recursive(n):
  if n <= 1:
    return n
  else:
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
  
# print(fibonacci_iterative(9))
# print(fibonacci_recursive(9))