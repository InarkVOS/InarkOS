def writetoimg(file,msg):
    with open(file,'ab') as f:
        f.write(bytes(msg,'UTF-8'))
def readfromimg(file):
    with open(file,'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))

        f.seek(offset + 2)
        print(f.read())