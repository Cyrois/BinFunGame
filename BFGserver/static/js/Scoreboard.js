var BinFunGame = BinFunGame || {};

BinFunGame.Scoreboard = function (){};

BinFunGame.Scoreboard.prototype = {
	init: function(score) {
    console.log(score);
	if(score == undefined){
		var score = 9999;
	}
    this.score = score;
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
		this.scoreboardList = [{name:"Bob",score:5.5},{name:"Bill",score:6.4},{name:"Andy",score:8.4}];
		this.displayScoreboard(this.scoreboardList);


	},
	update: function(){
	},

	startGame: function(){
		this.game.state.start('Game');
	},

	submitScore: function(){
		if(this.score!=null){
			this.scoreboard.push(this.score);
			this.score=null;
		}
	},

	displayScoreboard: function(scoreboard){
		var scoreboardBackground = this.game.add.sprite(this.game.world.width/2, this.game.world.height/10, 'scoreboard');
		scoreboardBackground.scale.setTo(1.5);


		this.scoreboardEntries = this.game.add.group();
		var style = { font: "20px Arial", fill: "#000", align: "center" };
			
		for(var i=0;i<scoreboard.length;i++){
			var entryText = scoreboard[i].name + " Score: " + scoreboard[i].score + " seconds";
			this.scoreboardEntries.add(this.game.make.text(this.game.world.width/2+55, this.game.world.height/5+(i*35), entryText, style));
		}

		this.scoreboardEntries.add(this.game.make.text(this.game.world.width/2+15, this.game.world.height/10+15, "Scoreboard: Top 10 Times", { font: "30px Arial", fill: "#000", align: "center" }));
		//Change to top 10 when graphic changes
		for(var i=0;i<9;i++){
			this.scoreboardEntries.add(this.game.make.text(this.game.world.width/2+25, this.game.world.height/5+(i*35), i+1, style));
		}
	}

};