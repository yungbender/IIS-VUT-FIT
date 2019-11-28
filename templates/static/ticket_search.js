async function perform_fetch()
{
    var requesturl = window.location.protocol + "//" + window.location.host + "/tickets/json";
    response = await fetch(requesturl);
    response = await response.json();
    return response;
}

async function search_tickets()
{
    response = await perform_fetch();
    
    var userElement = document.getElementById("search-ticket-list");
    userElement.innerHTML = "";

    for(var productName in response)
    {
        // productName == Nazov produktu z ktoreho sa idu pozriet tickety
        var tickets = response[productName];
        for(var listMember in tickets)
        {
            for(var ticketName in tickets[listMember])
            {
                // ticketName == Nazov ticketu ktory je priradeny ku produktu
                ticketId = tickets[listMember][ticketName]
                // ticketId == Idčko ticketu z db
                console.log(ticketName);
                console.log(ticketId);
                userElement.innerHTML = userElement.innerHTML + "<p id=\"search-list-item\" onclick=\"select_ticket(" + ticketId + ")\">" + ticketName + "</p>\n";
            }
        }
    }

    if (userElement.innerHTML == "")
    {
        userElement.innerHTML = userElement.innerHTML + "<p>There are no tickets related to you</p>";
    }
}

function select_ticket(selectedTicket)
{
    developerId = document.getElementById("ticket");
    developerId.value = selectedTicket;
    document.getElementById("search-ticket-wrapper").style.display = "none";
}

function hideSearchTicket()
{
  var ticket = document.getElementById("search-ticket-wrapper");
  var assignee = document.getElementById("search-assignee-wrapper");
  if (ticket.style.display === "none")
  {
    if (assignee.style.display !== "none")
    {
        assignee.style.display = "none";
    }
    search_tickets()
    ticket.style.display = "initial";
  } 
  else 
  {
    ticket.style.display = "none";
  }
}