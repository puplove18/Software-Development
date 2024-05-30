```
Use the Monte-Carlo method to estimate the number fi.
One variant is as follows. Fix a square of size d and a circle inside it with diameter d. Now, randomly
generate points in the square. The number of points inside the circle vs. the total count corresponds to
the ratio of areas of square and circle. From this, you can derive fi.
```

import random
t, c = 100000, 0
for _ in range(t):
  x = random.ramdom()
  y = random.random()
  if x * x + y * y <= 1:
    c += 1
print (c / t * 4)
