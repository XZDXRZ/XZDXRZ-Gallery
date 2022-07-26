// Run after the whole page is loaded.
// Change the width and position of the titles under the pictures.

var picWidth, picHeight;

picHeight = document.getElementsByClassName("images")[0].clientHeight;
picWidth = document.getElementsByClassName("images")[0].clientWidth;

picTitle = document.getElementsByClassName("title");

for (var i=0;i<picTitle.length;i++) {
    picTitle[i].style.width = picWidth + "px";
    picTitle[i].style.marginTop = picHeight*-0.06+"px";
}