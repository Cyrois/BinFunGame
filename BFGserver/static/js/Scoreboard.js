var BinFunGame = BinFunGame || {};

BinFunGame.Scoreboard = function (){};

BinFunGame.Scoreboard.prototype = {
	init: function(score) {
	if(score == undefined){
		var score = 9999;
	}
    this.score = score;
    this.load = true;
   },
	create: function(){
	    //this.game.stage.backgroundColor = '#fff';
	    this.skyBackground = this.game.add.tileSprite(0, 0, this.game.world.width, this.game.world.height-128, 'sky');
	    this.groundBackground = this.game.add.tileSprite(0, this.game.world.height-128, this.game.world.width, 128, 'ground');
	    this.generateClouds();

	    var scoreText = "Your score: " + this.score;
	    var style = { font: "30px Arial", fill: "#000", align: "center" };
	    var t = this.game.add.text(this.game.width/4, this.game.height/4+50, scoreText, style);
	    t.anchor.set(0.5);

	    //Submit Score button
		var submitButton = this.game.add.button();
		submitButton = this.game.add.button(this.game.width/4, this.game.height/4 + 100, 'submitButton', this.submitScore, this);
		submitButton.anchor.set(0.5);

	    //Start Game button
		var startButton = this.game.add.button();
		startButton = this.game.add.button(this.game.width/4, this.game.height/4 + 150, 'startButton', this.startGame, this);
		startButton.anchor.set(0.5);

		//Temp code for scoreboard
		scoreboardList = [{name:"Anon",score:99},{name:"Anon",score:99},{name:"Anon",score:99},
		{name:"Anon",score:99},{name:"Anon",score:99},{name:"Anon",score:99}
		,{name:"Anon",score:99},{name:"Anon",score:99},{name:"Anon",score:99}
		,{name:"Anon",score:99}];

		this.initScoreboard(scoreboardList);


	},
	update: function(){

		if(this.game.input.activePointer.justPressed()) {
		   //this.getScoreboardList();
		}
		if(this.load == true){
			console.log("First load");
			this.getScoreboardList();
			this.load =false;
		}
	},

	generateClouds: function(){
		this.clouds =  this.game.add.group();
	    this.clouds.enableBody = true;
		for(var i=0;i<10;i++){
			var cloud = this.clouds.create(this.game.world.randomX,this.game.world.randomY/2,'cloud');
			cloud.body.velocity.x = this.game.rnd.integerInRange(-40, -10);
		}
	},

	startGame: function(){
		this.game.state.start('Game');
	},

	submitScore: function(){
		var name = prompt("Please enter your name", "Anonymous");
		if(this.score!=null && name){
			jQuery.ajax({
				type: "POST",
				data: {submit:"True", name : name, score: this.score },
				success: function(data) {
					this.score=null;
					}
			});
		}
		this.getScoreboardList();
	},

	getScoreboardList: function(){
		jQuery.ajax({
				type: "POST",
				data: {submit:"False"},
				success: function(data) {
					scoreboardList = data;
					console.log("Get scoreboardList");
					console.log(scoreboardList);
					BinFunGame.Scoreboard.prototype.updateScoreboard(scoreboardList);
					return scoreboardList;
					}
			});
	},

	initScoreboard: function(scoreboard){
		var scoreboardBackground = this.game.add.sprite(this.game.world.width/2, this.game.world.height/10, 'scoreboard');
		scoreboardBackground.scale.setTo(1.5);
		scoreboardEntries = this.game.add.group();
		this.scoreboardNumbers =  this.game.add.group();
		this.style = { font: "20px Arial", fill: "#000", align: "center" };
		
		for(var i=0;i<scoreboard.length;i++){
			var entryText = scoreboard[i].name + " Score: " + scoreboard[i].score + " seconds";
			scoreboardEntries.add(this.game.make.text(this.game.world.width/2+55, this.game.world.height/10+70+(i*35), entryText, this.style));
		}

		var t = this.game.add.text(this.game.world.width/2+15, this.game.world.height/10+15, "Scoreboard: Top 10 Times", { font: "30px Arial", fill: "#000", align: "center" });
		
		//Change to top 10 when graphic changes
		for(var i=0;i<10;i++){
			this.scoreboardNumbers.add(this.game.make.text(this.game.world.width/2+15, this.game.world.height/10+70+(i*35), i+1, this.style));
		}
	},

	updateScoreboard: function(scoreboard){
		//ERROR between here and passing the list around
		// Add lock/flags thing here
		scoreboard = this.parseData(scoreboard);
		for(var i=0;i<scoreboard.length;i++){
			scoreboardEntries.children[i].setText(scoreboard[i].name + " Score: " + scoreboard[i].score );

		}
	},

	parseData: function(scoreboard){
		var indexScore = scoreboard.indexOf('score');
		var tempScoreboard = [];
		while(indexScore !==-1){
			var indexBegin =  indexScore+10;
			var indexNameBegin = indexBegin+17;
			var indexEnd = scoreboard.indexOf('\'',indexBegin);
			var indexNameEnd = scoreboard.indexOf('\'',indexNameBegin);
			var entry={name:"", score:0};
			entry.score = String(scoreboard).substring(indexBegin,indexEnd);
			entry.name = String(scoreboard).substring(indexNameBegin,indexNameEnd);
			tempScoreboard.push(entry);
			var indexScore = scoreboard.indexOf('score',indexScore+1);
		}
		return tempScoreboard;
	}
};