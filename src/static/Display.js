jQuery(document).ready(function() {
	//initialize variables
	var num = 0;
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
	var green_slot = document.getElementById("GreenSlot");
	var grey_slot = document.getElementById("GreySlot");
	var blue_slot = document.getElementById("BlueSlot");
	var black_slot = document.getElementById("BlackSlot");
	green_img.style.display = 'none';
	grey_img.style.display = 'none';
	blue_img.style.display = 'none';
	black_img.style.display = 'none';
	green_msg.style.display = 'none';
	grey_msg.style.display = 'none';
	blue_msg.style.display = 'none';
	black_msg.style.display = 'none';
	var counter = setInterval(updateCount, 500);

	//list of bin fun game tips
	var green_list = new Array();
	var grey_list = new Array();
	var blue_list = new Array();
	var black_list = new Array();

	//tips for food scraps
	green_list[ 0] = "Wet or dirty paper goes into the food scraps bin";
	green_list[ 1] = "Napkins and paper towels go into the food scraps bin";
	green_list[ 2] = "Dirty paper plates go into the food scraps bin";
	green_list[ 3] = "Wooden chopsticks go into the food scraps bin";
	green_list[ 4] = "No plastic containers in the food scraps bin";
	green_list[ 5] = "No plastic bags in the food scraps bin";
	green_list[ 6] = "No compostable plastics in the food scraps bin";
	green_list[ 7] = "No compostable plastic bags in the food scraps bin";
	green_list[ 8] = "No biodegradable plastic bags in the food scraps bin";
	green_list[ 9] = "UBC uses food scraps to nurture flowers and trees";
	green_list[10] = "Food waste in the garbage bin produce methane";
	green_list[11] = "Keep ALL plastics out of the food scraps bin";
	green_list[12] = "Food scraps are banned from garbage in Vancouver";

	//tips for recyclable containers
	grey_list[ 0] = "Check for a recycling symbol and number 1-7";
	grey_list[ 1] = "UBC accepts all plastics (#1-7) in the recyclable containers bin";
	grey_list[ 2] = "Always separate the paper sleeve from your coffee cup";
	grey_list[ 3] = "Milk cartons go into the recyclable containers bin";
	grey_list[ 4] = "Tetra paks go into the recyclable containers bin";
	grey_list[ 5] = "Only recycle clean containers in the recyclable containers bin";
	grey_list[ 6] = "Clean aluminum containers go into the recyclable containers bin";
	grey_list[ 7] = "No broken glass in the recyclable containers bin";
	grey_list[ 8] = "No styrofoam in the recyclable containers bin";
	grey_list[ 9] = "No plastic bags in the recyclable containers bin";
	grey_list[10] = "No candy wrappers in the recyclable containers bin";
	grey_list[11] = "No chip bags in the recyclable containers bin";
	grey_list[12] = "No plastic wrappers in the recyclable containers bin";
	grey_list[13] = "Dump liquids before recycling cups in the containers bin";
	grey_list[14] = "Dump food before recycling containers";
	grey_list[15] = "It takes 1 million years for glass bottles to decompose";
	grey_list[16] = "It takes 1000 years for plastic bottles to decompose";
	grey_list[17] = "It takes 1000 years for plastic bags to decompose";
	grey_list[18] = "It takes 500 years for aluminum cans to decompose";

	//tips for paper
	blue_list[ 0] = "Paper sleeves from coffee cup go into the paper bin";
	blue_list[ 1] = "Only clean paper in the paper bin";
	blue_list[ 2] = "No napkins in the paper bin";
	blue_list[ 3] = "Paper napkins go into the food scraps bin";
	blue_list[ 4] = "No paper towels in the paper bin";
	blue_list[ 5] = "Paper towels go into the food scraps bin";
	blue_list[ 6] = "No dirty pizza boxes in the paper bin";
	blue_list[ 7] = "No paper plates in the paper bin";
	blue_list[ 8] = "Paper plates go into the food scraps bin";
	blue_list[ 9] = "No coffee cups in the paper bin";
	blue_list[10] = "Coffee cups go into the recyclable containers bin";
	blue_list[11] = "Soiled paper plates in the paper bin";
	blue_list[12] = "1 ton of recycled paper saves 17 trees";
	blue_list[13] = "1 ton of recycled paper saves 7000 gallons of water";
	blue_list[14] = "1 ton of recycled paper saves 4200 kWh of electricity";

	//tips for garbage
	black_list[ 0] = "Styrofoam cups or boxes go into garbage";
	black_list[ 1] = "Broken glass goes into garbage";
	black_list[ 2] = "Plastic bags go into garbage";
	black_list[ 3] = "Chip bags go into garbage ";
	black_list[ 4] = "Candy wrappers go into garbage";
	black_list[ 5] = "Aluminum foil goes into garbage";
	black_list[ 6] = "Dirty aluminum containers go into garbage";
	black_list[ 7] = "Plastic wraps go into garbage";
	black_list[ 8] = "Waxed paper goes into garbage";
	black_list[ 9] = "Plastics with no recycling symbol go into garbage";
	black_list[10] = "Plastic bags go into garbage";
	black_list[11] = "Compostable plastics go into garbage";
	black_list[12] = "Compostable plastic bags go into garbage";
	black_list[13] = "Biodegradable plastic bags go into garbage";
	black_list[14] = "When in doubt, throw it in garbage";
	black_list[15] = "Batteries and e-waste cannot be recycled here";

	//fcn to update count of each bin when a recyclable is placed into a bin
	function updateCount() {
		jQuery.ajax({
			type: "POST",
			success: function(data) {
				var array = parseData(data);
				num = num + 1;
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
	}

	//fcn to parse counts of bins
	function parseData(data) {
		var str = data.substring(1, (data.length) - 1);
		var array = str.split(", ");
		return array;
	}

	//fcns to animate images and messages of each bin
	function changeGreenPic() {  
        green_img.style.display = '';
		green_msg.style.display = '';
        green_img.src = "static/gifs/Food.gif";
        jQuery("#GreenMessage").hide().fadeIn(2000);
        jQuery("#GreenMessage").fadeOut(2000);
		jQuery("#GreenMessage").html(green_list[num % green_list.length]);
    }
    function changeGreyPic() {  
        grey_img.style.display = ''; 
        grey_msg.style.display = '';
        grey_img.src = "static/gifs/Plastics.gif";
		jQuery("#GreyMessage").hide().fadeIn(2000);
        jQuery("#GreyMessage").fadeOut(2000);
		jQuery("#GreyMessage").html(grey_list[num % grey_list.length]);
    }
    function changeBluePic() {  
        blue_img.style.display = '';
		blue_msg.style.display = ''; 
        blue_img.src = "static/gifs/Paper.gif";
		jQuery("#BlueMessage").hide().fadeIn(2000);
        jQuery("#BlueMessage").fadeOut(2000);
		jQuery("#BlueMessage").html(blue_list[num % blue_list.length]);
    }
    function changeBlackPic() {
        black_img.style.display = '';
		black_msg.style.display = '';
        black_img.src = "static/gifs/Garbage.gif";
		jQuery("#BlackMessage").hide().fadeIn(2000);
        jQuery("#BlackMessage").fadeOut(2000);
		jQuery("#BlackMessage").html(black_list[num % black_list.length]);
    }
});