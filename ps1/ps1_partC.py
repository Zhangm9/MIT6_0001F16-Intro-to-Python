# Problem Set 1_ Part C: Finding the right amount to save away
# Name: MY Zhang

def cal_payment():
    '''
    To find out the best saving rate for you to pay for a 1M dollars house in 36 months
    '''
    base_annual_salary = int(input("Enter your starting salary: "))
    total_cost = 1000000 # int(input("Enter the total cost of your dream house: "))  # 1000000
    semi_annual_raise = 0.07 # float(input("Enter your semi-annual raise rate: ")) # 0.07
    months = 36  #int(input("How many months do you want to spend to save for the house?: ")) # 36
    
    portion_down_payment = 0.25
    r = 0.04 #investment annual return
    down_payment = total_cost * portion_down_payment
    current_savings = 0
    
    # acceptable error
    error = 100
    
    # set the starting and ending indexes
    bisection = 0
    initial_high = 10000
    low = 0
    high = initial_high
    portion_saved = (low + high) // 2
    
    # use bisection search to find the solution
    while abs(current_savings - down_payment) > error:
       bisection += 1
       current_savings = 0
       annual_salary = base_annual_salary
       
       for months in range(1, months + 1):
           current_savings = current_savings * ( 1+ r/12) + (annual_salary/12)* portion_saved/10000
           
           if months % 6 == 0: 
              annual_salary *= 1 + semi_annual_raise
       
       prev_portion_saved = portion_saved
       
           
       if current_savings > down_payment:
           high = portion_saved
       else:
           low = portion_saved
       portion_saved = int(round((high + low)/2))
       
       # if portion_saved is no longer changing, the searching space is not changing
       # because the search value id outside the range 1-10000
       # so stop the loop
       if prev_portion_saved == portion_saved:
           break
    
   
    if prev_portion_saved == portion_saved and portion_saved == initial_high:
        print('It is not possible to pay the down payment in three years.')
    else:
        print('Best savings rate:'+ str(portion_saved/10000))
        print('Steps in bisection search:'+ str(bisection))
           
cal_payment()