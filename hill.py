import numpy as np

def chr_to_int(char):
  char = char.upper()
  integer = ord(char) - 65
  return integer

def create_matrix_of_integers_from_string(string):
  integers = [chr_to_int(c) for c in string]
  length = len(integers)
  M = np.zeros((2, int(length / 2)), dtype=np.int32)
  iterator = 0
  for column in range(int(length / 2)):
    for row in range(2):
      M[row][column] = integers[iterator]
      iterator += 1
  return M

def find_multiplicative_inverse(determinant):
  multiplicative_inverse = -1
  for i in range(26):
    inverse = determinant * i
    if inverse % 26 == 1:
      multiplicative_inverse = i
      break
  return multiplicative_inverse

def make_key():
  determinant = 0
  C = None
  while True:
    cipher = input("Input 4 letter cipher: ")
    C = create_matrix_of_integers_from_string(cipher)
    determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
    determinant = determinant % 26
    inverse_element = find_multiplicative_inverse(determinant)
    if inverse_element == -1:
      print("Determinant is not relatively prime to 26, uninvertible key")
    elif np.amax(C) > 26 and np.amin(C) < 0:
      print("Only a-z characters are accepted")
      print(np.amax(C), np.amin(C))
    else:
      break
  return C

# Encryption

def encrypt(m):
  # remove all the spaces in the text
  m = m.replace(" ", "")
  # get the encryption matrix
  C = make_key()
  len_check = len(m) % 2 == 0
  if not len_check:
    m += "0"
  P = create_matrix_of_integers_from_string(m)
  m_len = int(len(m) / 2)
  print("message", P)
  en_m = ""
  for i in range(m_len):
    row_0 = P[0][i] * C[0][0] + P[1][i] * C[0][1]
    integer = int(row_0 % 26 + 65)
    en_m += chr(integer)
    row_1 = P[0][i] * C[1][0] + P[1][i] * C[1][1]
    integer = int(row_1 % 26 + 65)
    en_m += chr(integer)
  return en_m

m = input("Message: ")
en_m = encrypt(m)
print(en_m)


# Decryption

def decrypt(en_m):
  C = make_key()
  determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
  determinant = determinant % 26
  multiplicative_inverse = find_multiplicative_inverse(determinant)
  C_inverse = C
  C_inverse[0][0], C_inverse[1][1] = C_inverse[1, 1], C_inverse[0, 0]
  C[0][1] *= -1
  C[1][0] *= -1
  for row in range(2):
    for column in range(2):
      C_inverse[row][column] *= multiplicative_inverse
      C_inverse[row][column] = C_inverse[row][column] % 26
  P = create_matrix_of_integers_from_string(en_m)
  m_len = int(len(en_m) / 2)
  de_m = ""
  for i in range(m_len):
    column_0 = P[0][i] * C_inverse[0][0] + P[1][i] * C_inverse[0][1]
    integer = int(column_0 % 26 + 65)
    de_m += chr(integer)
    column_1 = P[0][i] * C_inverse[1][0] + P[1][i] * C_inverse[1][1]
    integer = int(column_1 % 26 + 65)
    de_m += chr(integer)
  if de_m[-1] == "0":
    de_m = de_m[:-1]
  return de_m

de_m = decrypt(en_m)
print(de_m)