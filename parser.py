import textile
with open("README.textile", "r") as file:
    cont = file.read()
    c = textile.textile(cont)
    print(c)