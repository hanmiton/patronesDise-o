function testBuilderPattern(){
	var shop = new Director(); //instanciando Directro
	var carBuilder = null;	//varibale con null
	var car = shop.construct(carBuilder);  //variable  llama a shop.construc(null)

	car.doSomethin();

	log.show();
}

function Director(){//director
	this.construct = function(builder){
		builder.step1(); //funciones q vienen de car bulilder se recibe como buildere
		builder.step2();
		return builder.get();
	}
}

function CarBuilder(){
	this.car = null;
	this.step1 = function(){
		this.car = new Car();
	}
	this.step2 = function(){
		this.car.addParts();

	}
	this.getResult = function(){
		return this.car;
	}
}

function Car(){
	this.doors = 0;
	this.addParts = function(){
		this.doors = 4;
	}

	this.doSomethin= function(){
		print('tengo'+ this.doors + 'puertas');
	}
}

testBuilderPattern();//ejecuntando clase