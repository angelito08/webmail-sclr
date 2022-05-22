from flask import Flask, render_template
import json
app = Flask(__name__)

@app.route("/")
def resyData():
    resy = []
    with open('data.json', 'r') as f:
        resy = json.load(f)
        f.close()
    return render_template('dynamic_angel-estrada.html', resy=resy)

if __name__ == '__main__':
    app.run(debug=True)