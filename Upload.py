# upload.py
import pandas as pd

def UPLOAD(file_type):
    file_type = file_type.lower()

    if file_type == "csv":
        path = input(f"Enter your {file_type} file path: ")
        data = pd.read_csv(path)
        return data

    elif file_type == "excel":
        path = input(f"Enter your {file_type} file path: ")
        data = pd.read_excel(path)
        return data

    else:
        print("Unsupported file type. Please use csv or excel.")
        return None
