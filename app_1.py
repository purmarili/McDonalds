import random
from typing import Optional

from flask import Flask, render_template, redirect, url_for, request

app_1 = Flask(__name__)


@app_1.route('/')
def default():
    return redirect(url_for('home'))


@app_1.route('/home')
def home():
    number = random.randint(1, 10000)
    return f'<h1>{number}</h1>'


@app_1.route('/author')
def author():
    first_name = 'Jemali'
    last_name = 'Vashakmadze'
    age = 23
    return render_template('author.html', first_name=first_name, last_name=last_name, age=age)


@app_1.route('/calculate')
def calculate():
    number_1 = request.args.get('number_1')
    number_2 = request.args.get('number_2')
    operator_ = request.args.get('operator')

    if not validate_calculate_params(number_1, number_2, operator_):
        return render_template('calculate.html')

    number_1 = float(number_1)
    number_2 = float(number_2)

    match operator_:
        case 'sum':
            result = number_1 + number_2
        case 'sub':
            result = number_1 - number_2
        case 'div':
            result = number_1 / number_2
        case 'mul':
            result = number_1 * number_2
        case _:
            result = 0

    return render_template('calculate.html', result=f'{result:.2f}')


def validate_calculate_params(n_1: Optional[str], n_2: Optional[str], op_: Optional[str]):
    if n_1 is None or n_2 is None or op_ is None:
        return False
    if n_1.isnumeric() and n_2.isnumeric() and op_ in ['sum', 'sub', 'div', 'mul']:
        return True
    return False


if __name__ == '__main__':
    app_1.run(port=5005, debug=True)
