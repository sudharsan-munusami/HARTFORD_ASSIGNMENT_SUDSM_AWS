import os

from flask import Flask, render_template, request, redirect, send_file, url_for

from s3_demo import list_files, download_file, upload_file


app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = "1905-assignment1"


@app.route('/')
def entry_point():
    return 'Hello World!'


@app.route("/storage")
def storage():
    contents = list_files(BUCKET) #("flaskdrive")
    return render_template('storage.html', contents=contents)


@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        f.save(f.filename)
        upload_file(f"{f.filename}", BUCKET)

        return redirect("/storage")


@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        output = download_file(filename, BUCKET)

        return send_file(output, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085) #debug=True)
