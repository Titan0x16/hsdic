



// $("#get_image").click( function() {
// 	console.log("CLICK get_image");
// });

$("#changepid").click( function() {
	console.log("CLICK check_name_btn");
	$('#pid').append("<li>Starting request at </li>");

});

// $(document).ajaxSend(function(event, request, settings) {
// 	$("#logodown").hide()
//     $( "#pid" ).append( "<li>Starting request at " + settings.url + "</li>" );
// });

// $("#logodown").bind("ajaxSend", function(){
//     $(this).show(); // показываем элемент
// }).bind("ajaxComplete", function(){
//     $(this).hide(); // скрываем элемент
// });


$("#check_name_btn").click( function() {
	console.log("CLICK check_name_btn")
// Отправляем ajax запрос на сервер
	$(document).ajaxSend(function() {
		$("#test_block1").show()
	});
	$(document).ajaxComplete(function() {
		$("#test_block1").hide()
	});

	$.ajax({
		type: "GET",
		url: "check_username/",
		data: {
			'user_name': $("#user_name_input").val(),
		},
		dataType: "text",
		cache: false,
		global: true,
		success: function(data){
			// alert( "Прибыли данные: ");
			console.log(data)
			$('#email_input').val(data);
			var srclogo = $('#logo').attr('src');
			console.log(srclogo);
			$('#logo').attr('src', '/static/hsdic/'+data+'.png');
			var srclogo2 = $('#logo').attr('src');
			console.log(srclogo2);

			// srclogo.replace('hslogo', data);

			// if (data == 'ok') {
			// 	console.log("ok");
			// 	$('#email_input').val('text+++');
			// }
			// else if (data == 'no') {
			// 	console.log("no");
			// }
		}
	});
});

// $("#check_name_btn").click( function() {
// 	console.log("CLICK check_name_btn")
// 	$.ajax({
// 		type: "GET",
// 		url: "check_username",
// 		data: {
// 			'user_name': "XXX",
// 		},
// 		success: function(data){
// 			alert( "Прибыли данные: " + data );
// 		}
// 	});
// });


// $("#check_name_btn").click(function() {
// 	console.log("CLICK")
// 	var text = $(this).text();
// 	$('#user_name_input').val(text);
// });
