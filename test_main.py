import main as mn
import pytest

def test_cleaner():
    assert (mn.cleaner({'text':'A*B(C)D#E%F^'})=='A_B_C_D_E_F_')
    assert (mn.cleaner({'text':'ABCDE'})=='ABCDE')
    assert (mn.cleaner({'text':'ABC123'})=='ABC123')
    assert (mn.cleaner({'text':'_123___'})=='_123___')
    assert (mn.cleaner({'text':'---'})=='_'*3)
    assert (mn.cleaner({'text':'%$^&*'})=='_'*5)
