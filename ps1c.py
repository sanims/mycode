#program that calculate a approriate time ot take to save upto 1m in 36 month using Bisection and guess
annual_salary = float(input("Enter your annual salary: "))
#portion saved
portion_saved = float(input("Enter the percent of your salary to save, in decimal: "))
total_cost = float(1000000)
# semi annual raise incrsement....
semi_annual_raise = float(0.7)
#to get the portion down payment 
portion_down_payment = total_cost * 0.25
#initializing the current saving getting a return value from monthly salary X by portion saved plus value of current+
current_savings = 0
r = 0.04
months = 36
while current_savings < portion_down_payment:
    months += 1
    if months%6 == 0:
        annual_salary += annual_salary * semi_annual_raise
#apropriate time variable
p_time=total_cost
semi_annual_raise=0.7
r=0
portion_down_payment=0
guess=(p_time+r) /2.0
while abs (guess**3-p_time) >=semi_annual_raise:
	if guess**3 < p_time:
		r=p_time
else:
	portion_down_payment=p_time
portion_down_payment=(guess-p_time)/2.0
guess (r + portion_down_payment) /2.0
current_savings += (annual_salary/12)*portion_saved + current_savings*(r/12)
print (current_saving,"best saving rate:",)
print (guess,"Steps in Bisection search is :",)