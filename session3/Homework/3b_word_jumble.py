words = ["instagram", "twitter", "weibo", "facebook"]
import random
rand_word = random.choice(words)
a = list(rand_word)
for i in range(len(a)):
    b = random.randint(0, len(a) - 1)
    a.append(a[b])
    a.pop(b)
print(a)
user = input("Your answer: ")
loop = True
while loop:
    if user == rand_word:
        print("Hura")
        loop = False
    else:
        print(":(")
        loop = True
        user = input("Your answer: ")