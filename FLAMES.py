myName=input("Enter your name")
crushName=input("Enter your crush name")
mn_copy=myName
cn_copy=crushName
for i in myName:
    cn_copy=cn_copy.replace(i,'',1)
for i in crushName:
    mn_copy=mn_copy.replace(i,'',1)
# print(mn_copy) balance characters
# print(cn_copy) balance characters
balMyName=len(mn_copy)
balCrushName=len(cn_copy)
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
