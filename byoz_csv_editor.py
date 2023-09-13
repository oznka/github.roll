import csv
import datetime

# Save a CSV file of your transactions in the same folder as this project and put the name below
file_name = input("Please enter file name:")
statement = file_name
def finance_manager(file):
    sum = 0
    transactions = []
    #Reading csv file
    with open(file, mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        #Selecting necessary columns 
        transactions.append((header[0], header[2], header[3]))
        
        #Reading csv file line by line with for loop
        for row in csv_reader:
            
            #Reading and reformatting date format
            csv_date = datetime.datetime.strptime(row[0], "%d/%m/%Y")
            date = csv_date.strftime("%m/%Y")
            
            desc = row[2]
            amount = float(row[3])

            transaction = (date, desc, amount)
            sum += amount
            transactions.append(transaction)
        
        print(f"The sum of your transaction is {sum}")
        print()
        return transactions


#Saving csv file
def export(file, file_name):

    filename = f"{file_name}.csv"

    with open(filename, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(file)

    print("CSV file exported successfully.")

export(finance_manager(statement), "output")

