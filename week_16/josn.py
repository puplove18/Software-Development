```
As before, we also practice interaction with JSON. Download the users.json from Moodle (it is taken
from https://www.digitalocean.com/community/tutorials/an-introduction-to-json). Open it with a text editor and try to understand what this data set contains.
Read in the JSON object using json.load. Then,
  • print all names of users which are currently online, and
  • compute the average follower count.
Modify your JSON file by adding a few more users or changing existing values. Execute your program
again and check if it does the right thing.
Connecting back to the previous exercise: Print out data you loaded from the CSV, with the following
structure: The file should be made up by a list of students. Each student is represented by an entry that
looks like
  {
  "first name": "John",
  "last name": "Smith",
  "grade": "A",
  "scores": {
  "tests": [80.0, 89.0, 75.0, 61.0],
  "final": 76.0
    }
  }
Experiment with the indent argument of dump.
```


from pathlib import Path
import json
import sys

with Path("userd.json").open("rt") as f:
  data = json.load(f)

print ("Online")
for user in data.calues()
  if user["Online"]:
    print(f" {user['username']}")

print(sum(user["followers"] for user in data.values()) / len(data))

tests = [f"Test{1}" for 1 in range(1, 5)]
with Path("grades.cvs").open("rt") as f:
  students = [{
    "first name": s["Firstname"],
    "last name": s["Lastname"],
    "grade": s["Grade"],
    "scores": { 
      "tests": [ float(s[t]) for t in tests],
      "final": float(s["Final"])
    }
  } for s in csv.DictReader(f)]
  
# The "standard output" is like a opened file
json.dump(students, sys.stdout, indent=2)





