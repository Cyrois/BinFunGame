var BinFunGame = BinFunGame || {};

BinFunGame.Boot = function(){};

BinFunGame.Boot.prototype = {
  preload: function() {

    this.load.image('emily', 'static/assets/images/Emily.png');
    this.load.image('preloadbar', 'static/assets/images/loading_bar.jpg');
  },
  create: function() {
  	//loading screen will have a white background
    this.game.stage.backgroundColor = '#fff';

    //scaling options
	this.scale.scaleMode = Phaser.ScaleManager.RESIZE;
  this.scale.minWidth = 240;
  this.scale.minHeight = 170;
  this.scale.maxWidth = 1280;
  this.scale.maxHeight = 1024;
	
	//have the game centered horizontally
	this.scale.pageAlignHorizontally = true;

	//physics system for movement
	this.game.physics.startSystem(Phaser.Physics.ARCADE);
    
    //loads the Preload state
    this.state.start('Preload');
  }
};