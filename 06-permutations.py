def permute2( nums, values=[]):
    if not nums:
        return [values]
    result = []
    for i in range(len(nums)):
        result += permute2(nums[:i] + nums[i + 1:], values + [nums[i]])
    return result
def permute2Iterative(nums):
    results = []
    stack = [(nums, [])]
    print(stack)
    while len(stack):
      nums, values = stack.pop()
      print(stack)
      if not nums:
        print(values)
        results += [values]
      for i in range(len(nums)):

        stack.append((nums[:i]+nums[i+1:], values+[nums[i]]))
        print(stack)
    return results

res=permute2Iterative([1,2,3])
for i in res:
    print(i)