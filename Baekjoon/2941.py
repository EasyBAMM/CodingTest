_input = input()

redata = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for x in redata:
    _input = _input.replace(x, "?")

print(len(_input))
