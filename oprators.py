#num=int(input("enter number"))#
#if num%2==0:#
 #   print("even number")#
#else:
     #   print("odd number")
#age =int(input("enter your age"))
#if age>=18:
 #       print("Eligible for voting")
#else:
 #           print("not eligible")
#username=input("enter username")
#password=input("enter password")
#if username=="admin" and password == "1234":
 #   print("login successful")
#else:
 #   print("login failed")
amount=int(input("enter amount"))
if amount>=500:
    discount=amount *10/100
    print("final amount",amount-discount)
elif amount<=1000:
    discount=amount *15/100
    print("final pese",amount-discount)
else:
    print("final amount",amount)
