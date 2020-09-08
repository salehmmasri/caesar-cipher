from caesar_cipher.caesar_cipher import decrypt,encrypt
import random

def test_encryption():
    sent = 'The rain in Spain falls mainly on the plain.'
    expected = 'vjg tckp kp urckp hcnnu ockpna qp vjg rnckp.'
    assert encrypt(sent, 2) == expected

def test_decryption_known():
    encrypted = 'vjg tckp kp urckp hcnnu ockpna qp vjg rnckp.'
    expected = 'the rain in spain falls mainly on the plain.'
    assert decrypt(encrypted) == expected
