medname=input("enter the medicine name")
l=len(medname)
rev=input("type your review")
fin1=open("reviews.txt","w")
x=medname+"="+rev
fin1.write(x)
fin1.write("\n")
fin1.close()
print("thank you for providing your review ")
