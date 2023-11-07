# Question 16(a)
# Name and School

cardNum=7200828282828210

print(cardNum)


cardstr = str(input("Welcome to CardCheak. Enter your card number:"))

card=list(cardstr)

x=0
while x < 1:
    if int(card[0])== 7 and len(card) >= 16:
        print("that is correct")
        print("This is a ZinCard")
        x += 1
    elif int(card[0]) == 8 and len(card) >= 16:
        print("that is correct")
        print("This is a WindCard")
        x += 1
    else:
        print("That is incoorrect, please try again:" + cardstr)
        x += 1
date = str(input("Enter the card expiry date e.g. 11/26 should be entered as 1126:"))
    