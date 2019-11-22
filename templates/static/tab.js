function selectTab(tabName)
{

  if(tabName == "detail")
  {
    document.getElementById("detail-butt").style.backgroundColor = "rgb(26, 163, 255)";
    document.getElementById("content-butt").style.backgroundColor = "white";
    document.getElementById("content").style.display = "none";
    document.getElementById("detail").style.display = "block";
  }
  else if (tabName == "content")
  {
    document.getElementById("content-butt").style.backgroundColor = "rgb(26, 163, 255)";
    document.getElementById("detail-butt").style.backgroundColor = "white";
    document.getElementById("detail").style.display = "none";
    document.getElementById("content").style.display = "block";
  }
}