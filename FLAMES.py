myName=list(input("Enter your name"))
crushName=list(input("Enter your crush name"))
for mN in myName:
    for cN in crushName:
        if mN== cN:
            crushName.remove(cN)
            myName.remove(mN)
        else:
            pass
print(myName)
print(crushName)
balMyName=len(myName)
balCrushName=len(crushName)
total=balMyName+balCrushName
flames=['Friend','Love','Affection','Marriage','Enemy','Sister']
while len(flames)>1:
    split=(total % len(flames)-1)
    if split>=0:
        right=flames[split+1:]
        left=flames[:split]
        flames=right+left
    else:
        flames=flames[:len(flames)-1]
print("FLAMES :" ,flames[0])


