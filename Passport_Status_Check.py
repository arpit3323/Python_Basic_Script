

def passport_check(passport_no):
    
    if(len(passport_no)==8):
        if(passport_no[0]>="A" and passport_no[0]<="Z"):
            status="valid"
        else:
            status="invalid"
    else:
        status= "invalid"
    return status

passport_status=passport_check("M9993471")
print("Passport is",passport_status)
