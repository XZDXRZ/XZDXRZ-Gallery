# Adding HTML of pictures for "./index.html"

import re

def pictureIndexConvert(picture_index):
    if picture_index < 10:
        return '0'+str(picture_index)
    elif picture_index >= 10 and picture_index < 100:
        return str(picture_index)

def getPictureCode(picture_index, title, picType):
    pictureCode = [
        '\t\t<div class="picture">\n',
        '\t\t\t<a href=\"./pictures/'+pictureIndexConvert(picture_index)+r'.html"><img src="./images/'+pictureIndexConvert(picture_index)+r'.'+picType+'\" alt=\"Check your internet\" class=\"images\" /></a>\n',
        '\t\t\t<p class=\"title\">'+title+'</p>\n',
        '\t\t</div>\n'
    ]
    return pictureCode

def getTargetRowIndex():
    with open("./index.html", 'r') as page:
        HTMLcode = page.readlines()
        row_index = 0
        target_index = -1
        for code in HTMLcode:
            row_index+=1
            if re.findall(r'<div class="picture">',code) != []:
                target_index = row_index + 3
        return target_index, HTMLcode

def insertCode(target_index, HTMLcode, pictureCode):
    with open("./index.html", 'w') as page:
        for i in range(0, 4):
            HTMLcode.insert(target_index+i, pictureCode[i])
        HTMLcode = "".join(HTMLcode)
        page.write(HTMLcode)

if __name__ == "__main__":
    picture_index = 8
    picture_title = 'Shokaku'
    picture_type = 'jpg'
    targetIndex, html = getTargetRowIndex()
    pictureCode = getPictureCode(picture_index, picture_title, picture_type)
    insertCode(targetIndex, html, pictureCode)
