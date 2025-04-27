# Sales Report Software

## 📦 Overview
The **Sales Report Software** is a Python-based tool designed to automate the process of generating and sending daily or periodic sales reports.  
It can:
- Generate financial summaries for businesses.
- Automatically send sales reports via WhatsApp.
- Attach and save sales data in Excel files (optional).

This tool is ideal for businesses that need regular reports without manual intervention.

## 🛠 Features
- 📤 **WhatsApp Messaging**: Automatically sends sales updates to a specified WhatsApp number.
- 🕒 **Smart Scheduling**: Automatically calculates the time to send the report, ensuring it's sent at the correct moment.
- 📊 **Excel Integration**: Saves the financial summary as an Excel file (optional).
- 🛡 **Security**: Uses WhatsApp Web for sending messages, ensuring secure communication.

## 🏁 Installation

### Requirements:
- Python 3.8 or higher
- An active internet connection

### Steps:
1. Clone or download this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/sales-report-software.git

# Install the required Python libraries:

**pip install pywhatkit pandas openpyxl**

# Set up your virtual environment and activate it:

# python -m venv venv

**venv\Scripts\activate   # On Windows*

**source venv/bin/activate  # On macOS/Linux**



# Run the software:

 python cal.py

## ⚙ Configuration
You can customize the following:

- **Phone number**: Enter the recipient's WhatsApp number (including country code) where the report will be sent.
- **Input file**: Upload a CSV or Excel file for your stock data.
- **Report Format**: The report contains sales summary and profit calculations. You can modify the message format in the `cal.py` script.

## 📊 Example Sales Report
### Financial Summary:
- **Total Sales (TS)** → ₦223,000
- **Total Cost (TC)** → ₦104,200
- **Staff Bill** → ₦10,000

### Total Expenses:
- **TC + Staff Bill** → ₦104,200 + ₦10,000 = ₦114,200

### Profit Calculation:
- **TS – Total Expenses** → ₦223,000 − ₦114,200 = ₦108,800

### Conclusion:
The figures indicate a **net profit of ₦108,800**.

🧑‍💻 How to Contribute
If you'd like to contribute, feel free to fork this repository and submit a pull request.
Please ensure your code adheres to the project's standards and includes tests where applicable.

📞 Support
For any issues or questions, please reach out to Purposewalks9@gmail.com.

📄 License
This software is free for personal use. You may modify or redistribute it as long as you credit the original author.

Thank you for using the Sales Report Software! 🚀 
