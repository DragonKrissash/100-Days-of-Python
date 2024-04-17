#Monthly salary for a given annual salary and tax
ann_sal=int(input("Enter the annual salary: "))
tax=int(input("Enter the tax rate: "))
month_sal=(ann_sal/12)*(1-tax/100)
print(f"The monthly salary is :{month_sal}")