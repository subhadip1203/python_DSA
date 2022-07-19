def findSum(num):
  # give condition to solve infinite condition
  if num == 1:
    return 1

  result = num + findSum(num-1)
  
  # always return 
  # mostly at the end of the function
  return result


print(findSum(5))