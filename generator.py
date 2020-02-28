import string
import random

table = "USERS"
attr = 'phone_number, name, password, email'

firstNames = []
lastNames = []
phoneNums = []

f = open('firstnames.txt', 'r')
firstNames = [line.rstrip('\n') for line in f]
f.close()
g=open('lastnames.txt', 'r')
lastNames = [line.rstrip('\n') for line in g]
g.close()
l = open("phoneNums.txt", "r")
phoneNums = [line.rstrip('\n') for line in l]
l.close()
roles = ["'JANITOR'", "'MAINTENANCE'", "'DOORMAN'", "'SECURITY'", "'FRONT DESK'"]
wages = ['12.50', '15.70', '18.10', '19.60', '20.30', '24.80', '13.40']
emailEnds = ["@gmail.com", '@yahoo.ca', '@hotmail.com','@outlook.com','@mail.mcgill.ca']
emailList = []

numRecs =120
j = 0

for i in range(numRecs):
    first = random.choice(firstNames)
    last = random.choice(lastNames)
    newEmail = "'"+ first.lower() + '.' + last.lower() + random.choice(emailEnds) + "'"
    if newEmail not in emailList:
        emailList.append(newEmail)
        password = "'" + ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=10)) + "'"
        name = "'" +  first + ' ' + last + "'"
        phone = "'" + random.choice(phoneNums)  + "'"
        if j<100:
            print("INSERT INTO " + table + "(" + attr + ") VALUES (" + phone + "," + name + "," + password + "," + newEmail + ");")
            if 0 <= j <= 5:
                print("INSERT INTO MANAGERS (email) VALUES (" + newEmail + ");")
            elif 5 < j <=25:
                print("INSERT INTO STAFF (role, wage, email) VALUES (" + random.choice(roles) + "," + random.choice(wages) + "," + newEmail + ");")
            else:
                print("INSERT INTO TENANTS (email) VALUES (" + newEmail + ");")
        else:
            print("INSERT INTO APPLICATION (" + attr + ") VALUES (" + phone + "," + name + "," + password + "," + newEmail + ");")
        j+=1
