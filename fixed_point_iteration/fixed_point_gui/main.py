import tkinter as tk
from tkinter import messagebox
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


# Function to send request to Flask API
def find_root():
    api_url = "http://127.0.0.1:5000/api/fixed_point_iteration"  # Replace with your actual Flask API URL
    data = {
        "function": function_entry.get(),
        "initial_guess": float(initial_guess_entry.get()),
        "tolerance": float(tolerance_entry.get()),
        "max_iterations": int(max_iterations_entry.get())
    }

    response = requests.post(api_url, json=data)
    if response.status_code == 200:
        result = response.json()
        visualize_convergence(result['iterations'])
    else:
        messagebox.showerror("Error", "API Error")


# Function to visualize the convergence process
def visualize_convergence(iterations):
    fig, ax = plt.subplots()
    ax.set_xlim(0, iterations)  # Adjust according to your expected iteration count
    ax.set_ylim(-10, 10)  # Adjust the y limits according to your function's range

    x = float(initial_guess_entry.get())  # Starting point
    points_x, points_y = [], []

    for i in range(iterations):
        x = eval(function_entry.get().replace('x', str(x)))  # Be cautious with eval
        points_x.append(i)
        points_y.append(x)

    ax.plot(points_x, points_y, 'ro-', label='Iteration Points')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Function Value')
    ax.set_title('Convergence of Fixed-Point Iteration')
    plt.legend()

    # Embedding the plot in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=5, columnspan=2)


# GUI setup
root = tk.Tk()
root.title("Fixed Point Iteration")

tk.Label(root, text="Function (e.g., x**2 - x - 2):").grid(row=0)
function_entry = tk.Entry(root)
function_entry.grid(row=0, column=1)

tk.Label(root, text="Initial Guess:").grid(row=1)
initial_guess_entry = tk.Entry(root)
initial_guess_entry.grid(row=1, column=1)

tk.Label(root, text="Tolerance:").grid(row=2)
tolerance_entry = tk.Entry(root)
tolerance_entry.grid(row=2, column=1)

tk.Label(root, text="Max Iterations:").grid(row=3)
max_iterations_entry = tk.Entry(root)
max_iterations_entry.grid(row=3, column=1)

tk.Button(root, text="Find Root", command=find_root).grid(row=4, columnspan=2)

root.mainloop()
