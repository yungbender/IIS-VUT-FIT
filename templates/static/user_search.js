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
    if(position == 2)
        var managerName = document.getElementById("search-manager-bar-input");
    else
        var managerName = document.getElementById("search-developer-bar-input");

    managerName = managerName.value;

    var json = await perform_search(managerName, position);

    if(position == 2)
        var userElement = document.getElementById("search-manager-list");
    else
        var userElement = document.getElementById("search-developer-list");
    
    userElement.innerHTML = "";

    for(user in json[position])
    {
        if(position == 2)
            userElement.innerHTML = userElement.innerHTML + "<p id=\"search-manager-list-item\" onclick=\"select_manager(this)\">" + json[position][user] + "</p>\n";
        else
            userElement.innerHTML = userElement.innerHTML + "<p id=\"search-developer-list-item\" onclick=\"select_developer(this)\">" + json[position][user] + "</p>\n";
    }
}

function search_manager_wrap()
{
    search_user(2);
}

function search_developer_wrap()
{
    search_user(1);
}

function search_basedOnCookie_wrap()
{
    search_user(99);
}

function select_manager(selectedManager)
{
    managerId = document.getElementById("manager_id");
    managerId.value = selectedManager.innerHTML;
    document.getElementById("search-manager-wrapper").style.display = "none";
}

function select_developer(selectedDeveloper)
{
    developerId = document.getElementById("worker");
    developerId.value = selectedDeveloper.innerHTML;
    document.getElementById("search-developer-wrapper").style.display = "none";
}

window.onload = function(){
    if(document.getElementById("search-manager-bar-butt") != null)
        document.getElementById("search-manager-bar-butt").onclick = search_manager_wrap;
    if(document.getElementById("search-developer-bar-butt") != null)
        document.getElementById("search-developer-bar-butt").onclick = search_basedOnCookie_wrap;
}
