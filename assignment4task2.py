data=input("Enter text to write to a file:")
file=open('output.txt','w')
writefile=file.write(data)
file.close

data1=input("Enter additional text to append :")
file=open('output.txt','a')
addfile=file.write(data1)
file.close

print("\nFinal content of output.txt:")
file=open('output.txt','r')
read=file.read()
print(read)



