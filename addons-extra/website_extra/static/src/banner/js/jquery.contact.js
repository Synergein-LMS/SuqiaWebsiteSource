(function($) { 
	"use strict";
	
jQuery(document).ready(function(){
	$('#cform').on( "submit", function() { 

		var action = $(this).attr('action');

		$("#messages").slideUp(750,function() {
		$('#messages').hide();
		
		 $('#submit').before('<div class="text-center"><img src="images/ajax-loader.gif" class="contact-loader" /></div>').attr('disabled', 'disabled');
		
 		/*$('#submit')
			.before('<div class="text-center"></div>')
			.attr('disabled','disabled');*/

		$.post(action, {
			fname: $('#name').val(),
			designation: $('#designation').val(),
			company_name: $('#company_name').val(),
			address: $('#address').val(),
			email: $('#email').val(),
			phone: $('#phone').val(),
			message: $('#message').val(),
			
		},
			function(data){
				document.getElementById('messages').innerHTML = data;
				$('#messages').slideDown('slow');
				$('#cform img.contact-loader').fadeOut('slow',function(){$(this).remove()});
				$('#submit').removeAttr('disabled');
				if(data.match('success') != null) $('#cform').slideUp('slow');
			}
		);

		});

		return false;

	});

});

}(jQuery));