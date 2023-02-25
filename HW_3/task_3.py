friends = ["John", "Marta", "James"]
enemies = ["John", "Johnatan", "Artur"]
for person in friends:
    if person == "James":
        continue #He is the best friend
    elif person in friends and person not in enemies:
        print(f"{person} we are the best friends")
    elif person in enemies:
        print(f"{person} we are not friends anymore")
