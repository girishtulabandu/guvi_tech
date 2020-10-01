s1=input('ENTER STRING ONE')
s2=input('ENTER SECOND STRING')
l1=[ord(i) for i in s1]
l2=[ord(i) for i in s2]
if sum(l1)==sum(l2):
   print("Yes Anagram strings")
else:
   print("Strings are not anagram")
