import re

s = "The Rain in Spain"
search_patern = r"The.*Spain$"
x = re.search(search_patern, s)
print(x)