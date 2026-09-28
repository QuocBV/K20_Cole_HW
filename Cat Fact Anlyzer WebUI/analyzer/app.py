import requests
import pandas as pd
from flask import Flask, jsonify

URL = "https://catfact.ninja/facts?limit=20"

app = Flask(__name__)

@app.route("/analyze")
def analyze():
    resp = requests.get(URL)
    data = resp.json()["data"]
    df = pd.DataFrame(data)

    df["length"] = df["fact"].str.len()
    df["fluffiness_score"] = df["length"] % 13

    # Return JSON for webUI
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
