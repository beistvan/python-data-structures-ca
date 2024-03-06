memo = {}

def fibonacci(num):
  answer = None
  # Write your code here
  if num < 2:
    memo[num] = num
    return num
  if num in memo:
    return memo[num]
  else:
    answer = fibonacci(num - 1) + fibonacci(num - 2)
  memo[num] = answer
  return answer

# Test your code with calls here:
print(fibonacci(20))
print(fibonacci(200))
