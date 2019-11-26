async function perform_search(name, position)
{
    var endpoint = window.location.protocol + "//" + window.location.host + "/users";
    var parameters = "?" + "pattern=" + name + "&" + "position=" + position;
    var requesturl = endpoint + parameters;
    response = await fetch(requesturl);
    response = await response.json()
    return response;
}

async function search_user(position)
{
    var managerName = document.getElementById("search-bar-input");

    managerName = managerName.value;

    var json = await perform_search(managerName, position);

    var userElement = document.getElementById("search-list");
    
    userElement.innerHTML = "";

    for(user in json[position])
    {
        userElement.innerHTML = userElement.innerHTML + "<p id=\"search-list-item\" onclick=\"select_assignee(this)\">" + json[position][user] + "</p>\n";
    }
}

async function search_ticket(position)
{
    var managerName = document.getElementById("search-ticket-bar-input");

    managerName = managerName.value;

    var json = await perform_search(managerName, position);

    var userElement = document.getElementById("search-ticket-list");
    
    userElement.innerHTML = "";

    for(user in json[position])
    {
        userElement.innerHTML = userElement.innerHTML + "<p id=\"search-list-item\" onclick=\"select_assignee(this)\">" + json[position][user] + "</p>\n";
    }
}

function search_wrap()
{
    search_user(99);
}

function search_ticket_wrap()
{
    search_ticket(99);
}

function search_manager_wrap()
{
    search_user(2);
}

function select_assignee(selectedDeveloper)
{
    developerId = document.getElementById("worker");
    developerId.value = selectedDeveloper.innerHTML;
    document.getElementById("search-assignee-wrapper").style.display = "none";
}

function select_ticket(selectedTicket)
{
    developerId = document.getElementById("ticket");
    developerId.value = selectedTicket;
    document.getElementById("search-ticket-wrapper").style.display = "none";
}

function hideSearch()
{
    var assignee = document.getElementById("search-assignee-wrapper");
    if (assignee.style.display === "none")
    {
        assignee.style.display = "initial";
    } 
    else 
    {
        assignee.style.display = "none";
    }
  }

function hideSearchAssignee()
{
    var ticket = document.getElementById("search-ticket-wrapper");
    var assignee = document.getElementById("search-assignee-wrapper");
    if (assignee.style.display === "none")
    {
        if (ticket.style.display !== "none")
        {
        ticket.style.display = "none";
        }
        assignee.style.display = "initial";
    } 
    else 
    {
        assignee.style.display = "none";
    }
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
    ticket.style.display = "initial";
  } 
  else 
  {
    ticket.style.display = "none";
  }
}