# Problem Set 1_ Part A: House Hunting
# Name: MY Zhang

def cal_payment():
    annual_salary = int(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save: "))
    total_cost = int(input("Enter the total cost of your dream house: ")) 

    portion_down_payment = 0.25
    r = 0.04 #investment annual return
    down_payment = total_cost * portion_down_payment
    monthly_salary = annual_salary/12
    current_savings = 0

    months = 0

    while current_savings < down_payment:
       
          current_savings = current_savings * (1+ r/12) + monthly_salary * portion_saved
          months += 1
       
    print("Number of months:"+ str(months))
           
cal_payment()