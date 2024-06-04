let url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json'
$.get(url, function (data, stat) {
	$('div#character').text(data.name);
});
