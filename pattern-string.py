import re

text = 'To jest przykład tekstu do wyszukania wzorca'
pattern='wzorca'

matches = re.finditer(pattern,text)

for match in matches:
    print(match)