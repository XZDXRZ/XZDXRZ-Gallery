# Mix addPictureInIndex.py and generatePictureDetail.py in order to add picture in one file

import addPictureInIndex as pid
import generatePictureDetail as pdtl

if __name__ == "__main__":
    picture_index = 9
    picture_type = 'png'
    picture_title = 'Atago and Takao'
    # addPictureInIndex.py
    targetIndex, html = pid.getTargetRowIndex()
    pictureCode = pid.getPictureCode(picture_index, picture_title, picture_type)
    pid.insertCode(targetIndex, html, pictureCode)
    # generatePictureDetail.py
    source_code = pdtl.generateSourceCode(picture_index, picture_type, picture_title)
    pdtl.writeHTML(picture_index, source_code)
