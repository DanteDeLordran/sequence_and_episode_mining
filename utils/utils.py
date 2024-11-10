import numpy as np
from tkinter import filedialog
from numpy import ndarray


def get_csv_as_matrix() -> ndarray:
    matrix = np.loadtxt(filedialog.askopenfilename(), delimiter=',', dtype=str)
    return matrix