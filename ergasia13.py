#για την 13 θα πρεπει να αφερέσω οτι δεν ειναι λατινικα γράμματα
f=open('two_cities_ascii.txt','r')
#x=f.readline()
y=[]
for x in f:
    x=x.replace("\n"," ")
    x=x.replace("*","")
    x=x.replace("-"," ")
    x=x.replace("0","")
    x=x.replace("1","")
    x=x.replace("2","")
    x=x.replace("3","")
    x=x.replace("3","")
    x=x.replace("3","")
    x=x.replace("4","")
    x=x.replace("5","")
    x=x.replace("6","")
    x=x.replace("7","")
    x=x.replace("8","")
    x=x.replace("9","")
    x=x.replace("(","")
    x=x.replace(")","")
    x=x.replace("[","")
    x=x.replace("]","")
    x=x.replace("{","")
    x=x.replace("}","")
    x=x.replace(".","")
    x=x.replace(",","")
    x=x.replace("?","")
    x=x.replace(";","")
    x=x.replace("!","")
    x=x.replace("#","")
    x=x.replace(":","")
    x=x.replace("'","")
    x=x.replace('"',"")
    x=x.replace("/","")
    x=x.replace("_","")
    x=x.replace("=","")
    x=x.replace("+","")
    x=x.replace("&","")
    x=x.replace("%","")
    x=x.replace("$","")
    x=x.replace(">","")
    x=x.replace("<","")
    x=x.replace("«","")
    x=x.replace("»","")
    y.append(x.split(" "))
f.close()
one=[]
two=[]
three=[]
four=[]
five=[]
six=[]
seven=[]
eight=[]
nine=[]
ten=[]
eleven=[]
twelve=[]
thirteen=[]
fourteen=[]
fifteen=[]
sixteen=[]
seventeen=[]
eighteen=[]
nineteen=[]
twenty=[]
for j in range(len(y)):
    for i in range(len(y[j])):
        if len(y[j][i])==1 :
            one.append(y[j][i])
        elif len((y[j][i]))==2 :
            two.append(y[j][i])
        elif len(y[j][i])==3 :
            three.append(y[j][i])
        elif len(y[j][i])==4 :
            four.append(y[j][i])
        elif len(y[j][i])==5 :
            five.append(y[j][i])
        elif len(y[j][i])==6 :
            six.append(y[j][i])
        elif len(y[j][i])==7 :
            seven.append(y[j][i])
        elif len(y[j][i])==8 :
            eight.append(y[j][i])
        elif len(y[j][i])==9 :
            nine.append(y[j][i])
        elif len(y[j][i])==10 :
            ten.append(y[j][i])
        elif len(y[j][i])==11 :
            eleven.append(y[j][i])
        elif len(y[j][i])==12 :
            twelve.append(y[j][i])
        elif len(y[j][i])==13 :
            thirteen.append(y[j][i])
        elif len(y[j][i])==14 :
            fourteen.append(y[j][i])
        elif len(y[j][i])==15 :
            fifteen.append(y[j][i])
        elif len(y[j][i])==16 :
            sixteen.append(y[j][i])
        elif len(y[j][i])==17 :
            seventeen.append(y[j][i])
        elif len(y[j][i])==18 :
            eighteen.append(y[j][i])
        elif len(y[j][i])==19 :
            nineteen.append(y[j][i])
        elif len(y[j][i])==20 :
            twenty.append(y[j][i])

while len(twenty) != 0 :
    twenty.pop()
while len(one) != 0 and len(nineteen) != 0 :
    one.pop()
    nineteen.pop()
while len(two) != 0 and len(eighteen) != 0 :
    two.pop()
    eighteen.pop()
while len(three) != 0 and len(seventeen) != 0 :
    three.pop()
    seventeen.pop()
while len(four) != 0 and len(sixteen) != 0 :
    four.pop()
    sixteen.pop()
while len(five) != 0 and len(fifteen) != 0 :
    five.pop()
    fifteen.pop()
while len(six) != 0 and len(fourteen) != 0 :
    six.pop()
    fourteen.pop()
while len(seven) != 0 and len(thirteen) != 0 :
    seven.pop()
    thirteen.pop()
while len(eight) != 0 and len(twelve) != 0 :
    eight.pop()
    twelve.pop()
while len(nine) != 0 and len(eleven) != 0 :
    nine.pop()
    eleven.pop()
while len(ten) >1  :
    ten.pop()
    ten.pop()
print("ena ")
print(len(one))
print("duo ")
print(len(two))
print("tria ")
print(len(three))
print("tesera ")
print(len(four))
print("pente  ")
print(len(five))
print("eji ")
print(len(six))
print("efta ")
print(len(seven))
print("oxto ")
print(len(eight))
print("enia ")
print(len(nine))
print("deka ")
print(len(ten))
print("enteka")
print(len(eleven))
print("dodeka ")
print(len(twelve))
print("dekatria ")
print(len(thirteen))
print("dekatesera ")
print(len(fourteen))
print("dekapente ")
print(len(fifteen))
print("dekaeji ")
print(len(sixteen))
print("dekaepta ")
print(len(seventeen))
print("dekaoxto")
print(len(eighteen))
print("dekaenia")
print(len(nineteen))
print("eikosi ")
print(len(twenty))
