from flask import Flask, render_template, request, jsonify
from order_data import get_order_details

app = Flask(__name__, static_folder="../static", template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/track", methods=["POST"])
def track_order():
    order_id = request.json.get("order_id")
    details = get_order_details(order_id)
    if details:
        return jsonify({
            "found": True,
            "data": details
        })
    return jsonify({"found": False})

if __name__ == "__main__":
    app.run(debug=True)
