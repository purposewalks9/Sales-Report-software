# cal.py

import pandas as pd
import openpyxl
from Upload import UPLOAD
from main import myvar
import pywhatkit as p
import datetime
import time

# Ask user for file type
file_type = input("What type of file do you have? (csv/excel): ").strip()

# Upload stock data
stock_data = UPLOAD(file_type)

if stock_data is not None:
    # Merge the uploaded stock data with the product database
    final_data = pd.concat([myvar, stock_data], axis=1)

    # Example: Create a new Profit column
    final_data["TotalSales"] = final_data["unit_price"] * final_data["Quantity Sold"]
    final_data["Totalcost"] = final_data["Costprice"] * final_data["Quantity Sold"]
    final_data["Expense"] = final_data["Bill"] + final_data["Ex"] + final_data["Totalcost"]

    # Calculate total expenses
    total_expenses = final_data["Expense"].sum()
    print(f"Total expenses: {total_expenses}")

    # Calculate total sales
    total_sales = final_data["TotalSales"].sum()
    print(f"Total sales: {total_sales}")

    # Check results
    result = total_sales - total_expenses
    if result < 0:
        conclusion = f"Loss of ₦{abs(result):,.0f}."
    else:
        conclusion = f"Net profit of ₦{result:,.0f}."

    # Get today's date for the report
    today = datetime.datetime.now().strftime("%B %d, %Y")  # Example: April 27, 2025

    # Prepare the message
    message = f"""\
Sales Report – {today}
Financial Summary
Total Sales (TS) → ₦{total_sales:,.0f}

Total Cost (TC) → ₦{final_data['Totalcost'].sum():,.0f}

Staff Bill → ₦{final_data['Bill'].sum():,.0f}

Total Expenses
TC + Staff Bill → ₦{final_data['Totalcost'].sum():,.0f} + ₦{final_data['Bill'].sum():,.0f} = ₦{total_expenses:,.0f}

Profit Calculation
TS – Total Expenses → ₦{total_sales:,.0f} − ₦{total_expenses:,.0f} = ₦{result:,.0f}

Conclusion
The figures indicate a {conclusion}
"""

    print("\nGenerated Sales Report:\n")
    print(message)

    # Save final report as Excel too (optional)
    output_file = input("Enter file name to save (example: report.xlsx): ").strip().replace('"', '').replace("'", '')
    if not output_file.endswith(".xlsx"):
        output_file += ".xlsx"
    final_data.to_excel(output_file, index=False)
    print(f"File saved as {output_file}")

    # ---- Sending Message to WhatsApp ----

    # Get current time
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute + 2  # Add 2 minutes to prepare

    if current_minute >= 60:
        current_minute -= 60
        current_hour += 1

    if current_hour >= 24:
        current_hour = 0

    phone_number = input("Enter receiver WhatsApp number (e.g. +2348012345678): ").strip()

    print("Sending message...")
    p.sendwhatmsg(phone_number, message, current_hour, current_minute)

else:
    print("No data uploaded. Exiting...")
