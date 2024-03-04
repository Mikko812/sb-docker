#  Return N Fibonachi numbers
def get_fib_numbers(qty):
    result = [0, 1]
    for i in range(2, qty):
        result.append(result[i-2] + result[i-1])
    return result

n = int(input('Введите количество чисел Фибоначчи:'))
fib_numbers = get_fib_numbers(n)
print(f'{n} первых чисел Фибоначчи:\n{fib_numbers}')