```
Create a class to represent a person. The class should store first name, last name, date of birth, and
nationality. You then can create an instance of the person class by writing Person("Alan", "Turing", 23, 06, 1912, "UK"). Equip the class with string representation and equality checking.
Ask a user about the relevant fields using input and print the data that you have read.
Add a method that computes the age (in years) of the person. Use import datetime and today =
datetime.date.today() to get today’s date and access year, month, and day as today.year, today.month, and today.day.
Create a CSV file with columns name, date of birth, and country. The date of birth should be written in the format day.month.year. The file could look like this:
  1 name,date of birth,country
  2 Alan Turing,23.06.1912,UK
  3 John von Neumann,28.12.1903,HU
  4 David Hilbert,23.01.1862,DE
Add a few entries to this file, e.g. relatives or fictional characters.
Write code that reads all persons from persons.csv and groups them into a list. Find the oldest person and print their name.
Write Person as a @dataclass and perform the reverse of the previous part: Given several Person objects, write out a person.csv that contains the given data.


import pathlib
import csv
import datetime
import dataclasses

@dataclasses.dataclass
class Person:
  first_name: str
  last_name: str
  day: int
  month: int
  year: int
  country: str

  def age(self):
    t = datetime.date.today()
    years = t.year - self.year
    if self.month < t.month or (self.month == t.month and self.day < t.day):
      return years
    return years + 1

def main():
  persons = []
  with pathlib.Path("persons.csv").open("rt") as f:
    r = csv.reader(f)
    next(r)
    for row in r:
      name, date, country = row
      first, last = name.split(maxsplit=1)
      day, month, year = (int(x) for x in date.split("."))
      persons.append(Person(first, last, day, month, year, country))

  oldest = max(persons, key=Person.age)
  print(f"Oldest: {oldest.first_name} {oldest.last_name} (born {oldest.age()} years ago)")

  with pathlib.Path("persons_out.csv").open("wt") as f:
    w = csv.writer(f)
    w.writerow(["name", "date of birth", "country"])
    for p in persons:
      w.writerow(
        [
          f"{p.first_name} {p.last_name}",
          f"{p.day:02d}.{p.month:02d}.{p.year:04d}",
          p.country,
        ]
      )

if __name__ == "__main__":
  main()



  
