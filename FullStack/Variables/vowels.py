s1 = input()
s2 = input()
vowels = ['a', 'e', 'i', 'o', 'u']

s1 = s1.lower()
allVowels = set("aeiou")

for char in s1 :
    if char in allVowels :
        allVowels.remove(char)

if len(allVowels) == 0:
    print("YES")
else :
    print("NO")

    s2 = s2.lower()
allVowels = set("aeiou")

for char in s2 :
    if char in allVowels :
        allVowels.remove(char)

if len(allVowels) == 0:
    print("YES")
else :
    print("NO")