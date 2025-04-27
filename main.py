# main.py
import pandas as pd

# Define the product database
myvar = pd.DataFrame({
    "Products": [
        "André", "Blue Nun", "Don Julio", "Belaire", "Castel White", "Martinelli's Cider",
        "Toma Wine", "Exotic", "Monster", "Coca-Cola", "Water", "Mateus", "Carlo Rossi",
        "Campari Big", "Calypso", "Hennessy VSOP", "Hennessy VS", "Hennessy XO", "Heineken",
        "Martell VS", "Kabisa", "Best Cream", "Bailey's Cream", "Glenfiddich 12 years",
        "Glenfiddich 18 years", "Glenfiddich 21 years", "Jack", "Jameson Black Barrel",
        "Jameson", "Jack Daniel's Big", "Jack Daniel's Medium", "Remy Martins",
        "Smirnoff Vodka Big", "Smirnoff Vodka Small", "Black Bullet", "Grant", "Azul",
        "Shisha Flavor", "Red Label",
    ],
    "unit_price": [
        25000, 50000, 700000, 130000, 20000, 0, 18000, 5000, 4000, 1000, 500,
        18000, 20000, 0, 3000, 200000, 130000, 700000, 5000, 120000, 2500,
        18000, 20000, 0, 190000, 700000, 20000, 70000, 80000, 120000, 35000,
        80000, 15000, 5000, 5000, 20000, 700000, 5000, 30000,
    ],
    "Costprice": [
        12000, 35000, 400000, 70000, 10000, 0, 10000, 2000, 1500, 500, 200,
        10000, 11000, 0, 1500, 130000, 85000, 400000, 2000, 70000, 1500,
        10000, 12000, 0, 130000, 400000, 12000, 40000, 30000, 80000, 20000,
        50000, 4000, 2500, 2000, 10000, 400000, 3000, 15000,
    ],
})