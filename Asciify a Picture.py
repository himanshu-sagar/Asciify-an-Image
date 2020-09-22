from PIL import Image ,ImageDraw,ImageFont
import math
import cv2 

chars="!@#$%^&*()QWERTYUIOPASDFGHJKLMNZBXCVhsjdhdhdyeteendhdkwtquwiei,<>?{}[]:-+.*/"[::-1]
#chars="!@#$%^&*()qwertyuioplkjhgfdsazxcvDFDDGFGFFHRDWWRTYHDDGMBCXZAQWERTIP_+=/*-+.:{}[]|"
charArray=list(chars)
charLength=len(charArray)
interval=charLength/256

scalefactor=0.1
charwidth=15
charheight=15

def getChar(input1):
    return charArray[math.floor(input1*interval)]

def asciifyImage(ImageFile):
    text_file=open('outputAscii.txt','w')
    image=Image.open(ImageFile)
    fontoutput=ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf",15)
    
    width,height=image.size
    image.resize((int(scalefactor*width),int(scalefactor*height*(charwidth/charheight))),Image.NEAREST)
    width,height=image.size
    pixel=image.load()
    
    outputimage=Image.new('RGB',(charwidth*width,charheight*height),color=(0,0,0))
    drawing=ImageDraw.Draw(outputimage)
    for i in range(height):
        for j in range(width):
            r,g,b=pixel[j,i]
            h=int((r+g+b)/3)
            pixel[j,i]=(h,h,h)
            text_file.write(getChar(h))
            drawing.text((j*charwidth,i*charheight),getChar(h),font=fontoutput,fill=(r,g,b))
        text_file.write('\n')
    outputimage.save('F:\\My Edited Images\\yuvia2.jpg')
    
asciifyImage("F:\\My Edited Images\\yuvia.jpg")
