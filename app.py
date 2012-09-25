import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['GET', 'POST'])
def process():
    file = request.files['file']
    
    text = file.readlines()

    word_groups = {}
     
    for word in text:
        word = word.rstrip("\n")
        group = "".join(sorted(list(word)))
        if group in word_groups:
            word_groups[group].append(word)
        else:
            word_groups[group] = [word]

    word_groups = dict(filter(lambda (k, v): len(v) > 1, word_groups.items()))

    return render_template("process.html", word_groups=word_groups)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
