'''
Program Name: User Login System 
Author: Henoc Cherestal 
Purpose: Simulate a user login system using a dictionary of usernames and passwords, 
validate the username, and display security level on login. (BONUS CHALLENGE: Limit to 3 incorrect attempts) 
'''

from typing import Dict, Optional 

def build_user_db() -> Dict[str, str]: 
    """Build my dictionary using provided here, it has to return a dict of usernames+passwords""" 
    return{
        "guest": "guest",
        "andywood": "pythonpro!!",
        "hcherestal": "$hootforan_@!",
        "challenge": "@ccepted!",
    }

def what_security_level(username: str) -> str: 
    """Security level based on username, build logic statements"""
    if username == "guest": 
        return "Guest Access"
    return "Security Level 1" 

def check_password(users: Dict[str, str], username: str, max_attempts: int = 3) -> bool: 
    """This has to to ask for the user's password up to 3 or max_attempts times. 
    Return True if password is right, otherwise false. 
    """

    correct_password: str = users[username]

    for attempt in range (1, max_attempts + 1):
        password: str = input("Please enter your password: ").strip()

        if password == correct_password:
            return True
    
        if attempt < max_attempts: 
            print("Access Denied")
            print(f"Try again ({max_attempts - attempt} attempts(s) left).")

    return False 

