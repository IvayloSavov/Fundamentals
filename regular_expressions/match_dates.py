import re

text = input()
pattern = r'(\d{2})([/\.-])([A-Z][a-z]{2})\2(\d{4})'
# всяка отделна скоба е една група и с \2 ревефираме към групата със символите и когато реферираме към някоя група, трябва да е затворена

for match in re.findall(pattern, text):
    day, _, month, year = match
    print(f'Day: {day}, Month: {month}, Year: {year}')