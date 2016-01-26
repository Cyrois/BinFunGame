var BinFunGame = BinFunGame || {};

BinFunGame.Game = function(){};

BinFunGame.Game.prototype = {
	create: function(){

		this.totalRecyclables = 40;
		this.maxScore=5;

		//set world dimensions
   		this.game.world.setBounds(0, 0, this.game.width, this.game.height);

   		//White background
   		this.game.stage.backgroundColor = '#9c9c9c';
   		this.floor = this.game.add.tileSprite(0, 0, this.game.world.width, this.game.world.height/2, 'wall');

   		//Generate Signs
   		this.generateSigns();

		//Description
		var description = "Click to start the game!";
	    style = { font: "25px Arial", fill: "#000", align: "center" };
		this.d = this.game.add.text(this.game.width/2, this.game.height/2 + 150, description, style);
		this.d.anchor.set(0.5);

		var mainMenuButton = this.game.add.button();
		mainMenuButton = this.game.add.button(0, 0, 'scoreboardButton', this.goToMainMenu, this,1,0,2);

		this.intro();

		this.gameRunning = false;
		this.endGameScreen = false;


	},
	update: function(){
		if(this.gameRunning==false){
			if(this.game.input.activePointer.justPressed()) {
		    	this.endIntro();
		    	this.gameRunning=true;
		    }
		}
		if(this.endGameScreen==true){
			if(this.game.input.activePointer.justPressed()){
				this.game.state.start('MainMenu', true, false, this.timerCount);
			}
		}
	},

	goToMainMenu: function(){
		this.game.state.start('MainMenu', true, false);
	},

	intro: function(){
		//Add arrow animation
		this.arrows =  this.game.add.group();

		this.arrow_0 = this.arrows.create(this.game.world.centerX-400, this.game.world.centerY+50, 'arrow');
		this.arrow_1 = this.arrows.create(this.game.world.centerX-140, this.game.world.centerY+50, 'arrow'); 
		this.arrow_2 = this.arrows.create(this.game.world.centerX+140, this.game.world.centerY+50, 'arrow');
		this.arrow_3 = this.arrows.create(this.game.world.centerX+400, this.game.world.centerY+50, 'arrow');
		this.arrows.callAll('anchor.set','anchor',0.5);
		this.arrows.callAll('animations.add','animations', 'move',[0, 1, 2, 3, 4, 5], 8, true);
		this.arrows.callAll('animations.play', 'animations','move');
	},

	endIntro: function(){
		this.d.destroy();
		this.arrows.forEach(function(sprite){
			sprite.kill();
		},this,true);
		
		this.introCountDown();
		
	},

	introCountDown: function(){
		var count = 3;
	    var style = { font: "50px Arial", fill: "#000", align: "center" };
		var d = this.game.add.text(this.game.width/2, this.game.height/2 + 125, count, style);
		d.anchor.set(0.5);
		
		this.game.time.events.repeat(Phaser.Timer.SECOND, 3,function(){
			count--;
			d.setText(count);
			console.log(count);
			if(count==0){
				d.destroy();
				this.startGame();
			}
		}, this);

		
	},

	startGame: function(){
		this.generateRecyclable();
		this.game.time.events.start();

		this.playerScore = 0;
		//Create Score text
		this.score = "score: "+ this.playerScore;
    	style = { font: "30px Arial", fill: "#000", align: "center" };
    	this.score = this.game.add.text(this.game.world.centerX+150, this.game.world.height-50, this.score, style);
		this.score.anchor.set(0.5);

		//Create time
		this.timerCount=0;
		this.timer = "Total time: "+ 0;
		style = { font: "30px Arial", fill: "#000", align: "center" };
		this.timer = this.game.add.text(this.game.world.centerX-200, this.game.world.height-50, this.timer, style);
		this.timer.anchor.set(0.5);

		this.game.time.events.loop(10, this.updateCounter, this);
	},

	checkEndGame: function(score){
		if(score >= this.maxScore){
			this.endGame();
		}
	},

	endGame: function(){
		this.game.time.events.stop();
		this.recyclable.inputEnabled = false;
		this.timerCount = this.timerCount.toFixed(2);
		this.endGameScreen = true;

		//Game Over text
		var description = "GAME OVER";
	    style = { font: "40px Arial", fill: "#000", align: "center" };
		this.d = this.game.add.text(this.game.width/2, this.game.height/2 + 200, description, style);
		this.d.anchor.set(0.5);


	},


	updateCounter: function(){
		this.timerCount+=0.01;
		this.timer.setText("Total time: "+ this.timerCount.toFixed(2));

	},

	generateSigns: function(){
		this.signs =  this.game.add.group();

		//Enable physics
	    this.signs.enableBody = true;
	    this.signs.physicsBodyType = Phaser.Physics.ARCADE;

	    var style = { font: "22px Arial", fill: "#FFF", align: "center" };
	    var foodText = this.game.add.text(this.game.world.centerX-370, this.game.world.centerY-140, 'Food Scraps', style);
	    var recyclableContainerText = this.game.add.text(this.game.world.centerX-135, this.game.world.centerY-135, 'Recyclable\nContainers', { font: "18px Arial", fill: "#FFF", align: "center" });
		var paperText = this.game.add.text(this.game.world.centerX+145, this.game.world.centerY-140, 'Paper', style);
		var garbageText = this.game.add.text(this.game.world.centerX+370, this.game.world.centerY-140, 'Garbage', style);
		foodText.anchor.setTo(0.5);
		recyclableContainerText.anchor.setTo(0.5);
		paperText.anchor.setTo(0.5);
		garbageText.anchor.setTo(0.5);

	    //Generate Signs
		this.foodSign = this.signs.create(this.game.world.centerX-370, this.game.world.centerY-100, 'foodSign');
		this.foodSign.anchor.setTo(0.5);
		this.foodSign.binType = "FoodScraps";


		this.recyclableContainersSign = this.signs.create(this.game.world.centerX-140, this.game.world.centerY-100, 'recyclableContainersSign');
		this.recyclableContainersSign.anchor.setTo(0.5);
		this.recyclableContainersSign.binType = "RecyclableContainer";

		this.paperSign = this.signs.create(this.game.world.centerX+140, this.game.world.centerY-100, 'paperSign');
		this.paperSign.anchor.setTo(0.5);
		this.paperSign.binType = "Paper";

		this.garbageSign = this.signs.create(this.game.world.centerX+370, this.game.world.centerY-100, 'garbageSign');
		this.garbageSign.anchor.setTo(0.5);
		this.garbageSign.binType = "Garbage";

		this.signs.callAll('animations.add','animations','correct', [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0], 8, false);
		this.signs.callAll('animations.add','animations','wrong', [0, 5, 0, 5, 0], 8, false);
		this.signs.callAll('scale.setTo','scale',2);
	},

	generateRecyclable: function(){
		//Randomly pick a item and add it in the center of world
		var rand = this.game.rnd.integerInRange(0, (this.totalRecyclables-1));
		this.recyclable = this.game.add.sprite(this.game.world.centerX,this.game.world.centerY+125,recyclableArray[rand].name);
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
		pointer.y =  this.game.world.centerY+125;
	},

	checkRecyclable: function(recyclable, sign){
		//this.playerScore+= 1;
		//Check if item is placed in correct spot
		if (recyclable.binType == sign.binType){
			this.playerScore+=1;
			this.score.setText("score: "+ this.playerScore);
			sign.animations.play('correct');
			this.scoreEmitter();
			recyclable.kill();
			this.checkEndGame(this.playerScore);
			if(this.endGameScreen == false){
				this.generateRecyclable();
			}
		}
		else{
			sign.animations.play('wrong');
		}

		
	},

	scoreEmitter: function(){
		var emitter = this.game.add.emitter(this.recyclable.x, this.recyclable.y, 50);
	    emitter.makeParticles('star');
	    emitter.minParticleSpeed.setTo(-200, -200);
	    emitter.maxParticleSpeed.setTo(200, 200);
	    emitter.gravity = 1000;
		emitter.start(true, 1000, null, 100);
	}

};