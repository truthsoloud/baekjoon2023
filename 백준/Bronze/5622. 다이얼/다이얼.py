dial_list = list(str(input()))

nums = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

count = 0
for dial in dial_list:
    for i in range(len(nums)):
        if dial in nums[i]:
            count += (i+3)

print(count)