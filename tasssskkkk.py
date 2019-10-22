list=list(range(1,99))
print(list)
def timee(function):
    import time
    def wrapper(*args):
        
        start_time = time.perf_counter() 
        res = function(*args) 
        print("%s seconds " % (time.perf_counter() - start_time))
        return res
    return wrapper


@timee
def sumFor(list):
    sum = 0 
    for i in list: 
        sum += i 
    #print(sum)
    return sum

@timee
def sumWhile(list): 
    sum = 0 
    length = len(list) 
    while length: 
        length -= 1 
        sum += list[length] 
    return sum

@timee
def sumRecursive(list):
    def f(*args):
        if len(list) == 0:
            return 0
        else:
            return list.pop() + f(list)
    return f(list)
    
#print(sumFor(list))
#print(sumWhile(list))
#print(sumRecursive(list))

print(sumFor(list)) 
print(sumWhile(list)) 
print(sumRecursive(list))
