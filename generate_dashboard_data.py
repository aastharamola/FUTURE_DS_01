import csv
import json
from collections import defaultdict
from datetime import datetime

print("Generating Dashboard Data...")

data = []
with open('Cleaned_Superstore.csv', 'r', encoding='latin-1') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

total_sales = 0.0
total_profit = 0.0
orders = set()
monthly_stats = defaultdict(lambda: {'Sales': 0.0, 'Profit': 0.0})
category_stats = defaultdict(lambda: {'Sales': 0.0, 'Profit': 0.0})
region_stats = defaultdict(lambda: {'Sales': 0.0, 'Profit': 0.0})

for row in data:
    try:
        sales = float(row['Sales'])
        profit = float(row['Profit'])
    except ValueError:
        continue
        
    total_sales += sales
    total_profit += profit
    orders.add(row['Order ID'])
    
    try:
        dt = datetime.strptime(row['Order Date'], '%Y-%m-%d')
    except ValueError:
        try:
            dt = datetime.strptime(row['Order Date'], '%m/%d/%Y')
        except:
            continue
            
    year_month = dt.strftime('%Y-%m')
    monthly_stats[year_month]['Sales'] += sales
    monthly_stats[year_month]['Profit'] += profit
        
    category_stats[row['Category']]['Sales'] += sales
    category_stats[row['Category']]['Profit'] += profit
    
    region_stats[row['Region']]['Sales'] += sales
    region_stats[row['Region']]['Profit'] += profit

sorted_months = sorted(monthly_stats.keys())
trend_labels = sorted_months
trend_sales = [monthly_stats[m]['Sales'] for m in sorted_months]
trend_profit = [monthly_stats[m]['Profit'] for m in sorted_months]
dashboard_data = {
    "kpis": {
        "totalSales": total_sales,
        "totalProfit": total_profit,
        "totalOrders": len(orders),
        "profitMargin": (total_profit / total_sales) * 100 if total_sales else 0
    },
    "trend": {
        "labels": trend_labels,
        "sales": trend_sales,
        "profit": trend_profit
    },
    "category": {
        "labels": list(category_stats.keys()),
        "sales": [stats['Sales'] for stats in category_stats.values()],
        "profit": [stats['Profit'] for stats in category_stats.values()]
    },
    "region": {
        "labels": list(region_stats.keys()),
        "profit": [stats['Profit'] for stats in region_stats.values()]
    }
}

with open('dashboard_data.js', 'w', encoding='utf-8') as f:
    f.write("const dashboardData = ")
    json.dump(dashboard_data, f, indent=4)
    f.write(";\n")

print("Created dashboard_data.js successfully!")
