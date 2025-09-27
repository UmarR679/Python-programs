data = 578378923
s = str(abs(data))
from collections import Counter
cnt = Counter(s)
print(cnt)
repeats = sum(1 for v in cnt.values() if v>1)
if repeats>0:
    print(repeats)
else:
    print(-1)

