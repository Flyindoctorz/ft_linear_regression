from train import trainer, estimate_price
import json

def predict():
    """predict the cost of a car based on its mileage"""
    try:
        with open("datas.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            theta0 = data["theta0"]
            theta1 = data["theta1"]
            ask = input("Enter the mileage of the car: ")
            if not ask.isnumeric() or int(ask) < 0:
                return ("Error: please enter a valid mileage")
            km = int(ask)
            km_max = data["km_max"]
            km_min = data["km_min"]
            km_normalise = (km - km_min) / (km_max - km_min)
            price = estimate_price(km_normalise, theta0, theta1)
            if price < 0:
                price = 0
            return(f"{price}")
    except:
        return(f"Error : please train the model first")


def main():
    res = predict()
    print(f"{res}")

if __name__ == "__main__":
    main()