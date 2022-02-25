#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Alice RSA data
Pa = 2**107 - 1
Qa = 2**607 - 1
Na = Pa*Qa
phi_Na = (Pa - 1)*(Qa - 1)
Ea = 101
Da = inverse_mod(Ea, phi_Na)
# Bob RSA data
Pb = 2**521 - 1
Qb = 2**127 - 1
Nb = Pb*Qb
phi_Nb = (Pb - 1)*(Qb - 1)
Eb = 173
Db = inverse_mod(Eb, phi_Nb)
M = "SUE IS TAKING A MIDTERM AND TRYING HARD TO ACE IT"
print(Db)


def encode_message(message):
    encoded_message = 0
    for char in message: encoded_message = 100*encoded_message + ord(char)
    return encoded_message
print(encode_message(M))



encoded_message = encode_message(M)
print(encoded_message)
cipher_text = power_mod(encoded_message, Eb, Nb)
print(cipher_text)



def rsa_create_signature(message_plaintext, key_sender_modulus, key_sender_private):
    
    # your code here
    # return digigal signature (instead of -1)
    return power_mod(message_plaintext,key_sender_private,key_sender_modulus)


# practice using a hash with the signature
import hashlib

hash = hashlib.sha256()
hash.update(M.encode('UTF-8'))

# create a string of hash
hash = hash.hexdigest()

# create an int of a hex; use this int with power_mod
hash_int = int(hash, 16)
print(hash_int)



alice_signature = rsa_create_signature(hash_int, Na, int(Da))
print(f"\n{alice_signature}")





