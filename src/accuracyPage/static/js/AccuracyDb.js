function getTodayDate() {
	var today = new Date();
	var dd = today.getDate();
	var mm = today.getMonth()+1; //January is 0!
	var yyyy = today.getFullYear();
	if(dd<10) {
		dd='0'+dd
	} 
	if(mm<10) {
		mm='0'+mm
	} 
	today = yyyy+'-'+mm+'-'+dd;
	console.log(today);
	return today;
}


function submitAccuracyData() {
	var food = document.getElementById('food').value
	var recyclables = document.getElementById('recyclables').value
	var paper = document.getElementById('paper').value
	var garbage = document.getElementById('garbage').value
	//myhiddeninput is the value of the calendar
	var date = $('#my_hidden_input').val();
	//console.log("DATE!!! : " + date);
	if(isNaN(food) || isNaN(recyclables) || isNaN(paper) || isNaN(garbage) || food == "" || recyclables == "" || paper == "" || garbage == ""){
		alert("Please make sure all the values in the textboxes are numbers!");
	}
	if(date == "") {
		alert("Please make sure a date is selected!");
	}
	else {
		jQuery.ajax({
			type: "POST",
			data: {submit:"True", food : food, recyclables: recyclables, paper: paper, garbage: garbage, date: date },
			success: function(data) {
				//console.log("submit success");
				$("#successText").fadeToggle("slow");
				$("#successText").fadeToggle(5500);
				}
		});
	}
	console.log("submit function done");
}