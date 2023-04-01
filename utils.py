from flask import Flask, render_template, request
# from utils import predict_text

app = Flask(_name_)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        # prediction = predict_text(text)
        return render_template('main.html', text=text)
    return render_template('main.html')

if _name_ == '_main_':
    app.run(debug=True, port=8080)