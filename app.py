from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return "testing"

