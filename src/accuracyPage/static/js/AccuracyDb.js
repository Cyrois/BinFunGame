function submitAccuracyData() {
	var food = document.getElementById('food').value
	var recyclables = document.getElementById('recyclables').value
	var paper = document.getElementById('paper').value
	var garbage = document.getElementById('garbage').value
	//TODO: get the date from the calendar
	var date = "2016-02-22" //temp date
	if(isNaN(food) || isNaN(recyclables) || isNaN(paper) || isNaN(garbage)){
		alert("Please make sure all the values in the textboxes are numbers");
	}
	else {
		jQuery.ajax({
			type: "POST",
			data: {submit:"True", food : food, recyclables: recyclables, paper: paper, garbage: garbage, date: date },
			success: function(data) {
				console.log("submit success");
				}
		});
	}
	console.log("submit function done");
}