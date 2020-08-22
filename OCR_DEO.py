import keyboard
from PIL import ImageGrab
from aip import AipOcr
import time

#调用api
APP_ID = '18782573'
API_KEY = ' 6nYTHKqaLHdnl7GxOTm9sFDl'
SECRET_KEY = 'AXNuBRkBhmhZzlxX3Sv8IAdzhlb9RpL1'

while 1:
    #截图
    keyboard.wait(hotkey='f1')
    keyboard.wait(hotkey='ctrl+c')

    #保存
    image = ImageGrab.grabclipboard()
    image.save('01.jpg')
    time.sleep(0.1)

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    # 读取图片
    # def get_file_content(filepath):
    #     with open(filepath, 'rb') as fp:
    #         return fp.read()

    #image = get_file_content('01.jpg')

    with open('01.jpg','rb') as fp:
        image = fp.read()

    text = client.basicAccurate(image)
    for result in text['words_result']:
        print(result['words'])

#         with open('to_write.txt',encoding='utf-8') as f:
#             f.write(result['words'])
# #
