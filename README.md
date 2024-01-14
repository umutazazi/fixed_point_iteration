# Fixed-Point Iteration Root Finder

This repository contains a Python project that implements a web-based application for finding roots of mathematical functions using the fixed-point iteration method. The project is divided into three main components:

## Components

1. **GUI Application (`main.py`)**:
   - A `tkinter` based graphical user interface allowing users to input a function, an initial guess, tolerance, and maximum iterations.
   - Sends a request to the Flask API to perform the fixed-point iteration.
   - Visualizes the convergence of the iteration process using `matplotlib`.

2. **Flask API (`app.py`)**:
   - A Flask web application serving as the backend.
   - Handles POST requests at the `/find_root` endpoint.
   - Uses the `FixedPoint` class to compute the root of the function.

3. **Fixed-Point Iteration Logic (`fixedpoint.py`)**:
   - Contains the `FixedPoint` class with methods for the fixed-point iteration.
   - `fixed_point_iteration`: Performs the iteration given a function, initial guess, tolerance, and maximum iterations.
   - `find_gx`: Finds a suitable function `g(x)` for the iteration, using symbolic computation.

## Getting Started

### Prerequisites

- Python 3
- Libraries: `flask`, `numpy`, `matplotlib`, `sympy`, `tkinter`, `requests`

### Installation

1. Clone the repository to your local machine.
2. Install the required Python packages:

pip install flask numpy matplotlib sympy requests


### Running the Application

1. Start the Flask API:

python app.py

2. Launch the GUI application:

python main.py


## Usage

- Enter a function in the GUI's function field (e.g., `x**2 - x - 2`).
- Set your initial guess, tolerance, and maximum iterations.
- Click "Find Root" to start the computation.
- Observe the convergence process visually in the GUI.

## Contributing

Contributions to enhance the functionality or efficiency of this project are welcome. Please follow the standard procedures for contributing to a GitHub project.




