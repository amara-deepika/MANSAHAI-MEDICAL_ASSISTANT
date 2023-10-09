##expiry date detection
# import the following libraries
# will convert the image to text string
import pytesseract      
# adds image processing capabilities
from PIL import Image    
 # converts the text to speech  
import pyttsx3            
#translates into the mentioned language
from googletrans import Translator       
 # opening an image from the source path
img = Image.open('exp.jpeg')     
# describes image format in the output
print(img)                          
# path where the tesseract module is installed
pytesseract.pytesseract.tesseract_cmd =r'C:\Users\admin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)
result=result.strip()
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="XXXXXXXXXXXXXX@1",database="mansahaidatabase")
mycursor=mydb.cursor()
mycursor.execute("select * from batchno where batchno ='%s'"%(result))
x=mycursor.fetchall()
for i in x:
    print("%5s"% i[0],"%19s"% i[1],"%15s"% i[2],"%15s"% i[3],"%15s"% i[4],"%15s"% i[5])

