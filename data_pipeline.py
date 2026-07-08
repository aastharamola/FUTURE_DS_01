import csv
from collections import defaultdict
from datetime import datetime

print("--- Starting Data Processing with Standard Library ---")

data = []
header = []
duplicates_count = 0
missing_count = defaultdict(int)

with open('Sample - Superstore.csv', 'r', encoding='latin-1') as f:
    reader = csv.reader(f)
    header = next(reader)
    
    seen = set()
    for row in reader:
        row_tuple = tuple(row)
        if row_tuple in seen:
            duplicates_count += 1
            continue
        seen.add(row_tuple)
        
        for col_idx, val in enumerate(row):
            if not val.strip():
                missing_count[header[col_idx]] += 1
                
        data.append(dict(zip(header, row)))

print(f"Initial shape: {len(data) + duplicates_count}")
print(f"Duplicate rows found: {duplicates_count}")
print(f"Missing values found: {dict(missing_count)}")

with open('Cleaned_Superstore.csv', 'w', newline='', encoding='latin-1') as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
print("Saved Cleaned_Superstore.csv")

print("\n--- Starting EDA ---")

total_sales = 0.0
total_profit = 0.0
orders = set()
customers = set()
products = set()
categories = set()

monthly_stats = defaultdict(lambda: {'Sales': 0.0, 'Profit': 0.0})
category_stats = defaultdict(lambda: {'Sales': 0.0, 'Profit': 0.0})
region_stats = defaultdict(lambda: {'Sales': 0.0, 'Profit': 0.0})
product_sales = defaultdict(float)
product_profit = defaultdict(float)
customer_sales = defaultdict(float)
discount_stats = defaultdict(lambda: {'Sales': 0.0, 'Profit': 0.0})
shipping_stats = defaultdict(lambda: {'Sales': 0.0, 'Profit': 0.0})

for row in data:
    try:
        sales = float(row['Sales'].replace(',', ''))
        profit = float(row['Profit'].replace(',', ''))
        discount = float(row['Discount'])
    except ValueError:
        continue
        
    total_sales += sales
    total_profit += profit
    
    orders.add(row['Order ID'])
    customers.add(row['Customer ID'])
    products.add(row['Product ID'])
    categories.add(row['Category'])
    
    try:
        dt = datetime.strptime(row['Order Date'], '%m/%d/%Y')
        year_month = dt.strftime('%Y-%m')
        monthly_stats[year_month]['Sales'] += sales
        monthly_stats[year_month]['Profit'] += profit
    except ValueError:
        pass
        
    category_stats[row['Category']]['Sales'] += sales
    category_stats[row['Category']]['Profit'] += profit
    
    region_stats[row['Region']]['Sales'] += sales
    region_stats[row['Region']]['Profit'] += profit
    
    product_sales[row['Product Name']] += sales
    product_profit[row['Product Name']] += profit
    
    customer_sales[row['Customer Name']] += sales
    
    discount_val = f"{discount:.2f}"
    discount_stats[discount_val]['Sales'] += sales
    discount_stats[discount_val]['Profit'] += profit
    
    shipping_stats[row['Ship Mode']]['Sales'] += sales
    shipping_stats[row['Ship Mode']]['Profit'] += profit

with open('eda_results.txt', 'w', encoding='utf-8') as f:
    f.write("--- EDA RESULTS ---\n")
    
    total_orders = len(orders)
    f.write(f"Total Sales: ${total_sales:,.2f}\n")
    f.write(f"Total Profit: ${total_profit:,.2f}\n")
    f.write(f"Total Orders: {total_orders:,}\n")
    f.write(f"Average Order Value: ${(total_sales/total_orders):,.2f}\n")
    f.write(f"Profit Margin: {(total_profit/total_sales)*100:.2f}%\n")
    f.write(f"Number of Customers: {len(customers):,}\n")
    f.write(f"Number of Products: {len(products):,}\n")
    f.write(f"Number of Categories: {len(categories):,}\n\n")

    f.write("Monthly Trend (Top 5 & Bottom 5 by date):\n")
    sorted_months = sorted(monthly_stats.items())
    for ym, stats in sorted_months[:5] + sorted_months[-5:]:
        f.write(f"{ym} -> Sales: ${stats['Sales']:,.2f} | Profit: ${stats['Profit']:,.2f}\n")
    f.write("\n")
    
    f.write("Category Summary:\n")
    for cat, stats in category_stats.items():
        pm = (stats['Profit']/stats['Sales'])*100 if stats['Sales'] else 0
        f.write(f"{cat} -> Sales: ${stats['Sales']:,.2f} | Profit: ${stats['Profit']:,.2f} | Margin: {pm:.2f}%\n")
    f.write("\n")

    f.write("Region Summary:\n")
    for reg, stats in region_stats.items():
        f.write(f"{reg} -> Sales: ${stats['Sales']:,.2f} | Profit: ${stats['Profit']:,.2f}\n")
    f.write("\n")

    f.write("Top 10 Products by Sales:\n")
    top_prods = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)[:10]
    for p, s in top_prods:
        f.write(f"{p}: ${s:,.2f}\n")
    f.write("\n")

    f.write("Bottom 10 Products by Profit (Biggest Losers):\n")
    bot_prods = sorted(product_profit.items(), key=lambda x: x[1])[:10]
    for p, pr in bot_prods:
        f.write(f"{p}: ${pr:,.2f}\n")
    f.write("\n")

    f.write("Top 5 Customers by Sales:\n")
    top_custs = sorted(customer_sales.items(), key=lambda x: x[1], reverse=True)[:5]
    for c, s in top_custs:
        f.write(f"{c}: ${s:,.2f}\n")
    f.write("\n")
    
    f.write("Discount Impact:\n")
    for d, stats in sorted(discount_stats.items()):
        pm = (stats['Profit']/stats['Sales'])*100 if stats['Sales'] else 0
        f.write(f"Discount {d} -> Sales: ${stats['Sales']:,.2f} | Profit: ${stats['Profit']:,.2f} | Margin: {pm:.2f}%\n")
    f.write("\n")

    f.write("Shipping Analysis:\n")
    for sm, stats in shipping_stats.items():
        f.write(f"{sm} -> Sales: ${stats['Sales']:,.2f} | Profit: ${stats['Profit']:,.2f}\n")

print("EDA results written to eda_results.txt")
