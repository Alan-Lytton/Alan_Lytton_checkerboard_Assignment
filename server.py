from flask import Flask, render_template
app=Flask(__name__)

@app.route('/check')
def main_checker():
    num1 = 0
    num2 = 0
    main = "red"
    second = "black"
    return render_template('index.html', num1 = num1, num2 = num2, main = main, second =second)

@app.route('/check/<int:num1>')
def var_row_checker(num1):
    num2 = 0
    main = "red"
    second = "black"
    return render_template('index.html', num1 = num1, num2 = num2, main = main, second =second)

@app.route('/check/<int:num1>/<int:num2>')
def col_row_checker(num1,num2):
    main = "red"
    second = "black"
    return render_template('index.html', num1 = num1, num2 = num2, main = main, second =second )

@app.route('/check/<int:num1>/<int:num2>/<string:main>')
def one_color_checker(num1, num2, main):
    second = "black"
    return render_template('index.html', num1 = num1, num2 = num2, main= main, second = second)

@app.route('/check/<int:num1>/<int:num2>/<string:main>/<string:second>')
def two_color_checker(num1, num2, main, second):
    return render_template('index.html', num1 = num1, num2 = num2, main= main, second = second)


if __name__== "__main__":  # lines 10 and 11 are required on all server.py files and will not run without them.
    app.run(debug=True)