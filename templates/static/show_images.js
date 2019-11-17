function show_images()
{
	var image = document.getElementById("ticket-image");
	if (image.style.display === "none")
	{
		image.style.display = "initial";
	}
	else 
	{
		image.style.display = "none";
	}
}
