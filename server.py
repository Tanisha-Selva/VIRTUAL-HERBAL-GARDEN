from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ---------- MAIN PAGE ROUTES ----------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/find")
def find_page():
    return render_template("find.html")

@app.route("/explore")
def explore_page():
    return render_template("explore.html")

@app.route("/siddha")
def siddha_page():
    return render_template("siddha.html")


# ---------- DYNAMIC PLANT ROUTE ----------
@app.route("/<plant_name>")
def plant_details(plant_name):
    """
    Automatically opens templates/<plant_name>.html
    Example: /plant/tulsi -> templates/tulsi.html
    """
    try:
        return render_template(f"{plant_name}.html")
    except:
        return f"❌ Herb page '{plant_name}' not found.", 404


# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)
