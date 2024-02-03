boarding_call="Good Evening, this is the final call to AI passengers for the Flight AI 466 which is planned to take off at 8.40A.M"

if(boarding_call.startswith("Good Evening")):
   print(boarding_call.replace("Good Evening","Good Morning"))

if(boarding_call.find("AI"))>=0:
   print("Welcome to Air India.")

if(boarding_call.endswith("A.M.")):
   print("Passengers are requested to have their breakfast:")

a=boarding_call.split(" ")
for i in a:
   if(i.isdigit()):
      print("Flight Number is Specified to the message")

print("Total number of time flight service name is specified in the boarding call",boarding_call.count("AI"))


message="Thank you all .. Have a nice journey"

print(message.upper())
print(message.lower())
