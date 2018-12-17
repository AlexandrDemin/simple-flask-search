$(document).foundation();
new ClipboardJS('.copy-btn');
$queriesArea = $('.queries-area');
autosize($queriesArea);

function getQueries() {
	var $search = $('.search');
	var q = $search.val();
	$.ajax({
		type: "POST",
		url: '/',
		data: JSON.stringify({"q": q}),
		success: function(data) {
			$queriesArea.val(data.join('\n'));
			autosize.update($queriesArea);
		},
		error: function() {alert('Ошибка при обращении к серверу. Попробуй ещё раз или обратись к разработчикам')},
		contentType:"application/json; charset=utf-8",
		dataType:"json",
	});
}

$searchBtn = $('.search-button');
$searchBtn.click(getQueries);

$('form').keypress(function(e) {
    if(e.which == 13) {
    	e.preventDefault();
        getQueries();
    }
});