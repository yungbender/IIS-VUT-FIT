function redirect_to_ticket(ticketId)
{
    current_url = window.location.href;
    new_url = current_url + "/" + ticketId;
    window.location.href = new_url;
}

function close_ticket()
{
    current_url = window.location.href;
    new_url = current_url + "/close";
    window.location.href = new_url;
}

function mark_answer(commentId)
{
    current_url = window.location.href;
    new_url = current_url + "/" + commentId;
    window.location.href = new_url;
}