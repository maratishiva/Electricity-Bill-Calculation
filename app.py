from flask import Flask, request, jsonify

app = Flask(__name__)

def calculate_bill(units):
    if units < 0:
        raise ValueError("Units cannot be negative")
    if units <= 100:
        return units * 2
    if units <= 200:
        return 100 * 2 + (units - 100) * 3
    return 100 * 2 + 100 * 3 + (units - 200) * 5

@app.get("/")
def home():
    return "Electricity Bill Calculator"

@app.get("/bill")
def bill():
    try:
        units = int(request.args.get("units", "0"))
        amount = calculate_bill(units)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400
    return jsonify({"units": units, "bill": amount})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
