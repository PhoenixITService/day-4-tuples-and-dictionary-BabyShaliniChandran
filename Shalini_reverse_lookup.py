scores = {
    "Anita": 92,
    "Ravi": 85,
    "Kiran": 76,
    "Zoya": 88
}
user_input=int(input("Enter score:"))
dict=dict(zip(scores.values(),scores.keys()))
print(dict.get(user_input,"Not found"))
