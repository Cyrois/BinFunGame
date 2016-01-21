var BinFunGame = BinFunGame || {};

BinFunGame.Scoreboard = function (){};

BinFunGame.Scoreboard.prototype = {
	init: function(score) {
    console.log(score);
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

	    //Title
	    var title = "Scoreboard!!";
	    var style = { font: "30px Arial", fill: "#000", align: "center" };
	    var t = this.game.add.text(this.game.width/4, this.game.height/4, title, style);
	    t.anchor.set(0.5);

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
		this.updateScoreboard(scoreboardList);


	},
	update: function(){

		if(this.game.input.activePointer.justPressed()) {
		   //this.updateScoreboard(scoreboardList);
		}
		if(this.load == true){
			console.log("Loading!")
			this.updateScoreboard(scoreboardList);
			this.load =false;
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
		this.updateScoreboard(scoreboardList);
	},

	getScoreboardList: function(scoreboard){
		jQuery.ajax({
				type: "POST",
				data: {submit:"False"},
				success: function(data) {
					scoreboardList = data;
					return ;
					}
			});
	},

	initScoreboard: function(scoreboard){
		var scoreboardBackground = this.game.add.sprite(this.game.world.width/2, this.game.world.height/10, 'scoreboard');
		scoreboardBackground.scale.setTo(1.5);
		this.scoreboardEntries = this.game.add.group();
		this.scoreboardNumbers =  this.game.add.group();
		this.style = { font: "20px Arial", fill: "#000", align: "center" };
		for(var i=0;i<scoreboard.length;i++){
			var entryText = scoreboard[i].name + " Score: " + scoreboard[i].score + " seconds";
			this.scoreboardEntries.add(this.game.make.text(this.game.world.width/2+55, this.game.world.height/5+(i*35), entryText, this.style));
		}

		var t = this.game.add.text(this.game.world.width/2+15, this.game.world.height/10+15, "Scoreboard: Top 10 Times", { font: "30px Arial", fill: "#000", align: "center" });
		//Change to top 10 when graphic changes
		for(var i=0;i<9;i++){
			this.scoreboardNumbers.add(this.game.make.text(this.game.world.width/2+25, this.game.world.height/5+(i*35), i+1, this.style));
		}
	},

	updateScoreboard: function(scoreboard){
		this.getScoreboardList(scoreboard);
		scoreboard = this.parseData(scoreboard);
		for(var i=0;i<scoreboard.length;i++){
			this.scoreboardEntries.children[i].setText(scoreboard[i].name + " Score: " + scoreboard[i].score );

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