from flask import Flask, render_template, request
import io
import pandas as pd

app = Flask(__name__)


def sortstr(Y):
    for i in range(1, len(Y)):
        b = Y[i]
        j = i - 1
        while j >= 0 and b < Y[j]:
            Y[j + 1] = Y[j]
            j -= 1
        Y[j + 1] = b
    return Y


@app.route('/')
def index():
    filename = 'base.csv'
    with io.open(filename, 'w', encoding='utf-8') as f:
        f.write('name')
        f.write(',')
        f.write('email')
        f.write(',')
        f.write('answer')
        f.write('\n')
    return render_template('index.html')


@app.route('/answer/', methods=['GET', 'POST'])
def msg():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        answer = request.form['answer']
        filename = 'base.csv'
        with io.open(filename, 'a', encoding='utf-8') as f:
            f.write(name)
            f.write(',')
            f.write(email)
            f.write(',')
            f.write(answer)
            f.write('\n')
        return render_template('index.html')
    else:
        return render_template('index.html')


@app.route('/answer2/', methods=['GET', 'POST'])
def sort_func():
    if request.method == 'POST':
        string = list(map(int, request.form['string'].split()))
        string = sortstr(string)
        string = ' '.join(map(str, string))
        return render_template('flask.html', ans=string)
    else:
        return render_template('flask.html')


@app.route('/answer3/', methods=['GET', 'POST'])
def findstr():
    if request.method == 'POST':
        name1 = request.form['name1']
        f = pd.read_csv('base.csv', encoding='utf-8')
        answ2 = f[f['name'] == name1].values
        return render_template('put.html', ans2=answ2)
    else:
        return render_template('put.html')


if __name__ == '__main__':
    app.run(debug=True)