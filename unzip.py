import sys

try:
    filename = sys.argv[1]
    fread = open(filename)
except:
    print("File not found!")
    quit()
    
fwrite = open("Original.txt","w")

text0=fread.read()
text1=text0.replace("Q","Qu").replace("q","qu").replace(".",".  ").replace(",",", ").replace("&","and")

fwrite.write(text1)

print("Original file:",text1)
print("1 File created:Original.txt")
print("Length of compressed text  :",len(text0))
print("Length of original text:",len(text1))
fread.close()
fwrite.close()