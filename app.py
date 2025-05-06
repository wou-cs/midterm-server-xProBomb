from flask import Flask, request

app = Flask(__name__)

@app.route("/api/calcs/<value>", methods=["GET"])
def calculate(value):
    try:
        num = int(value)
        if num <= 0:
            raise ValueError
    except ValueError:
        return {}, 404

    return {
        "dec": num - 1,
        "hex": hex(num)
    }

if __name__ == "__main__":
    app.run(port=8080)
