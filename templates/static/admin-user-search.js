async function perform_search(name, position)
{
    var endpoint = window.location.protocol + "//" + window.location.host + "/users";
    var parameters = "?" + "pattern=" + name + "&" + "position=" + position;
    var requesturl = endpoint + parameters;
    response = await fetch(requesturl);
    response = await response.json()
    return response;
}

async function search_admin_users(position)
{
    var managerName = document.getElementById("main-users");

    managerName = managerName.value;

    var json = await perform_search(managerName, position);

    var userElement = document.getElementById("users");
    userElement.innerHTML = "";
    var clientname;
    
    for(user in json[position])
    {
        for(id in json[position][user])
        {
            userElement.innerHTML = userElement.innerHTML + "<a href=\"/profile/" + json[position][user][id] + "\">" + id + "</a>\n";
        }
    }
    
    document.getElementById("main-users").focus();
}


function search_admin_wrap()
{
    search_admin_users(98);
}

function select_assignee(selectedDeveloper)
{
    developerId = document.getElementById("worker");
    developerId.value = selectedDeveloper.innerHTML;
    document.getElementById("search-assignee-wrapper").style.display = "none";
}