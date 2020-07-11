import csv
import os

#PyBank file location
PyBank_csv = os.path.join("Resources","budget_data.csv")

# Empty lists for data
profit = []
monthly_changes = []
date_list = []

# Values start at 0
month_count = 0
total_profit = 0
total_delta_profits = 0
initial_profit = 0

with open(PyBank_csv, newline="") as csvfile: #Open file and read
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #Create summary
    for row in csvreader:    
      # Count the months, starting at 1
      month_count = month_count + 1 

      # Find date for greatest and least value
      date_list.append(row[0])

      # Add the profit
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      #Avg change in profits
      final_profit = int(row[1])
      monthly_delta_profits = final_profit - initial_profit

      #monthly changes added to a list
      monthly_changes.append(monthly_delta_profits)

      total_delta_profits = total_delta_profits + monthly_delta_profits
      initial_profit = final_profit

      #Average change in profits
      average_change_profits = (total_delta_profits/month_count)
      
      #Greatest and least change i n profit, locate month
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)

      increase_date = date_list[monthly_changes.index(greatest_increase_profits)]
      decrease_date = date_list[monthly_changes.index(greatest_decrease_profits)]
      

    #Print analysis is shell
    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total Profits: ${total_profit}")
    print(f"Average Change:  $  {average_change_profits}")
    print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase_profits})")
    print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease_profits})")


