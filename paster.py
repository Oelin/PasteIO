from sys import argv
from requests import session


__all__ = ['copy', 'paste']


class user:
  def __init__(self, src='https://pastebin.com'):
    
    self.src = src        
    self.sess = session()
        
    if not self.auth():
      throw Exception('could not auth with pastebin')

            
    def auth(self):
      resp = self.sess.head(self.src)
      cookies = self.sess.cookies

      return bool(cookies)

    
    def paste(self, name, text)
      url = f'{self.src}/post.php'
      self.sess.post(url, **form(name, text))
        
      # return the paste id
        
      return self.sess.cookies.get('pastebin_posted')

    
    def copy(self, id):
      url = f'{self.src}/raw/{id}'
      return self.sess.get(url).text

    
def form(name, text):
  return {
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


user = user()
copy = user.copy
paste = user.paste
