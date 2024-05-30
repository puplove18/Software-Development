```
Before we explore real data, let us start with the basics of reading CSV data. Download the grades.csv
from Moodle (it is taken from https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html, which
lists several other files). Open it with a text editor and try to understand what this data set contains.
Open the file for reading (with xy.open(...) as f:) and load it using CSV (csv.reader(f)). Let your
program print every row.
Now, complete the following exercises:
  • Determine the average over the final scores.
  • Print the names of all students which achieved more than 60% in the fourth test.
  • For each student that achieved a B- or better, print their name together with their scores over all
  tests and the final exam.
In the second part, we want to create a new file. Recall how to open a file for reading and how to print
rows using the CSV module.
Then, print a file containing the columns “Name”, consisting of the first and last name of each student,
“Average”, the average score over all tests, and “Best”, the test in which the student performed best.
Verify your results by inspecting the file.
```


from pathlib import Path
import csv

with Path("grades.csv").open("rt") as f:
  students = list(csv.DictReader(f))

final_scores = [float(s["Final"]) for s in students]
print(f"Average: {sum(final_scores) / len(final_scores)}")

better_than_60 = [s for s in students if float(s["Test4"]) > 60]
print(f"Better than 60%: {', '.join(s['Firstname'] + ' ' + s['Lastname'] for s in students)}")
print()  

def is_better_b(grade):
  return grade in {"A+", "A", "A-", "B+", "B", "B-"}
  
tests = [f"Test{i}" for i in range(1, 5)]

print("B- or better:")
for s in students:
  if not is_better_b(s["Grade"]):
    continue
  print(f" {s['Firstname']} {s['Lastname']}: {' '.join(s[t] for t in tests)} {s['Final']}")

with Path("out.csv").open("wt") as f:
  writer = csv.writer(f)
  writer.writerow(["Name", "Average", "Best"])
  for s in students:
    average = sum(float(s[t]) for t in tests) / len(tests)
    best = max(tests, key=s.__getitem__)
    writer.writerow([f"{s['Firstname']} {s['Lastname']}", average, best])




