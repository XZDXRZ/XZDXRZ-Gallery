// Run after the whole page is loaded.
// Change the width and position of the titles under the pictures.

var picWidth, picHeight;

pic = document.getElementsByClassName("images");

picHeight = pic[0].height;
picWidth = pic[0].width;

picTitle = document.getElementsByClassName("title");

for (var i=0;i<picTitle.length;i++) {
    pic[i].style.width = picWidth + "px";
    picTitle[i].style.width = picWidth + "px";
    picTitle[i].style.marginTop = picHeight*(-0.055)+"px";
}
