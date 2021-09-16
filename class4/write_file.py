'''
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    for i in range(5):
        file_object.write("I love programming.\n")
'''
'''
10-5. Programming Poll: Write a while loop that asks people why they like programming. 
Each time someone enters a reason, add their reason to a file that stores all the responses.
'''
# while loops
# input()
# writing to a file

#response_filename = input('Where would you like to store your responses? ')
# response_filename = 'mythoughts.txt'
# with open(response_filename, 'a') as f:
#     while True:
#         reason = input('Why do you like programming? ')
#         if reason == 'quit':
#             break
#         f.write(f'{reason}\n')

response_filename = 'mythoughts.txt'
with open(response_filename, 'a') as f:
    reason = input('Why do you like programming? ')
    while reason != 'quit':
        f.write(f'{reason}\n')
        reason = input('Why do you like programming? ')

# exit the program by typing 'quit'
