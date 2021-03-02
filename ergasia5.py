import random
numbers=False
#αρχικά ελέγχω τις τιμές που δίνει ο χρ΄ηστης
while not numbers:
    print ("δόστε τις διαστάσεις για τον ορθογώνιο πίνακα")
    a=input("το πλάτος είναι :")
    b=input("το ύψος είναι :")
    try:
        x=int(a)
        y=int(b)
        size=x*y
        if x>=3 and y>0 and x != y:
            numbers=True
            #έλεγχος για τα 's' και 'o' για να είναι ίσα στο πλήθος
            def chek(w,z):
                r1=w.count("s")
                r2=w.count("o")
                for i in range(z):
                    if r1>r2:
                        w=w.replace("s","o",1)
                        r1=w.count("s")
                        r2=w.count("o")
                    elif r2>r1:
                        w=w.replace("o","s",1)
                        r1=w.count("s")
                        r2=w.count("o")
                    else:
                        r1=w.count("s")
                        r2=w.count("o")
                k=w.split()
                return k

            total_score=[]
            for f in range(10):
                #δημιουργία του πίνακα
                a=" "
                for p in range(size):
                    grammata=["s","o"]
                    random.shuffle(grammata)
                    a=a+" "+grammata[0]+" "
                l=chek(a,x)

                score1=0

                #οριζόντιος έλεγχος για sos
                for i in range(y):
                    for j in range(x-2):
                        if l[j+(i*x)]=="s" and l[j+(i*x)+1]=="o" and l[j+(i*x)+2]=="s":
                            score1=score1+1
                        else:
                            score1=score1

                #κάθετος έλεγχος για sos
                for j in range(x*y-2*x):
                    if l[j]=="s" and l[j+x]=="o" and l[j+2*x]=="s":
                        score1=score1+1
                    else:
                        score1=score1

                #διαγώνια προς τα δεξιά έλεγχος για sos
                for i in range(y-2):
                    for j in range(x-2):
                        if l[j+(i*x)]=="s" and l[j+(i*x)+(x+1)]=="o" and l[j+(i*x)+2*(x+1)]=="s":
                            score1=score1+1
                        else:
                            score1=score1

                #διαγώνια προς τα αριστερά έλεγχος για sos
                for i in range(y-2):
                    for j in range(x-2):
                        if l[(i*x)+(x-1)-j]=="s" and l[(i*x)+2*(x-1)-j]=="o" and l[(i*x)+3*(x-1)-j]=="s":
                            score1=score1+1
                        else:
                            score1=score1

                #αποθήκευση του score
                total_score.append(score1)
            #υπολογισμός και εκτύπωση το μέσου όρου απο τα score
            t=sum(total_score)
            l=len(total_score)
            average=t/l
            print("\nο μέσος όρος απο sos σε καθε γύρο είναι : ")
            print(average)
        elif x==y and x>=3 and y>0:
            print("παρακαλώ δώστε πλάτος και ύψος ώστε να βγαίνει ο πίνακας ορθογώνιος\n")
        elif x>=3:
            print("παρακαλώ δώστε ύψος μεγαλύτερο απο το 0 !\n")
        elif y>0:
            print("παρακαλώ δώστε πλάτος μεγαλύτερο ή ισο του 3 !\n")
        else:
            print ("παρακαλώ δώστε πλάτος μεγαλύτερο ή ισο του 3 και ύψος μεγαλύτερο απο το 0 !!!\n")
    except:
        print ("παρακαλώ δώστε μόνο αριθμούς !!!\n")
