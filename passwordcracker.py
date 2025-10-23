import time

password = input("Enter your password: ")
start = time.time()
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
guess = []
for val in range(5):
    a = [i for i in chars]
    for y in range(val):
        a = [x + i for i in chars for x in a]
    guess = guess + a
    if password in guess:
        break
end = time.time()
clock = str(end - start)

print(f"Your password : {password}")
print(f"Time taken : {clock}")