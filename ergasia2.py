import random
number=False
while not number:
    t=input("δόστε ποιόν όρο της ακολουθίας φιμπονάτσι θέλεται : ")
    #έλεγχος για τις τιμές που δίνει ο χρήστης
    try:
        t=int(t)
        if t>0:
            #υπολογισμός του αριθμού με την συνάρτηση φιμπονάτσι
            def fibo2(x):
                i=1
                j=1
                for k in range(x-2):
                    tmp =i
                    i=i+j
                    j=tmp
                return i
            number=True
            g=fibo2(t)
            chek=[]
            #επιλογή των 20 τυχαίων αριθμών
            for e in range(20):
                a=random.randrange(g)
                b=pow(a,g,g)
                if b==a:
                    chek.append("1")
                else:
                    chek.append("0")
                    break
            print("\n")
            #έλεγχος για τον αν ο αριθμός ειναι πρώτος
            z=chek.count("1")
            if z==20:
                print("ο αριθμός ειναι πρωτος")
            else:
                print("ο αριθμός δεν ειναι πρωτος")
        else:
            print ("παρακαλώ δώστε αριθμό μεγαλύτερο από το 0 !\n")
    except:
        print ("παρακαλώ δώστε μόνο αριθμούς !!!\n")
