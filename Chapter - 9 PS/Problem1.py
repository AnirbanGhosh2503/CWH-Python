f = open("poem.txt")
content = f.read()
if("twinkle".lower() in content.lower()):
    print("The word 'twinkle' is present in the content")
else:
    print("The word 'twinkle' is not present in the content")
f.close()