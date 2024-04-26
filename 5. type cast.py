x: int = 1
y: float = 2.0
z: str = "3"

print(x, y, z)
print(type(x), type(y), type(z))
print(x, int(y), int(z))
print(3*z)
y = int(y)
z: int = int(z)
print(type(x), type(y), type(z))
print(3*z)

nums = [x, y, z]
nums = [float(num) for num in nums]
print(nums)
