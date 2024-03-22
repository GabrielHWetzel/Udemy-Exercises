import random

l_bound = int(input("Enter the lower bound: "))
u_bound = int(input("Enter upper bound: "))
print(random.randint(l_bound, u_bound))

while True:
    input("Next")
    print(random.randint(1, 20))
