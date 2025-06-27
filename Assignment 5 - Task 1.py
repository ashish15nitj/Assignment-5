
my_dict = {'Alice':85, 'Ben':10, 'Charlie':56}
a = input("Enter the student's name: ")
if a in my_dict:
    print("{}'s marks: {}".format(a,my_dict[a]))
else:
    print('Student not found.')


