"""di={1:2,2:3}
with open('fileStore.py','w') as f:
    f.write("fileStore={}".format(str(di)))
    f.close()"""
"""
import pyautogui as p
p.FAILSAFE=False
p.click(583,101)
p.hotkey('ctrlleft','a')
p.typewrite('hello')
for n in range(10):
    p.click(683,100+n*20)
    p.typewrite("it worked!!")
    p.typewrite('\n')
    #p.hotkey('ctrlleft','v')
p.moveTo(0,0,3)
p.moveTo(500,500)"""
"""from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as p
driver=webdriver.Chrome(executable_path='/home/neil/Desktop/chromedriver')
driver.get('http:/python.org')
assert 'Python' in driver.title
print(driver.title)
p.click(808,264)
p.typewrite('windows\n')
driver.close()"""

from pytesseract import image_to_string
print(image_to_string('/home/neil/wordpress/output/output.jpg'))
    #for i in range(3):
    #    arr[arr[:,:,i]<100]=asarray(0)
    #    arr[arr[:,:,i]!=0]=asarray(255)
    #print(arr)
    
    #scipy.misc.imsave(arr,str(foldername)+"output.jpg")
   
    #img=imread(str(foldername)+"output.jpg")
    #return img
