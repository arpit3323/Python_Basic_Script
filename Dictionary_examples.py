crew_details={
              "Pilot":"Kumar",
              "C-Pilot":"Raghav",
              "Head-Strewardess":"Malini",
              "Stewardress":"Mal"

            }
print(dict(crew_details))

print("\n Iterating the dictionary using items functions")
for key,value in crew_details.items():
    print(key,":",value)

print("\nIterating the dictionary using keyword 'n'")
for key in crew_details:
    if(key=="Pilot" or key=="Co-Pilot"):
        print(crew_details[key])


crew_details["Pilot"]="James"
print("\nAfter modifying the value of Pilot:",crew_details["Pilot"])
      
crew_details.update({"Flight Attendant":"Jane", "Co-pilot":"Henry"})

print("\nAfter update:")
print("Co-pilot:",crew_details.get("Co-pilot"))
print("Flight Attendant:",crew_details["Flight Attendant"])
