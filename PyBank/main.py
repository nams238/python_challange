import os
import csv

total_months = 0
net_profitLosses = 0
average_profitLosses = 0
months_change = []
months = []
profit = []
greatest_increase = []

csvpath = os.path.join(os.path.expanduser('~'),'Desktop','python_challange','PyBank','resources','budget_data.csv')

textpath = os.path.join(os.path.expanduser('~'),'Desktop', 'python_challange','PyBank','analysis','analysis.txt')

f = open(textpath, 'w')

with open(csvpath) as csvfile:
    
 csvreader = csv.reader(csvfile, delimiter=',')

 for rows in csvreader:
     #profit.append(int(rows[1]))
     months.append(rows[0])
    
     total_months = len(months)
     
     net_profitLosses = int(sum(profit))
     
     profit_loss_change = []
     
 for change in range(1, len(profit)):
         profit_loss_change.append(int(profit[change]) - int(profit[change - 1]))
         
         average_profitLoss = round(sum(profit_loss_change) / len(profit_loss_change), 2)
         
         greatest_increase = max(profit_loss_change)
         
         greatest_decrease = min(profit_loss_change)
         
 for rows in csvreader:
           if greatest_increase == int(rows[1]):
               months_change == int(rows[0])
               
print(f'Financial Analysis')
print ("----------------------------")
print(f' Total Months: {str(total_months)}')

print(f' Total: ${str(net_profitLosses)}')

print(f'Average Change: ${str(average_profitLosses)}')

print(f' Greatest Increase in Profits: (${greatest_increase}')

print(f' Greatest Decrease in Profits: (${greatest_decrease}')
print(f' {months_change}')

f.write("Financial Analysis")
f.write('n')
f.write("--------------------------------")
f.write('\n')
f.write(f' Average Change: ${str(average_profitLoss)}')
f.write('\n')
f.write(f' Greatest Increase in Profits: ${greatest_increase}')
f.write('\n')
f.write(f' Greatest Decrease in Profits: ${greatest_decrease}')
f.write('\n')            
         
         
        
print(f' Total Months: {str(total_months)}')