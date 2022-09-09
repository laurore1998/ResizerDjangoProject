import PIL
from PIL import Image

def Resizer(file_path,nwidth,nheight):
    #file_path ="C:/Users/Nicodem LAURORE/OneDrive/Pictures/Capture.PNG"
    #file_path =""
    img = PIL.Image.open(file_path)
    myHeight, myWidth = img.size
    #nwidth=myWidth//4
    #nheight=myHeight//4
    #nwidth=0
    #nheight=0

    # img = img.resize((myHeight,myWidth), PIL.Image.ANTIALAS)
    #save_path = dial.asksaveasfilename()
    img = img.resize((nheight,nwidth))
    file_path1 = file_path.split("/")
    file_path=file_path.split(".")
    i = file_path1[0:-1]
    a = "/".join(i) + '/'
    #save_path ="C:/Users/Nicodem LAURORE/OneDrive/Pictures/"
    save_path =a
    img.save(save_path + "ResiZer."+file_path[-1][0::])
    print(file_path[-1][0::]+" "+str(nwidth)+" "+str(nheight))

def Resizer2(file_path,nwidth,nheight):
    #file_path ="C:/Users/Nicodem LAURORE/OneDrive/Pictures/Capture.PNG"
    #file_path =""
    img = PIL.Image.open(file_path)
    myHeight, myWidth = img.size
    #nwidth=myWidth//4
    #nheight=myHeight//4
    #nwidth=0
    #nheight=0

    # img = img.resize((myHeight,myWidth), PIL.Image.ANTIALAS)
    #save_path = dial.asksaveasfilename()
    img = img.resize((nheight,nwidth))

    file_path=file_path.split(".")
    #save_path ="C:/Users/Nicodem LAURORE/OneDrive/Pictures/"
    img.save("ResiZer."+file_path[-1][0::])
    print(file_path[-1][0::]+" "+str(nwidth)+" "+str(nheight))
    return

def he():
    print("hello")

def Resizer2(file_path,nwidth,nheight):
    #file_path ="C:/Users/Nicodem LAURORE/OneDrive/Pictures/Capture.PNG"
    #file_path =""
    img = PIL.Image.open(file_path)
    myHeight, myWidth = img.size
    #nwidth=myWidth//4
    #nheight=myHeight//4
    #nwidth=0
    #nheight=0

    # img = img.resize((myHeight,myWidth), PIL.Image.ANTIALAS)
    #save_path = dial.asksaveasfilename()
    img = img.resize((nheight,nwidth))

    file_path=str(file_path).split(".")
    #save_path ="C:/Users/Nicodem LAURORE/OneDrive/Pictures/"
    nameExtension=file_path[0][0::]+"_ResiZer."+file_path[-1][0::]

    print(file_path[-1][0::]+" "+str(nwidth)+" "+str(nheight))
    return img.save(nameExtension)