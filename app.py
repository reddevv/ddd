from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/callback")
def index()
    return("sukses bosque")
    
import os
if __name__ == "__main__":
    app.run()    
