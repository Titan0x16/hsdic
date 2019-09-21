$("#get_image").click( function() {
	console.log("Clicked")
// Отправляем ajax запрос на сервер

	$(document).ajaxSend(function() {
		$("#spinnerhs").show()
	});
	$(document).ajaxComplete(function() {
		$(".textedimage").show('slow')
		$(".spinnerhs").hide()
	});

	$.ajax({
		type: "GET",
		url: "check_code/",
		data: {
			'deck_code': $("#centerblock__input").val(),
			'deck_language': $('input[name=language]:checked').val(),
		},
		dataType: "text",
		cache: false,
		success: function(data){

			$('#centerblock__input').val('star');
			$('#mainimage').attr('src', '/static/'+data);
			$('#mainimagedown').attr('src', '/static/'+data);
			$('#mainimagedown').attr('href', '/static/'+data);
			var rad = $('input[name=language]:checked').val()
			console.log(rad)
		}
	});
});