function add_comment(parent)
{
if (parent == null)
{
   var parent = document.getElementById("new-comment-wrapper");
}
var childs = parent.childNodes;
var childsCount = childs.lenght;
for (var i = 0; i <= childsCount; i++)
{
   add_comment(childs[i])
   if (childs[i].style.display === "none")
   {
      childs[i].style.display = "initial";
   } else
   {
      child[i].style.display = "none";
   }
}

}
