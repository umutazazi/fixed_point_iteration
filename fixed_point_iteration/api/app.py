from flask import Flask, request, jsonify
from fixedpoint import FixedPoint

app = Flask(__name__)



@app.route('/find_root', methods=['POST'])
def find_root():
    data = request.json
    f_str = data['function']
    x0 = data['initial_guess']
    tol = data['tolerance']
    max_iter = data['max_iterations']

    g = FixedPoint.find_gx(f_str)

    if g:
        root, iterations, iteration_values = FixedPoint.fixed_point_iteration(g, x0, tol, max_iter)
        return jsonify({"root": str(root), "iterations": iterations, "iteration_values": iteration_values})
    else:
        return jsonify({"error": "Could not find a suitable g(x)"}), 400


if __name__ == '__main__':
    app.run(debug=True)
