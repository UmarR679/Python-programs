s = input("Enter a string: ")
freq={}
for char in s:
    if char not in freq:
        freq[char]=1
    else:
        freq[char]+=1
m=max(freq.values())
for i in freq:
    if freq[i]==m:
        print(i)
