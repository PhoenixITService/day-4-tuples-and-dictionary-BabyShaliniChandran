data = [
    ('A', 1, 2),
    ('B', 3),
    ('C', 4, 5, 6),
    ('D',),
    ('E', 7, 8)
]
length = list(map(len, data))
first_element = list(zip(*data))[0]
sorted=sorted(zip(length, first_element))
length,first_element=zip(*sorted)
result=list(first_element)
print(result)