try:
    samplefile=open('sample.txt','r') 
    readfile=samplefile.read()
    print(readfile)
    samplefile.close
    
except FileNotFoundError:
    print('ERROR:The file sample.txt not found')
    





  