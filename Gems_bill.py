def Calculate_bill_amount(gem_list,price_list,reqd_gems,reqd_quantity):
    bill_amount=0

    for gem in reqd_gems:
        if gem in gem_list:
            i1=gem_list.index(gem)
            i2=reqd_gems.index(gem)
            bill_amount=bill_amount+(reqd_quantity[i2]*price_list[i1])
            if bill_amount>30000:
                bill_amount=bill_amount- ((bill_amount*5)/100)
        else:
            return -1
    return bill_amounnt

gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

price_list=[1760,2119,1599,3920,3999]

reqd_gems=["Ivory","Emed","Garnet"]

reqd_quantity=[3,10,12]

bill_amount=Calculate_bill_amount(gems_list,price_list,reqd_gems,reqd_quantity)
print(bill_amount)
