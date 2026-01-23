distance = int(input("Enter distance in km: "))

if distance <= 5:
    print("Local Delivery")
elif distance <= 20:
    print("City Delivery")
else:
    print("Outstation Delivery")
