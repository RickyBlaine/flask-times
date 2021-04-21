from flask import Flask,  render_template

app = Flask(__name__)

@app.route('/')
def index():     
    return '<h1>Welcome!</h1>'



@app.route('/headlines/<nm>')

def hello_name(nm):
    return render_template('name.html', name=nm)       


if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)