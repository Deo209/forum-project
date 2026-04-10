from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# simula database (memory)
posts = []

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html", posts=posts)


@app.route("/post", methods=["POST"])
def post():
    name = request.form["name"]
    comment = request.form["comment"]

    posts.append({
        "name": name,
        "comment": comment
    })

    return redirect("/")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]

    if file:
        path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(path)

    return redirect("/")


if __name__ == "__main__":
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    app.run(host="0.0.0.0", port=5000, debug=True)