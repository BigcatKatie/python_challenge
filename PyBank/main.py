# Import the csv module
import csv
from pathlib import Path

# Define the file path using pathlib
file_path = Path('Resources') / 'budget_data.csv'

# Assign variables
# To count the number of months
total_months = 0
# To sum up the total profit/losses
total_profit_loss = 0
# To keep track of profit/losses
previous_profit_loss = None
# To store the changes
changes = []
# To store the dates associated with the changes
dates = []

# Read the CSV file
with file_path.open('r') as file:
    reader = csv.reader(file)
    header = next(reader)
    
    for row in reader:
        date = row[0]
        profit_loss = int(row[1])
        
        # Count the total number of months
        total_months += 1
        
        # Calculate the total profit/loss
        total_profit_loss += profit_loss
        
        # Calculate the changes in profit/loss
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date)
            
        previous_profit_loss = profit_loss
        
# Calculate the average change
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase)]

greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease)]

# Print the results
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {total_months}")
print(f"Total:${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in profits: {greatest_decrease_date} (${greatest_decrease})")

# Export the results to a text file
with open('analysis/financial_analysis.txt','w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_loss}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
    