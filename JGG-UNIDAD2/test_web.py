from flask import Flask, render_template, request, redirect
from JGGUNIDAD2_module import equation, equation2


app = Flask(__name__)


@app.route('/')
def hello() -> '302':
    return redirect('/entry')


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='JGG_UNIDAD-2')


@app.route('/exec_equation', methods=['GET', 'POST'])
def execute() -> 'html':
    P= float(request.form['P'])
    h= float(request.form['h'])
    a= float(request.form['a'])
    title = 'This is the equation\'s result'
    result = float(equation(P, h, a))
    return render_template('result.html',
                           the_title=title,
                           the_P=P,
                           the_h=h,
                           the_a=a,
                           the_result=result, )


if __name__ == '__main__':
    app.run()
