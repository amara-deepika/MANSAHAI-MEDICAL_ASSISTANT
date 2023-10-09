print("welcome to mansahai")
def admin_profit():
    fin=open("profit_admin.txt","r")
    profit=0
    red=fin.read()
    rd=red.split()
    for i in rd:
        profit=profit+int(i)
    print("till now your profit is:",profit)
def register():
    import pickle
    import random
    fout=open("reg.txt","rb")
    d=pickle.load(fout)
    name_list=list(d.keys())
    user_email=input("enter your google account id")
    while True:
        user=input("enter user name")
        phone_no=input("enter phone no.")
        if user not in name_list:
            otp=random.randint(1000,9999)
            otp=str(otp)
            import smtplib
            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login("amarajaibhargav@gmail.com","xsao uzpk rnev gmqp")
            ans="hey this is a message from SOUL BEAT \n your otp is:"+str(otp)
            server.sendmail("amarajaibhargav@gmail.com",user_email,ans)
            server.quit()
            verification=input("enter your otp")
            if otp==verification:
                d[user]=phone_no
                print("your name has been registered")
            else:
                print("your otp is wrong")
            break
            
        else:
            print("sorry user name already taken! try something else!")
    fin=open("reg.txt","wb")
    pickle.dump(d,fin)
    fin.close()
def user():
    counter5=1
    import pickle
    check={}
    fin=open("reg.txt","rb")
    d=pickle.load(fin)
    user=input("enter user name")
    phone_no=input("enter phone no.")
    counter1=1
    if d[user]==phone_no:
        import mysql.connector
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="Omganapati@1",database="mansahaidatabase")
        mycursor=mydb.cursor()
        print("user matched")
        print("you are now ready to access")
        print("so,here you will be getting various details about different medicines,their reviews,its drug effect and their MRP ")
        print("1.details of a medicine")
        print("2. search for a medicine of which disease")
        a=int(input("choose your option"))
        if a==1:
            try:
                medicine=input("enter the name of the medicine for which you want know its details")
                mycursor.execute("select * from mansahai where medicine='%s'"%(medicine))
                x=mycursor.fetchall()
                print("%5s"%"medicine","%20s"%"disease","%15s"%"type","%10s"%"mrp")
                print("===============================================================================================")
                for i in x:
                    print("%5s"% i[0],"%19s"% i[1],"%15s"% i[2],"%15s"% i[3])
                    counter1=2
                
            except:
                print("there is no such medicine in this dictionary")
                counter1=2

        if a==2:
            print("you have choosed to search a medicine")
            print("1.fever")
            print("2.cold")
            print("3.cough")
            print("4.headache")
            print("5.joint pain")
            print("6.vitamin defficiency")
            print("7.calcium defficiency")
            print("8.rashes")
            print("9.skin allergry")
            dis=int(input(" choose which kind of disease"))
            print("%5s"%"medicine","%20s"%"disease","%15s"%"type","%10s"%"mrp")
            print("===============================================================================================")
            choices=[]
            if dis==1:
                mycursor.execute("select * from mansahai where disease ='fever'")
                x=mycursor.fetchall()
                for i in x:
                    print("%5s"% i[0],"%19s"% i[1],"%15s"% i[2],"%15s"% i[3])
                    choices.append(i[0])
            if dis == 2:
                mycursor.execute("select * from mansahai where disease ='cold'")
                x=mycursor.fetchall()
                for i in x:
                    print("%5s"% i[0],"%19s"% i[1],"%15s"% i[2],"%15s"% i[3])
                    choices.append(i[0])
            if dis ==3:
                mycursor.execute("select * from mansahai where disease ='cough'")
                x=mycursor.fetchall()
                for i in x:
                    print("%5s"% i[0],"%19s"% i[1],"%15s"% i[2],"%15s"% i[3])
                    choices.append(i[0])
            if dis == 4:
                mycursor.execute("select * from mansahai where disease ='headache'")
                x=mycursor.fetchall()
                for i in x:
                    print("%5s"% i[0],"%19s"% i[1],"%15s"% i[2],"%15s"% i[3])
                    choices.append(i[0])
            if dis ==5:
                mycursor.execute("select * from mansahai where disease ='jointpain'")
                x=mycursor.fetchall()
                for i in x:
                    print("%5s"% i[0],"%19s"% i[1],"%15s"% i[2],"%15s"% i[3])
                    choices.append(i[0])
            if dis ==6:
                mycursor.execute("select * from mansahai where disease ='vitamindeficiency'")
                x=mycursor.fetchall()
                for i in x:
                    print("%5s"% i[0],"%19s"% i[1],"%15s"% i[2],"%15s"% i[3])
                    choices.append(i[0])
            if dis ==7:
                mycursor.execute("select * from mansahai where disease ='calciumdeficiency'")
                x=mycursor.fetchall()
                for i in x:
                    print("%5s"% i[0],"%19s"% i[1],"%15s"% i[2],"%15s"% i[3])
                    choices.append(i[0])
            if dis ==8:
                mycursor.execute("select * from mansahai where disease ='rashes'")
                x=mycursor.fetchall()
                for i in x:
                    print("%5s"% i[0],"%19s"% i[1],"%15s"% i[2],"%15s"% i[3])
                    choices.append(i[0])
            if dis ==9:
                mycursor.execute("select * from mansahai where disease ='allergy'")
                x=mycursor.fetchall()
                for i in x:
                    print("%5s"% i[0],"%19s"% i[1],"%15s"% i[2],"%15s"% i[3])
                    choices.append(i[0])
            if dis>9 or dis<1 : 
                print("entered number  is invalid")
        if counter1==1:
            finl=open("reviews.txt","r")
            red=finl.readlines()
            print("reviews for your options:")
            counter2=1
            for i in choices:
                for j in red:
                    length=len(i)
                    if j[0:length]==i:
                        j.strip()
                        print(j)
                        counter2=counter2+1
            finl.close()
     
    else:
        print("unauthorised user name")
    
    fin.close()
    
def bill():
    sum1=0
    price=[]
    med=[]
    num=[]
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Omganapati@1",database="mansahaidatabase")
    mycursor=mydb.cursor()
    deff="yes"
    while deff.lower()=="yes":
            name=input("enter the name of the medicine")
            med.append(name)
            deff=input("wanna buy more?(yes/no)")
            if deff.lower()=="no":
                print("you have ordered the following items")
                print("%5s"%"medicine","%20s"%"disease","%15s"%"type","%10s"%"mrp")
                print("=================================================================================================")
                for i in med:
                    mycursor.execute("select * from mansahai where medicine = '%s'"%(i))
                    x=mycursor.fetchall()
                    for j in x:
                        print("%5s"% j[0],"%19s"% j[1],"%15s"% j[2],"%15s"% j[3])
                        price.append(j[3])
    d={}
    for i in med:
        j=0
        print("specify the quantity of ",i, "required")
        no=int(input("enter the quantity."))
        each_price=int(price[j])*int(no)
        d[i]=each_price
        each_price=0
        j=j+1
    amount=list(d.values())
    sumup=0
    for j in amount:
        sumup=sumup+j
    ##profit owned by user
    user_email=input("please input your email id so that we can send you your bill")
    import smtplib,json
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("amarajaibhargav@gmail.com","xsao uzpk rnev gmqp")
    bill=json.dumps(d,indent=4)
    up=(90/100)*int(sumup)
    saved=int(sumup)-int(up)
    saved=str(saved)
    up=str(up)
    sumup=str(sumup)
    bill=str(bill)
    complete_bill="this is an officail bill from mansahi"+bill+"you have to pay"+up+"&&"+"   you have saved:"+saved+"Rs"
    server.sendmail("amarajaibhargav@gmail.com",user_email,complete_bill)
    server.quit()
    ##not for user use:(what ever happens after this is not displayed to the user)
    fin=open("profit_admin.txt","a")
    ap=(75/100)*int(sumup)
    pro=int(sumup)-ap
    pro=int(pro)
    pro=str(pro)
    fin.write(pro+" ")
    fin.close()
def review():
    medname=input("enter the medicine name")
    l=len(medname)
    rev=input("type your review")
    fin1=open("reviews.txt","w")
    x=medname+"="+rev
    fin1.write(x)
    fin1.write("\n")
    fin1.close()
    print("thank you for providing your review ")
counter=1
while(counter==1):
    print("1.user")
    print("2.buy")
    print("3.register")
    print("4.write reviews")
    print("5.profit_admin")
    choice=int(input("enter your choice"))   
    if choice==1:
        user()
    elif choice==2:
        bill()
    elif choice==3:
        register()
    elif choice==4:
        review()
    elif choice==5:
        admin_profit()
    else:
        print("enter valid choice")
    counter=int(input("do you still want to continue [1/0]"))
if counter !=1:
    print("thank you for using MANSAHAI")
    

