import re

s = """The Rain in Spain
The Rain in Spain"""
search_patern = r"The.*Spain$"
x = re.findall(search_patern, s, re.MULTILINE)
print(x)