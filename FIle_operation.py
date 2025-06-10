guests = open("guests_list.txt",'w')
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]
new_guests = ["Sam", "Danielle", "Jacob"]
checked_out=["Andrea", "Manuel", "Khalid"]
guests_to_check = ['Bob', 'Andrea']
temp_list = []
checked_in = []
for i in initial_guests:
    guests.write(i + '\n')

guests.close()

with open("guests_list.txt",'a') as guests:
      for i in new_guests:
          guests.write(i+'\n')

with open("guests_list.txt") as guests:
     for i in guests:
         temp_list.append(i.strip())

with open("guests_list.txt",'w') as guests:
     for i in temp_list:
         if i not in checked_out:
             guests.write(i +'\n')

with open("guests_list.txt") as guests:
    for line in guests:
        print(line)

with open("guests_list.txt") as guests:
    for i in guests:
        checked_in.append(i)
    for check in guests_to_check:
        if check in checked_in:
            print(f"{check} is checked in")
        else:
            print(f"{check} is not checked in")