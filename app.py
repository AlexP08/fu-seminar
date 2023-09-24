from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
def write_to_file(text):
    with open("text.txt", "a") as file:
        file.write(text + "\n")

# Функция для чтения текста из файла
def read_from_file():
    try:
        with open("text.txt", "r") as file:
            content = file.readlines()
        return content
    except FileNotFoundError:
        return []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        if text:
            write_to_file(text)
    content = read_from_file()
    return render_template("index.html", content=content)

if __name__ == "__main__":
    app.run(debug=True)


