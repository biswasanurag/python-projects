print("Welcome to PayUp!")
print()
event_name = input("What's the event name: ")
meal = input("What meal did you have: ")
cost = float(input("What was the cost of the meal: "))
service_charges = int(input("What was the service charges for the meal (for example 20%, type 20): ").strip("%"))
group_size = int(input("What was the group size for the meal: "))
# total_cost = "330"
# split_amount = "110"

service_charges_total = (service_charges / 100) * cost
grand_total = cost + service_charges_total
total_per_person = grand_total / group_size

print()
print(f"Here's the breakdown for {meal} at {event_name}:")
print()
print(f"Cost: ${cost:.2f}")
print(f"Service Charges: ${service_charges_total:.2f}")
print(f"Group Size: {group_size}")
print(f"Grand Total: ${grand_total:.2f}")
print()
print(f"Split Amount: ${total_per_person:.2f}")