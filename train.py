from load_csv import load
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

def estimate_price(mileage, theta0, theta1):
    """Estimate price for a given mileage"""
    return theta0 + (theta1 * mileage)

def trainer():
    """calculate the gradient and return it in a json"""
    tab = load("data.csv")
    tab.head()
    tab.plot(x='km', y='price', style='o')
    plt.title('Price vs Kilometers')
    plt.xlabel('Kilometers')
    plt.ylabel('Price')
    #plt.show()

    km_min = tab['km'].min()
    km_max = tab['km'].max()
    km_normalise = (tab['km'] - km_min) / (km_max - km_min)
    price = tab['price']

    theta0 = 0
    theta1 = 0
    m = len(tab)
    learningRate = 0.1
    iteration = 0
    for iteration in range(2000):
        tmp_theta0 = learningRate * (1 / m) * sum((estimate_price(km_normalise[i], theta0, theta1) - price[i]) for i in range(m))
        tmp_theta1 = learningRate * (1 / m) * sum((estimate_price(km_normalise[i], theta0, theta1) - price[i]) * km_normalise[i] for i in range(m))
        theta0 = theta0 - tmp_theta0
        theta1 = theta1 - tmp_theta1
    with open("datas.json", "w", encoding="utf-8") as file:
        json.dump({"theta0":theta0,
                   "theta1": theta1,
                   "km_min": float(km_min),
                   "km_max": float(km_max)
                  }, file, indent=4)
    return(print("Datas successfully loaded in file !"))


if __name__ == "__main__":
    trainer()