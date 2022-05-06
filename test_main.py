import main as mn
import pytest

def test_cleaner():
    assert (mn.cleaner({'text':'A*B(C)D#E%F^'})=='A_B_C_D_E_F_')
    assert (mn.cleaner({'text':'ABCDE'})=='ABCDE')
    assert (mn.cleaner({'text':'%$^&*'})=='_'*5)
    assert (mn.cleaner({'text':'%$^&*'})=='does not match')
