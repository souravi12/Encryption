from flask import Flask, render_template, request, redirect, url_for, session
from encrypt import encrypt_aes, encrypt_des , encrypt_rsa

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/encrypt",methods=["POST"])
def encrypt():
        message = request.form["message"]

        method =  request.form["method"]
        
        if method == "aes":
            encrypted = encrypt_aes(message)
        elif method == "des":
            encrypted = encrypt_des(message)
        elif method == "rsa":
            encrypted = encrypt_rsa(message)
        else:
            encrypted = "Unknown method"

        return render_template(
        "result.html",
        message=message,
        method=method.upper(),
        encrypted=encrypted
    )

if __name__ == "__main__":
    app.run(debug=True)       