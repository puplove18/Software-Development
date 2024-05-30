```
We want to analyse production costs of an assembly line by investigating the parts required for the final prod-
uct. To this end, read lines of data from the input, each of which describe a kind of parts needed. Each line is
made up of several components, namely <part name> <part weight in kilos> <part count> <part
dimensions> <material name> <material cost per kilo> <order ID> <accounting number>. Each
component does not contain spaces, so you can split the line with split. Read from the input until you
get an empty line.
Example dataset:
  1 Bolt_M10 0.01 143 15x15x30 Steel 12.3 o1874_A IN_B_254_22
  2 Beam_Pine 3.2 2 200x20x20 Wood 3 o3512_C IN_W_244_24
  3 Screw_Wood_30 0.02 20 7x7x40 Steel 8.23 oS-543 SCREW_2225x2
  
Several such datasets are provided on Moodle. Have a look at them, get a feeling for how the data looks,
and try to make sense of it. (This mimics a real scenario where you are provided with an incomplete
description of the data you are supposed to work with.) See what the type of each part should be, whether
there are any corner cases you should think of, and try to parse the data.
Try to answer the following queries:
  • What is the total cost of all materials of the product?
  • What is the name of the largest part (by volume)?
  • Which parts are made of steel?
  • What is the most expensive part per volume?
  • Which parts cost more than 1000€ in total?
  • The data unfortunately is not in perfect shape. Identify all parts that are somehow “incomplete” /
  try to fix problems automatically if possible.
                                                                        
Hint: On Linux, you can python3 <your program> < data.txt to automatically “paste” the content of
data.txt into the standard input of your program. On other systems, simply copy-paste the content.
```

parts = []
while True:
  l = input()
  if not l:
    break
  name, weight, count, sim, mat, cost, order_id, accounting_id = l.split()
  dim = [int(d) for d in dim.split("x")]
  parts.append((name, float(weight), int(count), dim, mat, float(cost)))

def cost(part):
  return part[1] * part[5]
def volume(part):
  x, y, z = part[3]
  return z * y * z
def cost_by_volume(part):
  return cost(part) / volume(part

print("Total cost:", sum(cost(part) * part[2] for part in parts))
print("Largest volume:", max(parts, key=volume)[0])
print("Made of steel:", ", ".join(part[0] for part in parts if "steel" in part[4].lower()))
print("Most expensive:", max(parts, key=cost_by_volume))


