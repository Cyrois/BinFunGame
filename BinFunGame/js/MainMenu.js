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

	    //Title
	    var title = "Bin Fun Game";
	    var style = { font: "30px Arial", fill: "#000", align: "center" };
	    var t = this.game.add.text(this.game.width/2, this.game.height/2, title, style);
	    t.anchor.set(0.5);

	   	//HighScore
	   	var highScore = "High Score Time: " + this.highestScore;
	   	style = { font: "25px Arial", fill: "#000", align: "center" };
	    var h = this.game.add.text(this.game.width/2, this.game.height/2 + 50, highScore, style);
	    h.anchor.set(0.5);

	    //Description
	    var description = "Click to begin";
	    style = { font: "15px Arial", fill: "#000", align: "center" };
		var d = this.game.add.text(this.game.width/2, this.game.height/2 + 100, description, style);
		d.anchor.set(0.5);
	},
	update: function(){
		if(this.game.input.activePointer.justPressed()) {
		    this.game.state.start('Game');
		}
	}
};