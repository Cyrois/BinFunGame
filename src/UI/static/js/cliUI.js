function getData() {
	var startdate = document.getElementById('startdate').value
	var enddate = document.getElementById('enddate').value
	var binlocation = document.getElementById('binlocation').value
	var color = document.getElementById('color').value

	//TODO: need to change 'if' part 
	if(!(startdate) || !(enddate) || !(binlocation) || !(color)){
		alert("Please make sure to fill in all the values");
	}
	else {
		jQuery.ajax({
			type: "POST",
			data: {submit:"True", startdate: startdate, enddate: enddate, binlocation: binlocation, color: color},
			success: function(data) {
				console.log("submit success");
				}
		});
	}
	console.log("submit function done");
}
