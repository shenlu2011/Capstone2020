from flask import Flask, render_template, request, redirect



ROOT = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/taxi')
def taxi():
  return render_template('taxi.html', root=ROOT)


if __name__ == '__main__':
  app.run(debug=True)