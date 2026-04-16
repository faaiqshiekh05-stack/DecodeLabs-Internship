# Step 1: Open Your Dataset

import pandas as pd

data = pd.read_excel("D:/internship as data analyst/DecodeLab/1st task/Dataset for Data Analytics.xlsx")

print(data)
print(data.head(10))
print(data.tail(10))


# Step 2: Find Missing Values

print(data.isnull().sum())

# The CouponCode column had missing values, which were replaced with 'No Coupon'

data['CouponCode'] = data['CouponCode'].fillna('No Coupon')

# Verify missing values again
print(data.isnull().sum())


# Step 3: Check & Remove Duplicates

print(data.duplicated().sum())
print(data['OrderID'].duplicated().sum())

# No duplicate data found in dataset


# Step 4: 2 decimal places

data["UnitPrice"] = data["UnitPrice"].round(2)
data["Quantity"] = data["Quantity"].round(2)


# Step 5: Date format

data["Date"] = pd.to_datetime(data["Date"]).dt.date

print(data)


# Step 6: Save Your Cleaned File

data.to_excel(r"D:\internship as data analyst\DecodeLab\Cleaned_Data_Project1.xlsx", index=False)

print("Project saved successfully!")
