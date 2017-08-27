
age = input('Please enter your age to find out if you are eligible to go on the holiday trip: ')
if 18 <= age <= 30:
    print('It must be your lucky day! You can go on the trip!')
elif age < 18:
    print('Sorry, but looks like you are too young to go on the trip. Maybe you can go in {0} years.'.format(18 - age))
else:
    print('Sorry, but it seems that you are too old for this trip. You could have gone {0} years earlier.'
          .format(age - 35))
