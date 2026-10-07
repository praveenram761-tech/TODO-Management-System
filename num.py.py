from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():

    voltage = float(request.form["voltage"])
    current = float(request.form["current"])
    temperature = float(request.form["temperature"])

    if voltage > 240:
        voltage_status = "Over Voltage"
    elif voltage < 220:
        voltage_status = "Low Voltage"
    else:
        voltage_status = "Normal"

    if current > 6:
        current_status = "High Current"
    elif current < 4:
        current_status = "Low Current"
    else:
        current_status = "Normal"

    if temperature > 40:
        temperature_status = "High Temperature"
    else:
        temperature_status = "Normal"

    return render_template(
        "index.html",
        voltage=voltage,
        current=current,
        temperature=temperature,
        voltage_status=voltage_status,
        current_status=current_status,
        temperature_status=temperature_status
    )


if __name__ == "__main__":
    app.run(debug=True)