from groq import Groq
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

load_dotenv()
client=Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

app = Flask(__name__)

UPLOAD_FOLDER = "static"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def main():

    output = ""

    if request.method == "POST":

        language = request.form.get("language")
        audio = request.files["audio"]

        if audio:

            filepath = os.path.join(app.config["UPLOAD_FOLDER"], audio.filename)
            audio.save(filepath)

            with open(filepath, "rb") as audio_file:

                result = client.audio.transcriptions.create(
                    file=audio_file,
                    model="whisper-large-v3-turbo",
                    language=language
                )

            output = result.text

    return render_template("index.html", output=output)
if __name__ == "__main__":
    app.run(debug=True)
