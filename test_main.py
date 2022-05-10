import main as mn
import pytest

def test_cleaner():
    assert (mn.cleaner({'text':'A*B(C)D#E%F^'})['clean_str']=='A_B_C_D_E_F_')
    assert (mn.cleaner({'text':'ABCDE'})['clean_str']=='ABCDE')
    assert (mn.cleaner({'text':'ABC123'})['clean_str']=='ABC123')
    assert (mn.cleaner({'text':'_123___'})['clean_str']=='_123___')
    assert (mn.cleaner({'text':'---'})['clean_str']=='_'*3)
    assert (mn.cleaner({'text':'%$^&*'})['clean_str']=='_'*5)
