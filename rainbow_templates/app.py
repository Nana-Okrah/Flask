from flask import Flask, render_template, current_app as app

app = Flask(__name__)

@app.route('/friends')
def index():
    friends = ["Bob", "James", "Mary", "John"]
    return render_template('rainbow.html', friends = friends)

if __name__ == '__main__':from flask import Flask, render_template, current_app as app




