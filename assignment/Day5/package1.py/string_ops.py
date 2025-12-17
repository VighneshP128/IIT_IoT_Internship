
def reverse(s):
 return s[::-1]

def count(s):
   vowels="aeiou"
   count=0
   for char in s:
     if char in vowels:
       count+=1
   return count