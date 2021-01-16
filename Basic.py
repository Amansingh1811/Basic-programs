"""a = input("enter number")
if int(a) >= 10:
    print("young")
elif a<0:
    print("wrong input")
else:
    print("kid")"""

nums = [10, 23, 66, 11, 8, 11, 12, 33, 2]
output = 0
for num in nums:
    if num % 2 == 0:
        output =+ num
print(output)