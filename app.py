from flask import Flask
import yfinance as yf
app = Flask(__name__)

@app.route("/stockinfo/<stockname>")
def hello():
    return "hello"
    #mystockinfo = yf.Ticker(stockname)
    #return mystockinfo.info
