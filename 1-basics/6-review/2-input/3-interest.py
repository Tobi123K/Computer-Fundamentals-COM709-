#Ask a user for amount of savings

print ("enter the current amount for savings")
amount_for_saving = float(input())

#Ask a user for amount of interes_rate
print ("enter the current percent interes rate")
amount_for_interes_rate = float(input())
# Calculate 
interest_rate = (amount_for_saving/amount_for_interes_rate) * 100.0
new_amount= amount_for_interes_rate + interest_rate
# Print an amoint for interes rate
print ("This is a new amount of savings", round(new_amount ,2))
