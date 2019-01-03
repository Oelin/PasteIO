# PasteIO

PasteIO is a simple API for using Pastebin as an anonymous guest. Follow the steps below
to get started.



### Getting Started

1. Create a client object. You must specify the URL of the Pastebin server. In almost all
cases, this will be 'https://pastebin.com/'. In some cases, you might want to point to an
alias, mirror site or proxy.

```myclient = client('https://pastebin.com')```

2. Authorise the client with the server. The client needs some session cookies to upload
and download pastes from Pastebin. The `auth` method will return `True` or `False`
depending on whether the cookies were obtained or not.

```myclient.auth()```

3. When the client has been authorised, you can choose what to do next. For instance, you
may like to upload a new paste.



### Methods

```client.upload(name, text)```

This uploads a new paste to Pastebin. If the upload was successfull, it will return the
"paste id" for the paste. Paste ids are unique identifiers assigned by Pastebin, to each
upload. For instance, https://pastebin.com/raw/2gHHDtZT, where 2gHHDtZT is the id.

```client.download(id)```

Use this method to download the text content of an existing paste. You must specify it's
paste id. The text content will be returned as a string.



**New methods and functionality coming soon.**
