from flask import Flask, render_template, request
from audioPull import download_audio

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def download():
    audio_data = None
    if request.method == "POST":
        try:
            url = request.form["url"]
            audio_file = download_audio(url)
            with open(audio_file, 'rb') as f:
                audio_data = f.read()
            return render_template("index.html", audio_data=audio_data)
        except:
            return render_template("index.html", success=False) 
    return render_template("index.html", success=False)
    
if __name__ == "__main__":
    app.run(debug=True)
