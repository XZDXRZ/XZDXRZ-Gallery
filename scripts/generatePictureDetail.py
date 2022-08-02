# Generating the detailed pages of each pictures.

basicHTML = [
    """<!DOCTYPE html>
<html>
<head>
    <title>XZDXRZ Gallery</title>
	<meta name="author" content="XZDXRZ" />
    <link rel="stylesheet" href="./css/pictureCSS.css" />
</head>
<body>
    <div id="nav_top">
        <ul>
            <li><a href="../index.html"><div class="nav_top_link">Home</div></a></li>
            <li><a href="../downloads/index.html"><div class="nav_top_link">Downloads</div></a></li>
            <li><a href="../about/index.html"><div class="nav_top_link">About</div></a></li>
            <li><a href="../contact/index.html"><div class="nav_top_link">Contact</div></a></li>
		</ul>
    </div>
    <h1>""",
    """</h1>
    <div id="display">
        <img id="image" src="../images/""",
    """.""",
    """" alt="Check your Internet." />
    </div>
    <div style="text-align: center"><a href="../images/""",
    """.""",
    """" id="download">Download</a></div>
	<footer>
		<p>Author: XZDXRZ</p>
	</footer>
</body>
</html>
"""
]

def pictureIndexConvert(picture_index):
    if picture_index < 10:
        return '0'+str(picture_index)
    elif picture_index >= 10 and picture_index < 100:
        return str(picture_index)

def generateSourceCode(pictureID, pictureType, pictureTitle):
    return basicHTML[0]+pictureTitle+basicHTML[1]+pictureIndexConvert(pictureID)+basicHTML[2]+pictureType+basicHTML[3]+pictureIndexConvert(pictureID)+basicHTML[4]+pictureType+basicHTML[5]

def writeHTML(pictureID, sourceCode):
    with open("./pictures/"+pictureIndexConvert(pictureID)+'.html', "w") as page:
        page.write(sourceCode)

if __name__ == "__main__":
    page_index = 9
    picture_type = 'png'
    page_title = 'Atago and Takao'
    source_code = generateSourceCode(page_index, picture_type, page_title)
    writeHTML(page_index, source_code)
