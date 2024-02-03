ticket_status="Confirmed"
luggage_weight=42
luggage_limit=30
extra_luggage_charge=0
if(ticket_status=="Confirmed"):
    if(luggage_weight>0 and (luggage_weight<=luggage_limit)):
        print("Checked in Cleared")
    elif(luggage_weight<=(luggage_limit+10)):
            extra_luggage_charge=300*(luggage_weight-luggage_limit)
    else:
        extra_luggage_charge=500*(luggage_weight-luggage_limit)
    if(extra_luggage_charge>0):
        print("Extra Luggage charge is",extra_luggage_charge)
        print("please make the payment to clear check in")
else:
    print("sorry, ticket is not confirmed")
    
