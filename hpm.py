import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the dataset from the CSV file
house_data = pd.read_csv("data.csv")

# Extract features and target variable
features_cols = [
    "bedrooms",
    "bathrooms",
    "sqft_living",
    "sqft_lot",
    "floors",
    "waterfront",
    "view",
    "condition",
    "sqft_above",
    "sqft_basement",
    "yr_built",
    "yr_renovated",
]
target_col = "price"

X = house_data[features_cols]
y = house_data[target_col]

# Train a simple linear regression model
model = LinearRegression()
model.fit(X, y)


# Tkinter GUI
def predict_price():
    try:
        bedrooms = int(bedrooms_entry.get())
        bathrooms = int(bathrooms_entry.get())
        sqft_living = float(sqft_living_entry.get())
        sqft_lot = float(sqft_lot_entry.get())
        floors = float(floors_entry.get())
        waterfront = int(waterfront_var.get())
        view = int(view_var.get())
        condition = int(condition_var.get())
        sqft_above = float(sqft_above_entry.get())
        sqft_basement = float(sqft_basement_entry.get())
        yr_built = int(yr_built_entry.get())
        yr_renovated = int(yr_renovated_entry.get())

        features = pd.DataFrame(
            {
                "bedrooms": [bedrooms],
                "bathrooms": [bathrooms],
                "sqft_living": [sqft_living],
                "sqft_lot": [sqft_lot],
                "floors": [floors],
                "waterfront": [waterfront],
                "view": [view],
                "condition": [condition],
                "sqft_above": [sqft_above],
                "sqft_basement": [sqft_basement],
                "yr_built": [yr_built],
                "yr_renovated": [yr_renovated],
            }
        )

        predicted_price = model.predict(features)[0]
        messagebox.showinfo(
            "Predicted Price", f"The predicted price is ${predicted_price:.2f}"
        )
    except ValueError:
        messagebox.showerror("Error", "Please enter valid values.")


# Create the main window
root = tk.Tk()
root.title("House Price Predictor")

# Create input fields
bedrooms_label = tk.Label(root, text="Bedrooms:")
bedrooms_label.pack()
bedrooms_entry = tk.Entry(root)
bedrooms_entry.pack()

bathrooms_label = tk.Label(root, text="Bathrooms:")
bathrooms_label.pack()
bathrooms_entry = tk.Entry(root)
bathrooms_entry.pack()

sqft_living_label = tk.Label(root, text="Sqft Living:")
sqft_living_label.pack()
sqft_living_entry = tk.Entry(root)
sqft_living_entry.pack()

sqft_lot_label = tk.Label(root, text="Sqft Lot:")
sqft_lot_label.pack()
sqft_lot_entry = tk.Entry(root)
sqft_lot_entry.pack()

floors_label = tk.Label(root, text="Floors:")
floors_label.pack()
floors_entry = tk.Entry(root)
floors_entry.pack()

waterfront_label = tk.Label(root, text="Waterfront (0/1):")
waterfront_label.pack()
waterfront_var = tk.StringVar(value="0")
waterfront_entry = tk.Entry(root, textvariable=waterfront_var)
waterfront_entry.pack()

view_label = tk.Label(root, text="View (0/1):")
view_label.pack()
view_var = tk.StringVar(value="0")
view_entry = tk.Entry(root, textvariable=view_var)
view_entry.pack()

condition_label = tk.Label(root, text="Condition (1-5):")
condition_label.pack()
condition_var = tk.StringVar(value="3")
condition_entry = tk.Entry(root, textvariable=condition_var)
condition_entry.pack()

sqft_above_label = tk.Label(root, text="Sqft Above:")
sqft_above_label.pack()
sqft_above_entry = tk.Entry(root)
sqft_above_entry.pack()

sqft_basement_label = tk.Label(root, text="Sqft Basement:")
sqft_basement_label.pack()
sqft_basement_entry = tk.Entry(root)
sqft_basement_entry.pack()

yr_built_label = tk.Label(root, text="Year Built:")
yr_built_label.pack()
yr_built_entry = tk.Entry(root)
yr_built_entry.pack()

yr_renovated_label = tk.Label(root, text="Year Renovated:")
yr_renovated_label.pack()
yr_renovated_entry = tk.Entry(root)
yr_renovated_entry.pack()

predict_button = tk.Button(root, text="Predict Price", command=predict_price)
predict_button.pack()

# Start the GUI event loop
root.mainloop()
