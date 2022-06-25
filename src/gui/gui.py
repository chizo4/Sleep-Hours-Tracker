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

import sys
from turtle import title
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PyQt6.QtWidgets import QApplication, QWidget


class Canvas(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(5,4), dpi=100)
        super().__init__()
        self.setParent(parent)

        # Matplotlib script.

        t = np.arange(0.0, 2.0, 0.01)
        s = 1+np.sin(2*np.pi*t)

        self.ax.plot(t,s)

        self.ax.set(xlabel='time (s', ylabel='voltage (mV)', title='About as simple as it gets, folks')
        self.ax.grid()


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1600, 800)

        chart = Canvas(self)

app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec())






























