from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')

def hello_world():
    return "<h1 style='text-align: center'>Hello World!</h1>" \
           "<p>This is a paragraph</p>" \
           "<img src='https://th.bing.com/th/id/R.bb046fbaf03b3397b541abd0830cf3d4?rik=h%2f8IkmGKpgTClQ&pid=ImgRaw&r=0' width=400>"

app.run(debug=True)
