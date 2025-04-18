# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:54:09 2024

@author: yashb
"""

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk




class ElectricityDemandForecastApp:
    
    
    def __init__(self, root):
        self.root = tk.Tk()
        #self.root.title("Electricity Demand Forecasting")
        w, h = self.root.winfo_screenwidth(),root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (w, h))
        ####################################
        image2 = Image.open('Firefly.jpg')

        image2 = image2.resize((w, h), Image.LANCZOS)

        background_image = ImageTk.PhotoImage(image2)


        background_label = tk.Label(root, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0) 
        
        
        
        

       
        # Labels and Entries
        self.label_features = [
            "Year", "Month", "Solar Energy (kWh/m^2)",
            "Electric Utility (kWh/m^2)", "Daylight Hours", "Peak Demand (kW)"
        ]
        self.entries = []
        #self.entries = []
        for i, label_text in enumerate(self.label_features):
            label = tk.Label(root, text=label_text, font=("TkDefaultFont", 10, "bold"), borderwidth=1, relief="solid")
            label.grid(row=i, column=0, padx=28, pady=30, sticky=tk.E)
            entry = tk.Entry(root, borderwidth=1, relief="solid")
            entry.grid(row=i, column=1, padx=15, pady=20)
            self.entries.append(entry)
        
        self.forecast_button = tk.Button(root, text="Forecast", command=self.forecast_demand, borderwidth=2, relief="raised", font=("TkDefaultFont", 10, "bold"),bg = "black", fg="red")
        self.forecast_button.grid(row=len(self.label_features), column=0, columnspan=2, padx=10, pady=15)

        
        self.fig, self.ax = plt.subplots(figsize=(7, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=0, column=2, rowspan=len(self.label_features), padx=10, pady=10)

        self.result_label = tk.Label(root, text="", borderwidth=1, relief="solid")
        self.result_label.grid(row=len(self.label_features)+1, column=0, columnspan=2, padx=10, pady=5)

        #for i, label_text in enumerate(self.label_features):
    def forecast_demand(self):
        try:
            input_data = [float(entry.get()) for entry in self.entries]
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for input.")
            return

        # Load your trained model here
        model = "linear_regression_model.joblib"
        # For demonstration, let's create a dummy model
        model = LinearRegression()
        X_train = np.array([[2019, 1,  5, 6, 8, 100], 
                             [2019, 2,  6, 7, 9, 110], 
                             [2019, 3,  7, 8, 10, 120]])  # Example training data
        y_train = np.array([110, 120, 130])  # Example labels
        model.fit(X_train, y_train)

        X = np.array([input_data])
        y_pred = model.predict(X)

        self.result_label.config(text=f"Predicted demand: {y_pred[0]:.2f} kW")

        # Plotting
        self.ax.clear()
        historical_years = np.arange(2019, 2020 + len(y_train))
        self.ax.plot(historical_years, np.concatenate(([0], y_train)), marker='o', linestyle='-', color='b', label='Historical Demand')
        self.ax.plot(historical_years[-1] + 1, y_pred, marker='o', color='r', label='Forecasted Demand')
        self.ax.legend()
        self.ax.set_xlabel('Year')
        self.ax.set_ylabel('Demand (kW)')
        self.ax.set_title('Electricity Demand Forecast')
        self.canvas.draw()

def main():
    root = tk.Tk()
    app = ElectricityDemandForecastApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
