from flask import Flask, request, jsonify
import random

app = Flask(__name__)  

#GET 
@app.route('/number/', methods=['GET'])
def get_number():
    try:
        param = float(request.args.get('param'))
    except (TypeError, ValueError):
        return jsonify({"error": "Должно быть число"}), 400

    random_num = random.uniform(0, 100)
    result = random_num * param
    
    return jsonify({"result": result, "random_num": random_num, "param": param})

#POST 
@app.route('/number/', methods=['POST'])
def post_number():
    try:
        data = request.get_json()
        json_param = float(data.get('jsonParam')) 
    except (TypeError, ValueError, AttributeError):
        return jsonify({"error": "Некорректное значение"}), 400

    random_num = random.uniform(0, 100)
    operation = random.choice(["+", "-", "*", "/"])

    if operation == "+":
        result = random_num + json_param
    elif operation == "-":
        result = random_num - json_param
    elif operation == "*":
        result = random_num * json_param
    elif operation == "/":
        if json_param == 0:
            return jsonify({"error": "Деление на ноль!"}), 400
        result = random_num / json_param

    return jsonify({
        "random_number": random_num,
        "operation": operation,
        "result": result
    })

#DELETE 
@app.route('/number/', methods=['DELETE'])
def delete_number():
    random_num = random.uniform(0, 100)
    operation = random.choice(["+", "-", "*", "/"])
    return jsonify({
        "random_number": random_num,
        "operation": operation
    })

if __name__ == '__main__': 
    app.run(debug=True)

    