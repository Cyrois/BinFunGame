$(document).ready(function(){
	$('#datepicker1').datepicker({
		format: 'yyyy-mm-dd',
	}),
	$('#datepicker1').on("changeDate", function() {
		console.log("clicked calendar")
		$('#my_hidden_input').val(
			$('#datepicker1').datepicker('getFormattedDate')
		);
	}),
	$('.nav.navbar-nav > li').on('click', function(e) {
		console.log("clicked nav-bar");
		$('.nav.navbar-nav > li').removeClass('active');

		$(this).addClass('active');
		console.log($(this).text());
		if( $(this).text() == "View" ) {
			$('.input-tab-container').fadeOut();
			$('.view-tab-container').delay(333).fadeIn();
		}
		if( $(this).text() == "Input Accuracy Data (%)" ) {
			$('.view-tab-container').fadeOut();
			$('.input-tab-container').delay(333).fadeIn();
		}
	})
});