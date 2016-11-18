from flask import Flask
app = Flask(__name__)

#index
@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    app.run(debug=True)
