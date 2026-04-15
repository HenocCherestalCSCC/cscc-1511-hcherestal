''' 
Program: test_rotation_utils.py
Author: Henoc Cherestal
Date: 04/14/2026
Purpose: This file tests the adjust_rotation() function from rotation_utils.py
         using pytest. It checks positive values, negative values, wrapped
         values, and invalid input.
Starter Code: Uses the provided rotation_utils.py file from class/lab starter code.
'''

import pytest
from rotation_utils import adjust_rotation

def test_adjust_rotation_100() -> None:
    '''Test that 100 stays 100.'''
    assert adjust_rotation(100) == 100


def test_adjust_rotation_460() -> None:
    '''Test that 460 wraps to 100.'''
    assert adjust_rotation(460) == 100 

def test_adjust_rotation_820() -> None:
    '''Test that 820 wraps to 100.'''
    assert adjust_rotation(820) == 100


def test_adjust_rotation_negative_100() -> None:
    '''Test that -100 wraps to 260.'''
    assert adjust_rotation(-100) == 260

def test_adjust_rotation_negative_460() -> None:
    """Test that -460 wraps to 260."""
    assert adjust_rotation(-460) == 260


def test_adjust_rotation_negative_820() -> None:
    """Test that -820 wraps to 260."""
    assert adjust_rotation(-820) == 260



