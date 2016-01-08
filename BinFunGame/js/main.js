var BinFunGame = BinFunGame || {};

BinFunGame.game =  new Phaser.Game(window.innerWidth, window.innerHeight, Phaser.AUTO, '');

BinFunGame.game.state.add('Boot',BinFunGame.Boot);
BinFunGame.game.state.add('Preload',BinFunGame.Preload);
BinFunGame.game.state.add('MainMenu',BinFunGame.MainMenu);
BinFunGame.game.state.add('Game',BinFunGame.Game);

//Make Global
recyclableArray = new Array();

BinFunGame.game.state.start('Boot');