import random
import time

time.sleep(2)

print("Pick a number from 1 to 10")

response = input()

print("Let's see...")

print(random.randrange(1, 10))
if response == (random.randrange(1, 10)):
    print(".")
elif response == random:
    print(".")

print("I'll make it more simple, Pick a number from 1 to 5")

response2 = input()

print(random.randrange(1, 5))
if response2 == (random.randrange(1, 5)):
    print(".")
elif response2 == random:
    print(".")

print("1 last time, pick a number")
print("       1 or 2")

response3 = input()

print(random.randrange(1, 3))
if response3 == random.randrange(1, 2):
    print(".")
elif response3 == random:
    print(".")
