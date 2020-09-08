start = int(input())
stop = int(input())
string = ""

for index in range(start, stop+1):
    char = chr(index)
    string += f"{char} "

print(string)