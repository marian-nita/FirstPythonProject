myCats = []

while True:
    print("Print the name of the cat " + str(len(myCats) + 1) + " (or enter nothing to stop): ")
    name = input()
    if name == '':
        break
    myCats += [name]

print("The name of the cats are: ")
for cat in myCats:
    print(" " + cat)

check = input("Enter a name of the cat: ")
if check in myCats:
    print(check + " is one of my cats.")
else:
    print(check + " is not my cat.")