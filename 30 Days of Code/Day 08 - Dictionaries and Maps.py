n = int(input())
phone_book = {}
for _ in range(0, n):
    entry = str(input()).split(" ")
    phone_book[entry[0]] = int(entry[1])

for _ in range(0, n):
    name = str(input())

    if name in phone_book:
        phone = phone_book[name]
        print(name + "=" + str(phone))
    else:
        print("Not found")
