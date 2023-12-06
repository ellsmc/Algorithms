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
        
callstack_model(4)