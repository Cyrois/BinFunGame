var BinFunGame = BinFunGame || {};

BinFunGame.MainMenu = function (){};

BinFunGame.MainMenu.prototype = {
	create: function(){
	    this.game.stage.backgroundColor = '#fff';

	    //Title
	    var title = "Bin Fun Game";
	    var style = { font: "30px Arial", fill: "#000", align: "center" };
	    var t = this.game.add.text(this.game.width/2, this.game.height/2, title, style);
	    t.anchor.set(0.5);
	    
	    //Description
	    var description = "Click to begin";
	    style = { font: "15px Arial", fill: "#000", align: "center" };
		var d = this.game.add.text(this.game.width/2, this.game.height/2 + 50, description, style);
		d.anchor.set(0.5);
	},
	update: function(){
		if(this.game.input.activePointer.justPressed()) {
		    this.game.state.start('Game');
		}
	}
};