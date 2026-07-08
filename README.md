# Business Sales Performance Analytics 📊

## Project Overview
This project is a comprehensive Data Analytics workflow focused on a retail superstore's sales performance. The goal of this project is to clean, analyze, and visualize over 9,900 transactional records to uncover business insights, optimize profitability, and formulate actionable recommendations that drive revenue.

This project was built to simulate a real-world client engagement, transforming raw CSV data into a professional executive dashboard and business report.

## Live Dashboard Demo
https://github.com/user-attachments/assets/99ee452e-9516-4f71-9b96-b3e841b38344

## Business Problem
The business needs to optimize its operations by identifying which products, categories, and regions are driving profitability, and which ones are underperforming. Without this insight, the company risks overspending on unprofitable marketing campaigns, maintaining excessive inventory of low-margin items, and losing out on high-value customer segments. 

## Dataset Description
The dataset (`Sample - Superstore.csv`) contains 9,994 transactional records with 21 attributes, covering 4 years of transactional data.
- **Categorical:** Order ID, Ship Mode, Customer ID, Customer Name, Segment, Country, City, State, Region, Product ID, Category, Sub-Category, Product Name
- **Numerical:** Row ID, Postal Code, Sales, Quantity, Discount, Profit
- **Temporal (Dates):** Order Date, Ship Date

## Data Cleaning & Pipeline
Prior to analysis, the dataset was rigorously cleaned (`data_pipeline.py`) to ensure data integrity:
- **Missing Values:** No critical missing values were found.
- **Duplicates:** No duplicate rows were identified in the dataset.
- **Formatting:** Date columns were converted into standardized Date formats to allow for accurate time-series analysis. 
- **Validation:** Ensured all numerical fields were parsed correctly.

## Exploratory Data Analysis (EDA) Summary
Through the EDA process, we extracted the following core findings:
- The business has generated a total of **$2.29M** in sales with a net profit of **$286K**.
- The overall profit margin is **12.47%**.
- **Technology** is the most profitable category ($145K), while **Furniture** is severely underperforming with only a 2.49% profit margin.
- Heavy discounts (above 20%) are significantly damaging profitability, with discounts of 30% or more resulting in massive net losses.

## Key Performance Indicators (KPIs)
- **Total Sales:** $2,297,200.86
- **Total Profit:** $286,397.02
- **Total Orders:** 5,009
- **Average Order Value (AOV):** $458.61
- **Profit Margin:** 12.47%
- **Best Selling Category:** Technology ($836,154.03)
- **Best Performing Region:** West ($725,457.82 Sales / $108,418.45 Profit)
- **Top Product:** Canon imageCLASS 2200 Advanced Copier ($61,599.82)

## Business Insights
1. **Technology Dominance:** Technology contributes 36.4% of total revenue and 50.7% of total profit (17.40% profit margin).
2. **Furniture Profitability Crisis:** While Furniture accounts for $741K in sales (32%), it only generates $18K in profit (2.49% margin).
3. **Regional Disparities:** The West region is the undisputed leader ($108K profit), while Central struggles with high sales ($501K) but low profit ($39K).
4. **The Discount Trap:** Any discount above 20% results in net negative profit.
5. **Customer Concentration:** The top 5 customers account for nearly $90K in sales (strong B2B reliance).
6. **Product Winners & Losers:** The 'Canon imageCLASS 2200 Advanced Copier' generated over $61K in sales. The 'Cubify CubeX 3D Printer' lost over $12,700 across two SKUs.
7. **Shipping Efficiency:** Standard Class shipping handles $1.35M in sales.
8. **Office Supplies Stability:** Highest volume of transactions and maintain a healthy 17.04% profit margin.
9. **Q4 Seasonality:** Massive spikes in Q4 (November/December).

## Actionable Recommendations
1. **Strictly cap discounts at 20%** to protect the overall profit margin.
2. **Restructure Furniture Pricing:** Investigate supply chain costs, raise prices, or phase out underperforming sub-categories.
3. **Double Down on Technology:** Increase marketing and inventory depth for high-margin Technology products.
4. **Phase Out Toxic SKUs:** Discontinue or aggressively liquidate the 'Cubify CubeX 3D Printer' line.
5. **Implement a VIP Customer Program:** Dedicated account management for the top 50 customers.
6. **Investigate Central Region Operations:** Conduct a localized audit of the Central region.
7. **Leverage Q4 Seasonality:** Begin inventory stockpiling and targeted marketing campaigns in early October.
8. **Promote Office Supplies as Add-ons** during checkout to boost AOV.
9. **Optimize Shipping:** Negotiate better bulk rates for Standard Class.
10. **Re-evaluate B2B Pricing:** Offer volume-based pricing structures for corporate clients.

## Power BI Dashboard Guidance
*(For reproducing the dashboard structure)*

### 1. Data Model & Relationships
- **Primary Table:** `Sales Data` (Cleaned_Superstore.csv).
- **Date Table (Recommended):** Create a dedicated Calendar table using DAX (`CALENDARAUTO()`). Link to `Sales Data[Order Date]` (1-to-many).

### 2. Essential DAX Measures
```dax
Total Sales = SUM('Sales Data'[Sales])
Total Profit = SUM('Sales Data'[Profit])
Total Orders = DISTINCTCOUNT('Sales Data'[Order ID])
Profit Margin % = DIVIDE([Total Profit], [Total Sales], 0)
Average Order Value = DIVIDE([Total Sales], [Total Orders], 0)
```

### 3. Dashboard Layout & UI Design
- **Theme:** Modern dark corporate or clean high-contrast light theme (avoid default colors).
- **Structure:** Top Bar (Title, Logo), Filter Pane (Year, Month, Region, Category), KPI Cards, Main Canvas.

### 4. Visualizations
1. **Monthly Sales & Profit Trend:** Line and Clustered Column Chart.
2. **Sales & Profit by Category:** Clustered Bar Chart.
3. **Regional Performance:** Filled Map or Donut Chart.
4. **Top 10 Products by Sales:** Matrix (Table) with Data Bars.
5. **Discount Impact on Profitability:** Scatter Chart.

## Folder Structure
```text
/
├── Sample - Superstore.csv      # Raw dataset
├── Cleaned_Superstore.csv       # Cleaned and processed data
├── data_pipeline.py             # Python script for Data Cleaning & EDA
├── generate_dashboard_data.py   # Python script to generate web dashboard JSON
├── eda_results.txt              # Output file containing raw KPI and EDA stats
├── dashboard.html               # Interactive Web Dashboard
├── dashboard_data.js            # Dashboard Data
├── dasbboard.mp4                # Live Demo Screen Recording
└── README.md                    # This documentation file
```
