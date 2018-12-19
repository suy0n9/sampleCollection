
def min_max(x):
    return [(i - min(x)) / (max(x) - min(x)) for i in x]


def normalize(x):
    return [float(i) / max(x) for i in x]


# import random
# random_l = [random.randint(0, 100) for i in range(9)]
# random_l.sort()
random_l = [0, 31, 41, 59, 68, 71, 75, 77, 79]

print(random_l)
print(min_max(random_l))
print(normalize(random_l))
