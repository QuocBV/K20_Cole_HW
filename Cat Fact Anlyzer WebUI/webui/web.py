from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests

ANALYZER_URL = "http://analyzer:5000/analyze"

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    try:
        data = requests.get(ANALYZER_URL).json()
    except Exception as e:
        return f"<h1>Error contacting analyzer: {e}</h1>"

    rows = ""
    for item in data:
        rows += f"""
            <tr>
                <td>{item['fact']}</td>
                <td>{item['length']}</td>
                <td>{item['fluffiness_score']}</td>
            </tr>
        """

    html = f"""
    <html>
    <head>
        <title>Cat Fact Analyzer 😺</title>
        <style>
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; }}
            th {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h1>🐱 Cat Fact Analyzer — Web UI</h1>
        <table>
            <tr><th>Fact</th><th>Length</th><th>Fluffiness Score</th></tr>
            {rows}
        </table>
    </body>
    </html>
    """
    return html
