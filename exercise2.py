def check_fibonacci(num):
  fib = [0, 1]
  while fib[-1] < num:
    fib.append(fib[-1] + fib[-2])
    if num in fib:
      return f"{num} faz parte da sequência de Fibonacci."
    else:
      return f"{num} não faz parte da sequência de Fibonacci."

num = int(input("Informe o número: "))

result = check_fibonacci(num)
print(result)

print("Sequência de Fibonacci gerada: ")
fib = [0, 1]
while fib[-1] < num:
  fib.append(fib[-1] + fib[-2])

print(fib)
