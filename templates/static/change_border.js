window.onload = onLoad;

function onLoad() {
  forms = document.getElementsByClassName("task-form")
  for (var i = forms.length - 1; i >= 0; i--) {
    forms[i].onmouseup = function(event) {changeColorOnMouseEnter()};
  }
  
}

function changeColorOnMouseEnter()
{
  form = document.getElementsByClassName("task-form")[0]
  event.target.style.border = "2px solid #1aa3ff";
}