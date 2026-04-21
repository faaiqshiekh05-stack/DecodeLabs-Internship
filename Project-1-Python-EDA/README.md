# 📊 Project 1: Data Cleaning & Exploratory Data Analysis (Python | PyCharm)

This project was developed in **PyCharm IDE** using Python and Pandas to clean, process, and prepare raw sales data for exploratory data analysis (EDA). The objective was to convert messy real-world transactional data into a structured, analysis-ready format suitable for business intelligence tools such as Power BI and Tableau.

The dataset was first imported using Pandas in PyCharm, and an initial inspection was performed using `data.head()`, `data.info()`, and `data.describe()` to understand structure, data types, and potential issues.

Missing values were detected using `data.isnull().sum()`. It was found that only the `CouponCode` column contained missing values, while all other key fields such as `OrderID`, `Date`, `Product`, `Quantity`, and `UnitPrice` were complete. The missing values in `CouponCode` were handled by replacing them with `"No Coupon"` using `data['CouponCode'] = data['CouponCode'].fillna('No Coupon')`, ensuring dataset consistency.

Duplicate data was checked using `data.duplicated().sum()` and `data['OrderID'].duplicated().sum()`. No duplicate records were found, confirming that each transaction was unique and the dataset maintained data integrity.

The `Date` column originally contained timestamp values such as `2023-01-04 00:00:00`, which were not required for analysis. This was cleaned using `data["Date"] = pd.to_datetime(data["Date"]).dt.date`, converting it into a clean `YYYY-MM-DD` format suitable for time-series analysis and BI tools.

To ensure numerical consistency, the `UnitPrice` column was standardized by rounding values to two decimal places using `data["UnitPrice"] = data["UnitPrice"].round(2)`, improving readability and financial accuracy.

Additional exploratory checks were performed in PyCharm, including grouping operations such as `groupby("Product")["Quantity"].sum()` to identify top-selling products and basic aggregation analysis to understand sales distribution.

After completing all cleaning steps, a final validation confirmed:
- No missing values
- No duplicate records
- Clean and standardized date format
- Consistent numeric formatting
- Fully structured dataset ready for analysis

The cleaned dataset was then exported using:
```python id="w9g0iu"
data.to_excel("Cleaned_Data_Project1.xlsx", index=False)
