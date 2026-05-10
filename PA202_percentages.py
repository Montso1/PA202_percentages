#Question1
original_price = float(input('Enter The Original Price :'))
discount_percent = float(input('Enter The Discounted percentage :'))

discount_amount = original_price * (discount_percent/100)
final_price = original_price - discount_amount

print(f'discount_amount : R{discount_amount :2f}')
print(f'final_price : R{final_price :2f}')

#Question2

user_marks = input('Enter Your Marks :')
total_marks = input('Enter Total Marks :')
if 75 <= user_marks <= 100 :
    print('Distinction')
elif 60 <= user_marks <=75 :
    print('Is Merit')
elif 50 <= user_marks <= 59 :
    print('Is Pass')
else :
    print('fail')

#Question3
current_salary =float(input('Enter Your Current Salary :'))
percentage_increase = float(input('Enter The Percentage Increase :'))

increase_percent = current_salary + (percentage_increase/100)
new_salary = increase_percent + current_salary
print(f'increase_percent : R{increase_percent :2f}')
print(f'new_salary : R{new_salary :2f}')

#Question4
cost_price = float(input('Enter Cost Price :'))
selling_price = float(input('Enter Selling Price :'))

profit = (profit // cost_price)*100
print(f'cost_price')