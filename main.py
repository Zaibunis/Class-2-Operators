print("\n==Arithmetic Operators==")

print("Addition")
print(f"111+3444={111+3444}")
print("Subtraction")
print(f"111+3444={111-3444}")
print("Multiplication")
print(f"111+3444={111*3444}")
print("Division")
print(f"111+3444={111/3444}")
print("Exponentiation")
print(f"2**5={2**5}")
print("Modulus")
print(f"2%5={2%5}")
print("Floor Division")
print(f"3//6={3//6}")

print("\n=== Assignment Operators ===")

x = 6
print(f"Initial value of x: {x}")
x +=7
print(f"After x += 7: {x}")
x -=8
print(f"After x -= 8: {x}")
x *=6
print(f"After x *= 6: {x}")
x /=9
print(f"After x /= 9: {x}")
x %=9
print(f"After x %= 9: {x}")
x **=9
print(f"After x **= 9: {x}")
x //=9
print(f"After x //= 9: {x}")

print("\n===Comparison Operators ===")

print(f"Is 4 equal to 5? {4 == 5}")
print(f"Is 3 greater than 5? {3 > 5}")
print(f"Is 2 less than 5? {2 < 5}")
print(f"Is 1 less than or equal to 5? {1 <= 5}")
print(f"Is 0 greater than or equal to 5? {0 >= 5}")
print(f"Is 9 not equal to 5? {9 != 5}")
print(f"Is 8 equal to 5? {8 == 5}")

print("\n===Logical Operators ===")

a , b = True , False
print(f"{a} , {b}")
print(f"{a and b}")
print(f"{a or b}")
print(f"{not a}")
print(f"{not b}")

print("\n===Identity Operators ===")

grocery = ["bread","milk","butter"]
RamadanGrocery = ["bread","milk","butter"]
DailyNeed = grocery

print(f"grocery is DailyNeed: {grocery is DailyNeed}")
print(f"grocery is RamadanGrocery: {grocery is RamadanGrocery}")

print("\n===Membership Operators ===")

DressCollection = ["Shirt","T-shirt","Jeans","Skirt","Dress"]

print(f"DressCollection = {DressCollection}")
print(f"Is 'Shirt' in DressCollection? {'Shirt' in DressCollection}")
print(f"frock in DressCollection? {'frock' in DressCollection}")
print(f"Is 'frock' not in DressCollection? {'frock' not in DressCollection}")

print("\n===Bitwise Operators ===")

a = 90  
b = 90  

print(f"a = {a} (binary: {bin(a)})")
print(f"b = {b} (binary: {bin(b)})")

# AND
print(f"a & b = {a & b} (binary: {bin(a & b)})")  # 12

# OR
print(f"a | b = {a | b} (binary: {bin(a | b)})")  # 61

# XOR
print(f"a ^ b = {a ^ b} (binary: {bin(a ^ b)})")  # 49

# NOT
print(f"~a = {~a} (binary: {bin(~a)})")  # -61

# Left Shift
print(f"a << 2 = {a << 2} (binary: {bin(a << 2)})")  # 240

# Right Shift
print(f"a >> 2 = {a >> 2} (binary: {bin(a >> 2)})")
