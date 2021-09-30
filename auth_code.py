import webbrowser
from urllib.parse import scheme_chars, urlparse 
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def __init__(self):
        self.code = ""
        
    def do_GET(self):
        url = urlparse(self.path)
        if url.query != "error=access_denied":
            self.code = url.query[5:]
        return self.code
    def set_code(self):
            return self.code

class Redirect(BaseHTTPRequestHandler):
   def do_GET(self):
       self.send_response(302)
       self.send_header('Location',"https://spotify.com" )
       self.end_headers()

class Auth:
    def __init__(self):
        self.id = "658d2f41c2624f768ac0202033459a25"
        self.redirect_uri = "http://127.0.0.1:8000/"
        self.scope = "user-read-private,user-read-email"
        self.challenge = "ag0Tkjgpq4kigDYFfQrzdvItgJF1HKdQvb9_lm1rp18"  

    def user_authentication(self):
        url = f"https://accounts.spotify.com/authorize?client_id={self.id}&response_type=code&redirect_uri={self.redirect_uri}&scope={self.scope}&code_challenge_method=S256&code_challenge={self.challenge}"
        webbrowser.open(url,new=1, autoraise = True)
        out = Handler()
        http_handler = HTTPServer(('', 8000), out)
        http_handler.handle_request()
        http_handler.socket.close()
        HTTPServer(("", 8000), Redirect).handle_request()
        return out
