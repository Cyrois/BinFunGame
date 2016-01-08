jQuery(document).ready(function() {
	//var num = 0;
	var prev_green = 0;
	var prev_grey = 0;
	var prev_blue = 0;
	var prev_black = 0;
	var green_img = document.getElementById("GreenImage");
	var grey_img = document.getElementById("GreyImage");
	var blue_img = document.getElementById("BlueImage");
	var black_img = document.getElementById("BlackImage");
	var green_msg = document.getElementById("GreenMessage");
	var grey_msg = document.getElementById("GreyMessage");
	var blue_msg = document.getElementById("BlueMessage");
	var black_msg = document.getElementById("BlackMessage");
	green_img.style.display = 'none';
	grey_img.style.display = 'none';
	blue_img.style.display = 'none';
	black_img.style.display = 'none';
	green_msg.style.display = 'none';
	grey_msg.style.display = 'none';
	blue_msg.style.display = 'none';
	black_msg.style.display = 'none';
	var counter = setInterval(updateCount, 500);
	var green_slot = document.getElementById("GreenSlot");
	var grey_slot = document.getElementById("GreySlot");
	var blue_slot = document.getElementById("BlueSlot");
	var black_slot = document.getElementById("BlackSlot");
	
	function updateCount() {
		jQuery.ajax({
			type: "POST",
			success: function(data) {
				var array = parseData(data);
				if (prev_green != array[0]) {
					jQuery('#front_green').html(array[0]);
					jQuery('#back_green').html(array[0]);
					green_slot.classList.toggle('flipped');
					changeGreenPic();
					prev_green = array[0];
				}
				if (prev_grey != array[1]) {
					jQuery('#front_grey').html(array[1]);
					jQuery('#back_grey').html(array[1]);
					grey_slot.classList.toggle('flipped');
					changeGreyPic();
					prev_grey = array[1];
				}
				if (prev_blue != array[2]) {
					jQuery('#front_blue').html(array[2]);
					jQuery('#back_blue').html(array[2]);
					blue_slot.classList.toggle('flipped');
					changeBluePic();
					prev_blue = array[2];
				}
				if (prev_black != array[3]) {
					jQuery('#front_black').html(array[3]);
					jQuery('#back_black').html(array[3]);
					black_slot.classList.toggle('flipped');
					changeBlackPic();
					prev_black = array[3];
				}
			}
		});
		//num = (num * 11 + 17) % 25;
	}

	function parseData(data) {
		var str = data.substring(1, (data.length) - 1);
		var array = str.split(", ");
		return array;
	}

	function changeGreenPic() {  
                green_img.style.display = '';
		        green_msg.style.display = '';
                green_img.src = "static/gifs/Food.gif";
            	jQuery("#GreenMessage").hide().fadeIn(2000);
            	jQuery("#GreenMessage").fadeOut(2000);
            }
            function changeGreyPic() {  
                grey_img.style.display = ''; 
                grey_msg.style.display = '';
                grey_img.src = "static/gifs/Plastics.gif";
		        jQuery("#GreyMessage").hide().fadeIn(2000);
            	jQuery("#GreyMessage").fadeOut(2000);
            }
            function changeBluePic() {  
                blue_img.style.display = '';
		        blue_msg.style.display = ''; 
                blue_img.src = "static/gifs/Paper.gif";
		        jQuery("#BlueMessage").hide().fadeIn(2000);
            	jQuery("#BlueMessage").fadeOut(2000);
            }
            function changeBlackPic() {
                black_img.style.display = '';
		        black_msg.style.display = '';
                black_img.src = "static/gifs/Garbage.gif";
		        jQuery("#BlackMessage").hide().fadeIn(2000);
                jQuery("#BlackMessage").fadeOut(2000);
            }
});