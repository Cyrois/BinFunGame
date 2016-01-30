var BinFunGame = BinFunGame || {};

BinFunGame.Preload = function (){};

BinFunGame.Preload.prototype = {
	preload: function (){
		//adds a sprite, logo, to center of game. Then sets the anchor point of the sprite in the middle
		this.splash = this.add.sprite(this.game.world.centerX, this.game.world.centerY-64, 'emily');
	    this.splash.anchor.setTo(0.5);

	    this.preloadBar = this.add.sprite(this.game.world.centerX, this.game.world.centerY + 128, 'preloadbar');
	    this.preloadBar.anchor.setTo(0.5);

    	//Sets it as so that it will be cropped horizontally or vertically on the % of the loader in real time
    	//This allows for easy loading bars
    	this.load.setPreloadSprite(this.preloadBar);
    	//Load images
    	this.load.spritesheet('foodSign', 'static/assets/images/signs/green.png',128,128);
    	this.load.spritesheet('garbageSign', 'static/assets/images/signs/black.png',128,128);
    	this.load.spritesheet('paperSign', 'static/assets/images/signs/blue.png',128,128);
    	this.load.spritesheet('recyclableContainersSign', 'static/assets/images/signs/grey.png',128,128);
    	this.load.image('sky', 'static/assets/images/sky.png');
    	this.load.image('ground', 'static/assets/images/ground.png');
    	this.load.image('star', 'static/assets/images/star.png');
    	this.load.image('cloud', 'static/assets/images/cloudClear.png');
    	this.load.spritesheet('startButton', 'static/assets/images/buttons/start_button.png',210,60);
    	this.load.spritesheet('scoreboardButton', 'static/assets/images/buttons/scoreboard_button.png',210,60);
    	this.load.spritesheet('submitButton', 'static/assets/images/buttons/submit_button.png',210,60);
    	this.load.spritesheet('infoButton','static/assets/images/buttons/info_button.png',210,60);
    	this.load.spritesheet('mainMenuButton','static/assets/images/buttons/mainMenu_button.png',210,60);
    	this.load.image('scoreboard','static/assets/images/scoreboard1.png');
    	this.load.image('wall', 'static/assets/images/wall.png');
    	this.load.image('bfg', 'static/assets/images/Logo1.png');
    	this.load.spritesheet('arrow', 'static/assets/images/arrow.png', 96, 96);



    	//Load recyclables
    	var path = "static/assets/recyclables/";
    	//Load recyclables based on types and concatenate them into one array
    	recyclableArray = this.concArrays(recyclableArray,this.loadRecyclables(path,"FoodScraps",10));
    	recyclableArray = this.concArrays(recyclableArray,this.loadRecyclables(path,"Garbage",10));
    	recyclableArray = this.concArrays(recyclableArray,this.loadRecyclables(path,"Paper",10));
    	recyclableArray = this.concArrays(recyclableArray,this.loadRecyclables(path,"RecyclableContainer",10));

	},
	create: function (){

		//loads the MainMenu State
		this.state.start('MainMenu');
	},

	loadRecyclables: function (path,type,size){
		path = path + type + "/";
		var recyclableArray = new Array();
		for(var i = 1;i<=size;i++){
			this.load.image("recyclable_" + type + i, path + type + "_"+ i + ".jpg");
			var recyclable = {name: "recyclable_" + type + i, binType: type};
			recyclableArray[i-1] = recyclable;
		}
		return recyclableArray;
	},

	concArrays: function (mainArray, subArray){
		for(var i = 0;i<subArray.length;i++){
			mainArray[mainArray.length] = subArray[i];
		}
		return mainArray;
	}
};

