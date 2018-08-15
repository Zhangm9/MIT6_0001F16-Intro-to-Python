# Problem Set 1_ Part B: Saving, with a raise
# Name: MY Zhang


def cal_payment():
    base_annual_salary = int(input("Enter your starting salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = int(input("Enter the total cost of your dream house: ")) 
    semi_annual_raise = float(input("Enter your semi-annual raise rate, as a decimal: ")) 

    portion_down_payment = 0.25
    r = 0.04 #investment annual return
    down_payment = total_cost * portion_down_payment

    
    current_savings = 0
    months = 0
    annual_salary = base_annual_salary
  
    while current_savings < down_payment:       
    
        current_savings = current_savings * (1+ r/12) + (annual_salary/12) * portion_saved
        months += 1
           
        if months % 6 == 0: 
            annual_salary *= 1 + semi_annual_raise
            
              
    print("Number of months:"+ str(months))
           
cal_payment()