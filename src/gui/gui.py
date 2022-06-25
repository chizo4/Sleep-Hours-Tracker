'''
SLEEP HOURS TRACKER: GUI window. (switch to pyqt6)

Date created: 05/2022

Author: Filip J. Cierkosz
'''

# from tkinter import *
# from PIL import ImageTk, Image
# import matplotlib.pyplot as plt
# import numpy as np

# # window setup
# root = Tk()
# root.title('Sleep Hours Tracker')
# root.configure(bg='white')
# root.geometry('400x400')

# # sample function for plotting the data
# def plot_graph():
#     house_prices = np.random.normal(200000, 25000, 5000)
#     plt.hist(house_prices, 50) #include 50 bins
#     plt.show()

# sample_btn = Button(root, text='PLOT', command=plot_graph)
# sample_btn.pack()

# root.mainloop()

# import sys
# from turtle import title
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
# from PyQt6.QtWidgets import QApplication, QWidget


# class Canvas(FigureCanvas):
#     def __init__(self, parent):
#         fig, self.ax = plt.subplots(figsize=(5,4), dpi=100)
#         super().__init__()
#         self.setParent(parent)

#         # Matplotlib script.

#         t = np.arange(0.0, 2.0, 0.01)
#         s = 1+np.sin(2*np.pi*t)

#         self.ax.plot(t,s)

#         self.ax.set(xlabel='time (s', ylabel='voltage (mV)', title='About as simple as it gets, folks')
#         self.ax.grid()


# class AppDemo(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.resize(1600, 800)

#         chart = Canvas(self)

# app = QApplication(sys.argv)
# demo = AppDemo()
# demo.show()
# sys.exit(app.exec())

import sys
import time

import numpy as np

from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qtagg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)

        static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        # Ideally one would use self.addToolBar here, but it is slightly
        # incompatible between PyQt6 and other bindings, so we just add the
        # toolbar as a plain widget instead.
        layout.addWidget(NavigationToolbar(static_canvas, self))
        layout.addWidget(static_canvas)

        dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(dynamic_canvas)
        layout.addWidget(NavigationToolbar(dynamic_canvas, self))

        self._static_ax = static_canvas.figure.subplots()
        t = np.linspace(0, 10, 501)
        self._static_ax.plot(t, np.tan(t), ".")

        self._dynamic_ax = dynamic_canvas.figure.subplots()
        t = np.linspace(0, 10, 101)
        # Set up a Line2D.
        self._line, = self._dynamic_ax.plot(t, np.sin(t + time.time()))
        self._timer = dynamic_canvas.new_timer(50)
        self._timer.add_callback(self._update_canvas)
        self._timer.start()

    def _update_canvas(self):
        t = np.linspace(0, 10, 101)
        # Shift the sinusoid as a function of time.
        self._line.set_data(t, np.sin(t + time.time()))
        self._line.figure.canvas.draw()


if __name__ == "__main__":
    # Check whether there is already a running QApplication (e.g., if running
    # from an IDE).
    qapp = QtWidgets.QApplication.instance()
    if not qapp:
        qapp = QtWidgets.QApplication(sys.argv)

    app = ApplicationWindow()
    app.show()
    app.activateWindow()
    app.raise_()
    qapp.exec()




























