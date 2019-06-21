// $('#post-form').on('submit', function(event){
//     event.preventDefault();
//     console.log("form submitted!")  // sanity check
//     create_post();
// });

// function create_post() {
//     $.ajax({
//         url : "/blogcomment/", // the endpoint
//         type : "POST", // http method
//         data : {
//             video_description : $('#video_description').val(),
//             video_duration:  $('#video_duration').val(),
//             video_location:  $('#video_location').val(),
//             video_tags:  $('#video_tags').val(),
//             video_file:  $('#video_file').val(),            
//         }, // data sent with the post request

//         // handle a successful response
//         success : function(json) {
//             $('#video_description').val(''); // remove the value from the input
//             $('#video_duration').val(''); // remove the value from the input
//             $('#video_location').val('');
//             $('#video_tags').val('');
//             $('#video_file').val(''); // remove the value from the input
//             $('#SubscribeForm').prepend("<div class='alert alert-success'><button type='button' class='close' data-dismiss='alert'>&times;</button>" + json.result +"</div>");
//         },

//         // handle a non-successful response
//         error : function(xhr,errmsg,err) {
//             $('#SubscribeForm').prepend("<div class='alert alert-danger'><button type='button' class='close' data-dismiss='alert'>&times;</button>Oop! Error happend!</div>"); // add the error to the dom
//             //console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
//         }
//     });
// }

$(document).ready(function(){
	var $myForm = $('.my-ajax-form');
	$myForm.submit(function(event){
		event.preventDefault();
		var $formData = $myForm.serialize();
		var $thisURL = $myForm.attr('data-url') || window.loaction.href;
		$.ajax({
			method:'POST',
			url: $thisURL,
			data: $formData,
			success: handleSuccess,
			error: handleError,
		});
		function handleSuccess(data){
			console.log(data.message);
			$myForm[0].reset()
		}
		function handleError(ThrowError){
			console.log(ThrowError);
		}
	});
});