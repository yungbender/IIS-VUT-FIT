var isShown = false;

function add_comment()
{
   new_comment = document.getElementById("new-comment-wrapper");
   if(isShown)
   {
      new_comment.classList.remove("new-comment-show");
      new_comment.classList.toggle("new-comment-hide");
      isShown = false;
   }
   else
   {
      new_comment.classList.remove("new-comment-hide");
      new_comment.classList.toggle("new-comment-show");
      isShown = true;
   }
}