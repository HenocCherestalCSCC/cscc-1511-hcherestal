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
        "admin": "Admin#2026",
    }

def what_security_level(username: str) -> str: 
    """Security level based on username, build logic statements"""
    if username == "guest": 
        return "Guest Access"
    return "Security Level 1" 

