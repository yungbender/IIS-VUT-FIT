function redirect_to_ticket(ticketId)
{
    current_url = window.location.href;
    new_url = current_url + "/" + ticketId;
    window.location.href = new_url;
}
