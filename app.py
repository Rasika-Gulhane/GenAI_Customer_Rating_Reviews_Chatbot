from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
from SentiBot.retrieval import generation
from SentiBot.ingest import ingestdata


app = Flask(__name__)

load_dotenv()

vstore=ingestdata(None)     # "done" in place of run after storing values in vectorDB AstraDB
chain=generation(vstore)

@app.route("/")
def index():
    return render_template('sentichat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    result=chain.invoke(input)
    print("Response : ", result)
    return str(result)

if __name__ == '__main__':
    app.run(debug= True)