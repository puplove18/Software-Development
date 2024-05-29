```
In this exercise, we will analyse the content of webpages. Concretely, for now we simply want to know if
some text appears in a webpage. We will use a module to handle downloading the website data – you do
not need to understand how it works for now, we will learn about modules later. Start with this skeleton:

  import urllib.request
  def main():
    url = "https://google.com"
    req = urllib.request.urlopen(url)
    response = req.read().decode(errors='ignore')
    print(response)

  main()

This downloads and prints the HTML code of https://google.com. (If this looks weird to you, here is a
relevant xkcd comic: https://xkcd.com/1605/.) Try to see if this works for you.

  1. Now, modify the code so that the user can enter a URL and fetch this site instead. You don’t need
  to care about handling errors etc.
  2. Check that the URL starts with http:// or https://. If not, add it to the string.
  3. Move fetching the website data into a separate function, so that you can write something akin to
  content = download_data(url).
  4. Check if the website content contains the word div.
  Bonus: Count how often it appears using optional arguments of the find method.
  5. Modify the code so that the user can enter the URL and the string to search for.
  6. Modify the code again so that the user once enters a URL, and then can enter multiple strings,
  where your program every time responds whether the website contains that word (or how often).
```

import urllib.request

def fetch_data(url):
if not url.startswith("http://") and not url.startswith("https://"):
  url = "https://" + url
req = urllib.request.urlopen(url)
return req.read().decode(errors='ignore')

def main():
  url = imput("URL: ")
  data = fetch_data(url)
  while True:
    word = input("Word to search: ")
    if not word:
      break
    count = data.count(word)
    print(f"{word} appears {count} times in {url}")

main()












