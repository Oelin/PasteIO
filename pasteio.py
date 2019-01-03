'PasteIO, by Oelin <me.oelin@gmail.com>'



from sys import argv
from requests import session



# Define which objects should be accessable when the library is imported.

__all__ = ['client']



# This class represents (or mimics) an anonymous guest user on Pastebin.

class client:
    # The `source` argument specifies which server the client should consider to be
    # Pastebin. Ordinarily, this would be 'https://pastebin.com/', but could also point to
    # an alias, mirror site or proxy.

    def __init__(self, source):
        self.source = source

        # The requests session object allows for a session to be maintained between requests
        # to a server.
        
        self.session = session()
        
    # Make a HEAD request to Pastebin in order to retrieve session cookies. This enables the
    # client to take further actions such as creating new pastes.
    
    def auth(self):
        response = self.session.head(self.source)
        cookies = self.session.cookies

        return bool(cookies)

    # Start a new session.

    def new(self, source):
        self.__init__(source)

    # Upload a new paste to Pastebin by sending a multipart/form encoded POST request to
    # '/post.php'.

    def upload(self, name, text):
        # Generate an upload form for the new paste.
      
        form = makeform(name, text)

        # Upload the paste by posting the form data to '/post.php'.

        to = self.source + '/post.php'
        self.session.post(to, **form)

        # Extract the cookie which holds the paste id and return it's value.

        cookies = self.session.cookies
        id = cookies.get('pastebin_posted')

        return id

    # Download a the content of a paste from Pastebin.

    def download(self, id):
        _from = self.source + '/raw/' + id
      
        response = self.session.get(_from)
        text = response.text

        return text



# Generate multipart form feilds required to upload new pastes to Pastebin. The form is
# created dynamically, given the paste's name and text content.

def makeform(name, text):
    form = {
        'files': {
            'paste_name': (
                None,
                name
            )
        },

        'data': {
            'paste_format': 1,
            'paste_expire_data': 'N',
            'paste_private': 0,
            'submit_hidden': 'submit_hidden',
            'paste_code': text
        }
    }

    return form
