# A script used for adding Download Links to ./downloads/index.html

import re

code = [
    '\t\t\t<tr>\n',
    '\t\t\t\t<th>', '</th>\n',
    '\t\t\t\t<th><a href="', '">', '</th>\n',
    '\t\t\t</tr>\n'
]

def pictureIndexConvert(picture_index):
    if picture_index < 10:
        return '0'+str(picture_index)
    elif picture_index >= 10 and picture_index < 100:
        return str(picture_index)

def getTitleLink(pictureIndex):
    with open("./pictures/"+pictureIndexConvert(pictureIndex)+".html", 'r') as page:
        HTMLcode = page.readlines()
        for line in HTMLcode:
            find_result = re.findall("<h1>.*?</h1>", line)
            if find_result != []:
                title = find_result[0][4:-5]
            find_result = re.findall('<img id="image"[\d\D]*?/>', line)
            if find_result != []:
                link = find_result[0][21:-31]
    return title, link

def findDownload():
    with open("./downloads/index.html", 'r') as downloadF:
        page = downloadF.readlines()
        i=1
        for line in page:
            if re.findall("</table>", line):
                return i-1
            i+=1

def addLink(lineIndex, HTMLCode, title, link):
    with open("./downloads/index.html", 'w') as page:
        HTMLcode = page.readline()
        indexAdder = (i for i in range(0, 10))
        HTMLcode.insert(lineIndex+next(indexAdder), code[0])
        HTMLcode.insert(lineIndex+next(indexAdder), code[1])
        HTMLcode.insert(lineIndex+next(indexAdder), title)
        HTMLcode.insert(lineIndex+next(indexAdder), code[2])
        HTMLcode.insert(lineIndex+next(indexAdder), code[3])
        HTMLcode.insert(lineIndex+next(indexAdder), link)
        HTMLcode.insert(lineIndex+next(indexAdder), code[4])
        HTMLcode.insert(lineIndex+next(indexAdder), title)
        HTMLcode.insert(lineIndex+next(indexAdder), code[5])
        HTMLcode.insert(lineIndex+next(indexAdder), code[6])
        HTMLcode = "".join(HTMLcode)
        page.write(HTMLcode)

if __name__ == "__main__":
    title, link = getTitleLink(2)
    line = findDownload()
    addLink(line, title, link)
