# comparison operators are important for logic building
# comparison operators return a boolean
# some important comparision operators
n1 = 10
n2 = 77
# greater than (x > y)
n1_is_greater_than_n2 = n1 > n2
print(n1_is_greater_than_n2)
# less than (x < y)
print(n1 < n2)
# less than or equal to (x <= y)
print(n1 <= n2)
# greater than or equal to (x >= y)
print(n1 >= n2)
# not equal to (x != y)
print(77 != 22)
# equal to (x == y)
print(2323 == 2323)

# comparision operators are very very important in programming.
# make sure you understand them and practice them

password = input("Password:")

correct_pass = "123456"

if correct_pass == password:
  print("correct password!")
else :
  print("Wrong password!")
