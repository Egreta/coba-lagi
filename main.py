from flask import Flask, render_template, request
from utils import predict_text

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download():
    username = request.args.get('username')
    password = request.args.get('password')

    list_username = ['a', 'b', 'c']
    list_password = ['x', 'y', 'z']

    if username in list_username:
        id_user = list_username.index(username)

        if password == list_password[id_user]:

            return "Berhasil"
        else:

            return "password salah"
    else:

        return "username salah"