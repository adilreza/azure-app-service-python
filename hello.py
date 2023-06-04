from flask import Flask, render_template
app=Flask(__name__,template_folder='template')

@app.route("/")
def index():
    return "<h1>Hello Azure! I am working now</h1>"

@app.route("/about")
def about():
    return "<div style='background-color: #ff0000;'>This is a div with a red background color.</div>"

@app.route("/home/")
def home():
   return render_template('home.html')

if __name__ == '__main__':
   app.run()