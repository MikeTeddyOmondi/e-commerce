from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    context = {
        'fname': 'mike', 
        'lname': 'teddy',
        'text': 'e-commerce'
    }

    return render_template('index.html', data=context)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True) 