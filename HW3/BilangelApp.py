from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def register():
    return render_template('register.html')

@app.route('/result', methods=['POST'])
def result():
    data = {
        'lastname': request.form['lastname'],
        'firstname': request.form['firstname'],
        'sex': request.form['sex'],
        'institution': request.form['institution'],
        'email': request.form['email']
    }
    return render_template('result.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
