function submitAccuracyData() {
	var food = document.getElementById('food').value
	var recyclables = document.getElementById('recyclables').value
	var recyclables = document.getElementById('recyclables').value
	var food = document.getElementById('food').value
	asdfasfdasf
	if(this.score!=null && name){
		jQuery.ajax({
			type: "POST",
			data: {submit:"True", name : name, score: this.score },
			success: function(data) {
				this.score=null;
				}
		});
	}
	this.score = null;
	this.getScoreboardList();
},