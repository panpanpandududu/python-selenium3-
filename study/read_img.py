import sys
import os
base_path = os.getcwd()
from PIL import Image  #图片处理，生成验证码图片
import pytesseract   #识别图片验证码
from ShowapiRequest import ShowapiRequest  #提高文字识别率，当文字受干扰因素多时
image_path = base_path+'/imooc_selenium/image/imooc2.png'
img = Image.open(image_path)
text = pytesseract.image_to_string(img)

# r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5")
# r.addBodyPara("typeId","35")
# r.addBodyPara("convert_to_jpg","0")
# # 定义文件上传设置：
# r.addFilePara("image",image_path)
# res = r.post()
print(text) #返回信息