from flask import Flask,  render_template
import secrets
import json
import requests
import time 

#response = requests.get("http://api.datamuse.com/words?rel_rhy=blue")

key = secrets.API_KEY


#response = requests.get("https://api.nytimes.com/svc/topstories/v2/technology.json?api-key=GMMt7g4Uw4pqxOGaZzweeN3hBQOIJYOx")


# endpoint ='https://api.nytimes.com/svc/topstories/v2/technology.json?api-key='

# response = requests.get(endpoint+key)
# full_results = (json.loads(response.text))
# results_dict = full_results['results']
# print(results_dict[0]['title'])


#https://api.nytimes.com/svc/topstories/v2/world.json?api-key=yourkey



headline_list = []
def fetch_news ():
    
    endpoint ='https://api.nytimes.com/svc/topstories/v2/technology.json?api-key='
    response = requests.get(endpoint+key)
    full_results = (json.loads(response.text))
    results_dict = full_results['results']

    count = 1
    
    
    for result in results_dict:
        headline = (result['title']) 
        if count <6:
            headline_count = f'{headline}'
            headline_list.append(headline_count)
        count +=1

    return(headline_list)
        


fetch_news()
print(headline_list)

#print(response.text)


# baseurl = "https://api.nytimes.com/svc/topstories/v2/tech"

# key_url = '?api-key={key}'

# key_test = '?api-key=GMMt7g4Uw4pqxOGaZzweeN3hBQOIJYOx'
# response = requests.get(baseurl,key_test)

#print(response.text)

app = Flask(__name__)

@app.route('/')
def index():     
    return '<h1>Welcome!</h1>'

#flask

@app.route('/name/<nm>')

def hello_name(nm):
    return render_template('name.html', name=nm) 


@app.route('/headlines/<nm>')

def headline(nm):

    lines = headline_list

    return render_template('headlines.html', name=nm,
    headlines = lines) 





if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)