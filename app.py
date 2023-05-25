from flask import Flask

# greeting
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# some text for the page
header_text = '''
    <html>\n<head> <title> Flask Test </title> </head>\n <body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL to say hello to someone specific.</p>\n'''
home_link = '<p><a href ="/">Back</a></p>\n'
footer_text = '<body>\n<html>'

app = Flask(__name__)

#index page
app.add_url_rule('/', 'index', (lambda: header_text + 
    say_hello() + instructions + footer_text))

#appended <name> site
app.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

if __name__ == "__main__":
    app.debug = True
    app.run()