## pyste

An unofficial API for pastebin.

```python

from pyste import user

user = user()
user.auth()

user.paste('hello', 'hello world!') # returns the id of your paste

  
