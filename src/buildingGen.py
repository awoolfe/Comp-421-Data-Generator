import random
managers = []
staff = []
tenants = []

f = open('tenantemail.txt', 'r')
managers = [line.rstrip('\n') for line in f]
f.close()
g=open('staffemail.txt', 'r')
staff = [line.rstrip('\n') for line in g]
g.close()
l = open("manageremail.txt", "r")
tenants = [line.rstrip('\n') for line in l]
l.close()

rents = ["1000", "800", "1100","1200","1150", "1300", "500", "600", "650", "700", "750"]
addresses = ["'123 Rue Notre-Dame, Montreal, QC, H4R5T1'","'60 Rue Sherbrooke , Montreal, QC, H6Q1P0'","'300 Gotham Lane, Montreal, QC, M6G4W2'","'808 Rue Maisonneuve, Montreal, QC, H6G4W2'","'4 Boul. St-Laurent, Montreal, QC, H6G4W2'","'333 Sesame Street, Montreal, QC, H6G4W2'"]

i = 1
while i<6:
    print("INSERT INTO Apartment (address, apartment_number, is_vacant, number_of_rooms, suggested_monthly_rent) VALUES (" + addresses[0] + "," +str(i)+ ", 'false' ," + "2," + random.choice(rents) + ");")
    i+=1
while i<11:
    print("INSERT INTO Apartment (address, apartment_number, is_vacant, number_of_rooms, suggested_monthly_rent) VALUES (" +addresses[0] + "," +str(i)+ ", 'false' ," + "3," + random.choice(rents) + ");")
    i+=1
while i<21:
    print(
        "INSERT INTO Apartment (address, apartment_number, is_vacant, number_of_rooms, suggested_monthly_rent) VALUES (" +
        addresses[0] + "," +str(i)+ ", 'false' ," + "2," + random.choice(rents) + ");")
    i+=1
i=1
while i<6:
    print(
        "INSERT INTO Apartment (address, apartment_number, is_vacant, number_of_rooms, suggested_monthly_rent) VALUES (" +
        addresses[1] + "," +str(i)+ ", 'false' ," + "1," + random.choice(rents) + ");")
    i+=1
i=1
while i<11:
    print(
        "INSERT INTO Apartment (address, apartment_number, is_vacant, number_of_rooms, suggested_monthly_rent) VALUES (" +
        addresses[2] + "," +str(i)+ ", 'false' ," + "1," + random.choice(rents) + ");")
    i+=1
i=1
while i<13:
    print(
        "INSERT INTO Apartment (address, apartment_number, is_vacant, number_of_rooms, suggested_monthly_rent) VALUES (" +
        addresses[3] + "," +str(i)+ ", 'false' ," + "1," + random.choice(rents) + ");")
    i+=1
i=1
while i<7:
    print(
        "INSERT INTO Apartment (address, apartment_number, is_vacant, number_of_rooms, suggested_monthly_rent) VALUES (" +
        addresses[4] + "," +str(i)+ ", 'false' ," + "1," + random.choice(rents) + ");")
    i+=1
i=1
while i<3:
    print(
        "INSERT INTO Apartment (address, apartment_number, is_vacant, number_of_rooms, suggested_monthly_rent) VALUES (" +
        addresses[5] + "," +str(i)+ ", 'false' ," + "1," + random.choice(rents) + ");")
    i+=1
