# PasteIO

PasteIO is a simple API for using Pastebin as an anonymous guest. Follow the steps below
to get started.

---

### Getting Started

1. **Import the Pastebin client.**

2. **Create a client object.** You must specify the URL of the Pastebin server. In almost all
cases, this will be `'https://pastebin.com/'`. In some cases, you might want to point to an
alias, mirror site or proxy.

3. **Authorise the client with Pastebin**. The client needs some session cookies to upload
and download pastes from Pastebin. The `auth` method will return `True` or `False`
depending on whether the cookies were obtained or not.

4. When the client has been authorised, you can choose what to do next. For instance, you
may like to upload a new paste via the ```upload``` method.

```python
from pasteio import client

myclient = client('https://pastebin.com/')

myclient.auth()

myclient.upload('Hello', 'Hello, World! This is my new paste.')
```

---

### Methods

```client.upload(name, text)```

This uploads a new paste to Pastebin. If the upload was successfull, it will return the
"paste id" for the paste. Paste ids are unique identifiers assigned by Pastebin, to each
upload. To view your paste, open https://pastebin.com/ `your paste id`, in a web browser.

```client.download(id)```

Use this method to download the text content of an existing paste. You must specify it's
paste id. The text content will be returned as a string.

**New methods and functionality coming soon.**

---

### Notes

One thing to note is that Pastebin only allows ten uploads per twentyfour hours for guest
users. After ten uploads, your IP will be blacklisted until the following day. There are
various ways to get around this (i.e Tor), but the API does not currently provide any 
such functions.

---

### Requirements

The requests library for Python3.
