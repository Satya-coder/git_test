from flask import Flask, render_template, request, redirect
import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

mongo_url = os.getenv("mongo_url")
client= pymongo.MongoClient(mongo_url)
db = client.test
collection = db['todo_page']

app = Flask(__name__, template_folder= 'templates')
@app.route('/')

def home():

    return render_template('index.html')

@app.route('/submit_todo_item', methods = ['POST'])

def submit_todo_item():

    form_data = dict(request.form)

    try:
        collection.insert_one(form_data)
        return redirect('success')
    except:
        return 'Something went wrong,Please try again'
    
@app.route('/success')

def success():
    return "Data submitted successfully"

if __name__ == '__main__':
    app.run(debug=True)