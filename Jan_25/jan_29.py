def twoSum(nums, target):
    seen = {}

    for i in range(len(nums)):
        remaining = target - nums[i]

        if remaining in seen:
            return [seen[remaining], i]

        seen[nums[i]] = i
        
def isValid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)

    return not stack
