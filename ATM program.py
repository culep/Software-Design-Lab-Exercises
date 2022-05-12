#PROJECT 4
#The ATM program allows a user an indefinite number of attempts to log in. 
#Fix the program so that it displays a popup message that the police will be 
#called after a user has had three successive failures. 
#The program should also disable the login button when this happens.


print("""
Welcome to ATM Machine
----------------------
""")
password=7744
PIN=""
password_attempt=1
is_password_lock= False

while PIN != password and not(is_password_lock):

    if password_attempt <= 3:
        PIN=int(input("Please enter your 4 digit PIN\n"))

    else:
        is_password_lock = True
    password_attempt = password_attempt + 1
    
if is_password_lock:
    print("""
    -------------------------------------------
    Dear customer, we've noticed an inadequate login attempt. 
    For the benefit of your safety and the community, we have
    made the decision to contact police about this incident.
    -------------------------------------------
    """)
else:
    print("Login is successful!")
    