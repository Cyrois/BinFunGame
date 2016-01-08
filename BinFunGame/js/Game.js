var BinFunGame = BinFunGame || {};

BinFunGame.Game = function(){};

BinFunGame.Game.prototype = {
	create: function(){

		this.totalRecyclables = 40;
		//set world dimensions
   		this.game.world.setBounds(0, 0, 1280, 720);

   		//White background
   		this.game.stage.backgroundColor = '#fff';

   		//Generate Signs
   		this.generateSigns();

		//Randomly pick one recyclable
		this.generateRecyclable();

		this.playerScore = 0;

		this.score = "score: "+ this.playerScore;
    	style = { font: "20px Arial", fill: "#000", align: "center" };
    	this.score = this.game.add.text(this.game.world.centerX+150, this.game.world.centerY, this.score, style);
		this.score.anchor.set(0.5);

	},
	update: function(){
	},

	generateSigns: function(){
		this.signs =  this.game.add.group();

		//Enable physics
	    this.signs.enableBody = true;
	    this.signs.physicsBodyType = Phaser.Physics.ARCADE;

	    //Generate Signs
		this.foodSign = this.signs.create(this.game.world.centerX-465, 150, 'foodSign');
		this.foodSign.anchor.setTo(0.5);
		this.foodSign.binType = "FoodScraps";
		this.garbageSign = this.signs.create(this.game.world.centerX-155, 150, 'garbageSign');
		this.garbageSign.anchor.setTo(0.5);
		this.garbageSign.binType = "Garbage";
		this.paperSign = this.signs.create(this.game.world.centerX+155, 150, 'paperSign');
		this.paperSign.anchor.setTo(0.5);
		this.paperSign.binType = "Paper";
		this.recyclableContainersSign = this.signs.create(this.game.world.centerX+465, 150, 'recyclableContainersSign');
		this.recyclableContainersSign.anchor.setTo(0.5);
		this.recyclableContainersSign.binType = "RecyclableContainer";
	},

	generateRecyclable: function(){
		//Randomly pick a item and add it in the center of world
		var rand = this.game.rnd.integerInRange(0, (this.totalRecyclables-1));
		this.recyclable = this.game.add.sprite(this.game.world.centerX,this.game.world.centerY,recyclableArray[rand].name);
		this.recyclable.binType = recyclableArray[rand].binType;
		
		this.recyclable.anchor.setTo(0.5);

		//Enable input/drag and centerRecyclable
		this.recyclable.inputEnabled = true;
		this.recyclable.input.enableDrag();
		this.recyclable.events.onDragStop.add(this.centerRecyclable, this);

		//Enable physics on recyclable
		this.game.physics.arcade.enable(this.recyclable);
		this.recyclable.enableBody = true;
		this.recyclable.physicsBodyType = Phaser.Physics.ARCADE;

	},

	centerRecyclable: function(pointer){
		
		this.game.physics.arcade.overlap(this.recyclable, this.signs, this.checkRecyclable, null, this);
		
		pointer.x =  this.game.world.centerX;
		pointer.y =  this.game.world.centerY;
	},

	checkRecyclable: function(recyclable, sign){
		//this.playerScore+= 1;
		//Check if item is placed in correct spot
		if (recyclable.binType == sign.binType){
			this.playerScore+=1;
			this.score.setText("score: "+ this.playerScore);
			recyclable.kill();
			this.generateRecyclable();
		}
	}

};