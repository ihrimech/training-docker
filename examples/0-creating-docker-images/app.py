import sys

if len(sys.argv) < 2:
   print("Manque un argument numerique, veuillez renseigner le nombre de termes de la suite de Fibonacci a afficher")
   sys.exit(1)
# Program to display the Fibonacci sequence up to n-th term
nterms = int(sys.argv[1])

# first two terms
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")

elif nterms == 1:
   print("Fibonacci sequence upto", nterms, ":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1