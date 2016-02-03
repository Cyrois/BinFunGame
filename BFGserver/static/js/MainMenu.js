var BinFunGame = BinFunGame || {};

BinFunGame.MainMenu = function (){};

BinFunGame.MainMenu.prototype = {
	init: function(score) {
	if(score == undefined){
		var score = 9999;
	}
    var score = score;
    if(this.highestScore == undefined){
    	this.highestScore = 9999 ;
    }
    this.highestScore = this.highestScore;

    this.highestScore = Math.min(score, this.highestScore);
   },
	create: function(){
	    //this.game.stage.backgroundColor = '#fff';
	    this.skyBackground = this.game.add.tileSprite(0, 0, this.game.world.width, this.game.world.height-128, 'sky');
	    this.groundBackground = this.game.add.tileSprite(0, this.game.world.height-128, this.game.world.width, 128, 'ground');
	    this.generateClouds();
	    //Title
	    /*
	    var title = "Bin Fun Game";
	    var style = { font: "30px Arial", fill: "#000", align: "center" };
	    var t = this.game.add.text(this.game.width/2, this.game.height/2, title, style);
	    t.anchor.set(0.5);
	    */
	   	var t = this.game.add.sprite(this.game.width/2, this.game.height*1/10, 'bfg');
	   	t.scale.setTo(1.25);
	   	t.anchor.set(0.5);

	   	var emily = this.game.add.sprite(this.game.width/2 -150, this.game.height/3, 'emily');
	   	emily.scale.setTo(0.5);
	   	emily.anchor.set(0.5);

	   	/*
	   	//HighScore
	   	var highScore = "High Score Time: " + this.highestScore;
	   	style = { font: "25px Arial", fill: "#000", align: "center" };
	    var h = this.game.add.text(this.game.width/2, this.game.height/2 + 55, highScore, style);
	    h.anchor.set(0.5);
	    */

	    //Start Game button
		var startButton = this.game.add.button();
		startButton = this.game.add.button(this.game.width/2, this.game.height/2 + 115, 'startButton', this.startGame, this ,1,0,2);
		startButton.anchor.set(0.5);
		//Go to scoreboard
		var scoreboardButton = this.game.add.button();
		scoreboardButton = this.game.add.button(this.game.width/2, this.game.height/2 + 180, 'scoreboardButton', this.submitToScoreboard, this,1,0,2);
		scoreboardButton.anchor.set(0.5);

		var instructions = "Click and drag each item to its correct bin as fast as you can!\nCompete for a highscore on the scoreboard!\n\nClick Info to find out more about Sort It Out UBC";
	   	style = { font: "20px Arial", fill: "#000", align: "center", wordWrap: true, wordWrapWidth: 300 };
	    var h = this.game.add.text(this.game.width/2 +90, this.game.height/3, instructions, style);
	    h.anchor.set(0.5);

		var info = this.game.add.button(this.game.width/2, this.game.height/2 +50, 'infoButton', function() {  
		// open in the same window (like clicking a link)  window.location.href = "http://www.google.com";  
		// open in a new window instead (this will likely be blocked by popup blockers though) 
		window.open("https://sustain.ubc.ca/campus-initiatives/recycling-waste/sort-it-out", "_blank");}, this,1,0,2);
		info.anchor.set(0.5);
		
	},
	update: function(){
		if(this.game.input.activePointer.justPressed()) {
		    //this.game.state.start('Game');
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
	submitToScoreboard: function(){
		this.game.state.start('Scoreboard',true,false,this.highestScore);
	}
};