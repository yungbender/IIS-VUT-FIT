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

    if (position == 99)
    {
        for(user in json[position])
        {
            for(id in json[position][user])
            {
                userElement.innerHTML = userElement.innerHTML + "<p id=\"search-list-item\" onclick=\"select_assignee(this)\">" + id + "</p>\n";
            }
        }
    }
    else if (position == 2)
    {
        for(user in json[position])
        {
                userElement.innerHTML = userElement.innerHTML + "<p id=\"search-list-item\" onclick=\"select_assignee(this)\">" + json[position][user] + "</p>\n";

        }
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

function select_assignee(selectedWorker)
{
    workerId = document.getElementById("worker");
    workerId.value = selectedWorker.innerHTML;
    document.getElementById("search-assignee-wrapper").style.display = "none";
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