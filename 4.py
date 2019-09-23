result = 1

for i in range(100, 1000):
    for j in range(100, 1000):
        multiply = i * j
        if str(multiply) == str(multiply)[::-1]:
            if multiply > result:
                result = multiply

print(result)


