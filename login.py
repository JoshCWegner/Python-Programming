import re

count_upper_case_password = 0;
count_lower_case_password = 0;
count_digits_in_password = 0;
user_password_check_for_special_characters = re.compile('[!@#$%^&*()_{}]')
check_file_for_existing_user = open("username_password_check.txt", "r")

# check for username / password is existing
# figure out new user
# if password does not match loop back up
# save username and password to text file

username_from_user = input("enter in your username  or if you are a new user type in new user and hit enter: ")

if username_from_user in 'new user':
    password_from_user = input("password: ")
    password_verification_from_user = input("reenter password: ")
    print(password_from_user);
    print(password_verification_from_user);

    for i in password_from_user:
        if i.isupper() == True:
            count_upper_case_password += 1
        if i.islower() == True:
            count_lower_case_password += 1
        if i.isdigit() == True:
            count_digits_in_password += 1;

    print("count_upper_case_password: " + str(count_upper_case_password));
    print("count_lower_case_password: " + str(count_lower_case_password));
    print("count_digits_in_password: " + str(count_digits_in_password));

    if password_from_user == password_verification_from_user and (user_password_check_for_special_characters.search(
    password_from_user) != None) and count_upper_case_password >= 1 and count_lower_case_password >= 1 and count_digits_in_password >= 1:
        print("YES");
    else:
        print("NO");
else:
    print("no");

# password_from_user = input("password: ")
# if password_from_user == check_file_for_existing_user and   #username_from_user == check_file_for_existing_user:
# print("Welcome " + username_from_user);
