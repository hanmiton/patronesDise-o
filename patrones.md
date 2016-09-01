Patrones de arquitectura
Patrones de Diseño
Raino
	compilador o interprete de javascript
	sin ejecutarlo en el browser
Patrones de diseño
	Sirve para ahcer aplicaciones escalbles
	Estructurar y descomponer en piezas claves de nuestro problema q queremos resolver
	Obligan a pensar en software robusto y matenible
Patrones mas utilizados
	mvc
		modelo,vista, controlador
		descomponer interaccion cliente con la capa de negocio q vive en el servidor
		- aplicaciones orientadasa eventos(sistemas distribuidos)
		event driven arquitecture(eda)
Los patrones no son entes aislados se pueden apoyar de distitntos patrones
Patrones de diseño
	factory method
	abstract factory
comunicacion entre clases
	patrones de estructura
Patron strategy
	identificar de una manera general
creacion de algoritmos
	2 enfoques
patrones 
	no resuleven el problema esencial
	resuelven los problemas exteriores (arquitectura)
capa de integracion
	enterpriser service boss
		bus de comunicacino entre las diferentes app que se van interactuar
isp
	............
gang of 4
	primer libro de reeferencia de diseño
patron fronend
	mvc
patron de comportamiento
orientado a objetos
	encapsular
	y comunicarse por metodos
patron de diseño
	orintado a arquitectura
		mvc
		capas
		eventos
	creacion objetos
	patron q tiene que ver con el comportamiento
tiempo real
comunicacion 
	mensaejs asincronos
	2 enfoques
		push
			capa recibe informacion (momento en que recibe la empujar publishes subcritbe)
			cuando se registran (por ejemplo una estacion de radio)
Informacion patrones de diseño
	posa (clasico para referencai de patrones)
	martin folder(pattern for enterprise applications)

Patrones
	ver patters of enterprise application arquitecture
	"Cada patrón describe un problmea que ocurre una y otra vez en nuesto mmedio amiente y, a conitnuacion describe el nucleo d ela solucion a ese problema, de tal manera qeu se pueda tulizar esta solucion un llion de veces, sintener que hacerlo de la misma manera dos veces"
Que es patron ingenieria de software
	Describe una solucion reutilizable a un problmea comun en un contexto dao.
	Se enfoca en la solucion, no en el problema
	Identifica responsabilidaddes e interaciciones entre los particpantes.
que no es
	paradigma de programacion
		programacion objetos
		programacion funcional 
		logica
	no es un silver bullet
	no es una solucion inefectiva y riesgosa (soluciones probadass)
	no resuelve un problema especifico
	no depende del legunaje de programacion
Para q sirve patron de diseño?
	Vocabulario y entendimiento común para el diseño de software
	- Alternativas de diseño para que sea flezible y reutilizable
	- Construir arquitecturas de fotware complejas y heterogeneas
	- favorece la vida y amntenibilidad de una plicacion
Patron Layers
	patron de arquitectura
	layer como un stack (cada capa tiene comunicacion)
	app grande que necesita descomposicion
	- grupos de subtareas
	Participantes
		Clase
			clase en este caso layer
		Colaborador
			clase ocn la que se comunica
		Responsabilidad
			las responsabilidades q tiene dicha capa
	layers
		cliente
		Layer N (alta abstraccion)
		.
		.
		Layer 1 (capa de abstracicon mas basica)
	Ejemplo ptron layers
		Capara presentacion
			interfaz de usuario
		Capa Logica
			negoico funcional
		Capa de datos
			almacenamiento de datos
	modelos osi
		va respuestas arriba hacia abajo
		y devuleve de abajo hacia arriba
	cada layer tiene servicios q da a su capa superior y a su vez se apoya de sus capas inferiores para construir su logica interna

SOA
	Service oriented arquitecture

Patron layer
	independencia de las piezas
	malo
		dependencia capa inferior

Categoiras y patrones de diseño
	libros(posa,...)

Sintomas mal diseño
	- Rigidez
		Dificil de modificar
	- Fragilidad
		una modificacion afecta a los demas modulos
	- Inmovilidad
		Que si se mueve a dicho modulo daña todo
	- Viscosidad
		Dificil hacer q fluja la informacion diferentes componentes

Principios SOLID de DOO
	- Principio de reponsabilidad unico
		solo va tener una razon para poder modificarse
	- open closed Principle
		clases facilmente extensibles y cerradas para q no se modifiquen
		herencia adecuada
	- principio subsitucion lislov
		poder definir clases derivadas deben ser sustituibles por la clases base
	- principo de segregacin interface
		hacer interfaces segregadas especificas del cliente
	- principio inversion de dependencia
		depender de las abstraccion de las clases bases y no de las derivadas

Categorias de ptraones (POSA)
	Patrones de artuitecuta
		layers, mvc eda
			sistema grande en subsistemas y la comunicacion y realcion existente
	Patrones de diseño
		factorey method, Facade, Strategy, Observer
			mas especializados
			como cada modulo esta implementado
			comunicacion para solucion
		Idioms/modismos
			Menjo de memoria
			uso de lenguaje
			convenciones nombrado
				usar el lenguaje
Clasificacion de patrones de diseño
(GoF)
	Proposito
		Refleja lo que hace un patron
		Patrones de creacion
			objetos
		Estructura
			componer clases u objetos mas complejos
		comportamiento
			interaccion entre calses y objesto dependendiendo de la responsabildiad
	Alcance
		se aplica a objeto o clases
		patrones de clases y objetos
			clases
				teimpo compilacion
				tiempo ejecuion
			objetos
				instancio como va interactuar

Divison patrones
	(proposito,alcance)
	(Creacion,Clase)
		FactoryMethod
	(Estrucutra,clase)
		adpater
	(comportamiento,clase)
		Interpreter
		template method
	(creacion, objeto)
		Abstract factory
		builder
		prototype
		singleotn
	(estructura,objeto)
		adapter
		bridge
		composite
		decorator
		facade
		fleweight
		proxy
	(comportamient,objeto)
		chain of repsoilbility
		command
		iterator
		mediator
		memento
		observer
		state
		startegy
		visitor
Patrones de diseño (creacionales)
	FactoryMethod
		Crea una instancia de varias clases derivadas
		clase bases se crean varias clases
		abstraer forma correcta de instanciar
		indireccion
	Abstract Factory
		Crea una instancia de varias familias de clases
		ejemplo animales mamiferon, no mamiferos, de hay crearmos mas clases de distintos tipso
	Builder
		Serara la construcicon de un objeto de su representacion

	Prototype
		a fully initialized instance to be copied or cloned
		generacion de prototipos
		previamente inicializados
		clonar y copiar

	Singleton
		Aclass of which only a single instance can exist
		asegurar q solo exista una instancaid entro de toda la app
		Conexion base de datos
			objeto unico y establecer base de datos
Patron Builder
	Builder class
		interface abstracta para crear parte de un objeto
	ConcreteBuilder
		construi y poner juntas partes de un producto y implementa builder interface
	Director class
Ciclo builder
Director->Builder->ConcreteBuilder->Product

//ver clases abstractas javascript (no es recomendable)

controller ve la comunicacion entre layers

layers
	ventaja
		dividir
		exponer servicios
	desventaja
		dependencia aservicios expuestos
Builder
	ventaja
		cliente no conoce como se construye el objeto
		se delega construccion al builder
	desventaja
		duplicidad de clases

Recomendacon lengujaes oreintados a objetos

Patron mas recomendado pra web
	MVC

------------pregutas y respuestas 2 

asociar nombre mas de negocio donde se va utilizar

patornes
	dividimos en 3 bloques
		cmo creo un objeto
			igual se lo usa en lengujaes funcionales
		partonre sde comportameinto
			paradigma funcional
				interaccion muy nautral

builder
	tenga diferentes paretes
		cada parte se la crea dinamicamente
	el builder no se gnera la instancia en el memoento
	si no se añaden los componentes dinamicamente

patrones para bases de datos
	data access layer
	data access object
MIT
	Programcion funcional
patrones mas usados
	mvc
	strategy (poder identificar algoritomos independiente mente dle objeto)
	observer(comunicacion de un objeto ocn otors que estan escuchando)
singleton
	te da la misma instancia del objeto
		integiradad instacia
		integridad de la inforamcion

Fatory method(interface)
	Product
		objeto qeu se desea construir
	ConcreteProduct
		implementacion de la interface producto
	Creatro(FActory)
		fabrica de los metodos
	ConcreteCreator
		sobreescribe el metodo

Abstract factory
	biblioteca de clases de productos
	creacion de clases(noproductos para eso usamos factory method)
	Abstract Factory
		delcara una interfaz
	ConcreteFactory
		implementa operacoines para crear product ocncretos
	AbstractProduct
		declara una interfaz para un tipo de objetos
	Product

Singleton
	nos van ayudar a construir objetos
	conexines base de datos
factory metohod 
	el mas usasdo
builder cunado el objeto es muy complejo

Notas patrones de creacion
|Abstract factory tien eel objeto factry produciendo objetos de varias clases
	Builider
		tiene el objeto factroy construyendo un porducto incrementalmente suando una estructura compleja
	AbstractFactry
		A menudo osn implementadas uasando Factory Methods pero tambien pueden ser implmenentadas usando Prototype
	Builider
		construir objetos complejos paso ap os
	Abstract FActory
		familia de objetos 

Patrones de estructura
	Adapter
		Relaiona interfaces de diferentes calses
	Bridge
		Separa la interfaz de un ojeto de su implementacino
	Composite
		Estructra de arbol de objeto ssimples y compuestos
	Decoradtor
		Añadir responsabilidades a los objetos dinamicamente
	Facade
		Una unica clase que representa todo un subsistema
	Flyweight
		Una instancia usada para comparticion eficiente
	Proxy
		Un objeto q representa a otro objeto
Patrones de estrutura
	Adapter
		como un adaptador
		Relaciona dos componente qeu no tiene una interfaz ocmun

		Target
			interfaz de dominio especifico que utiliza Client
		Adapter
			adpta la interfaz Adaptee para la interfaz de destino
		Adaptee
			define una interfaz existente qeu necesita adaptarse
		Client
			interactau con el target (target interacuta con el adpater)

Patron Facade
	encapsular toda la compelijidad provee una interfaz simpoel a un subsistema complejo

Flightweigth
	para q el codigo sea menos efectivo y mas efeciente
Interface
	repositori
	descripcion de metodos los cuales se enetnra definido en una clase
Inyeccion de dependencias es un principio(SOLID)

Principios SOLID de DOO
	S Una clase debe tener una y solo una razon para cmabiar
	O Deberia poder de extender comportameinde clases sin modificarlo
	L Las clases derivadas de ben ser sustituibles por sus clases base
	I Hacer interfaces detalladas que son especificas del cleinte
	D Depende de abstracciones, no de ocncreciones
UML
	...............
	definir casos de usos

Decorator
	Añada reponsabilidades al los objetos de forma dinamica
	tambien connociodo como wrapper
	adjuntar responsabilidaddesa adicionales a un objeto de fomra dinamica
	proporciona uana alterantiva
	Compoente
		Intrefaz para objetos que peuden tener rersposabildladdes aañadidas dinamicamente
	ConcreteComponent
		Define un objeto al cual se le puede ñadir
		responsabilidades adicionales
	Decorator
		mantienre una referendai al objeto Componet y fefine una intrefaz que cumple con la intrefaz de Component
	Concrete Decorators
		exteinde la funcionalidad de component
 adapter 
 	modifica la interfaz
 proxy
 	toma objeto intermiedo y añada ciertas funionlaidades
 decoratro
 	aumenta 
 	interfaz similar pero la instacia tiene valor adicional
 facade y singleton
 	no se necesita mas de una instancia q me permita dicha interaccion
Patrones de ocmportamiento
	Chain of responsability
		Capacidad poder encadernar una seri de objetos para pasarles al misma peticionSS
		Accin se ejecutra en los metodos
	Command
		Encapsualr una peticon de ocmandos como un objeto
		Una accin se encapsula dentro de una clase
	Interprete
		Incluir elemento sdel lenguaje en un programa
	Iterator
		Acceso secuencias a los elementos de una coleccion
	Mediator
		Define una comunicacino simplificada entre clases
	Memento
		Captura y restarua el estado interno de un objeto en ejecucion
		Guarda estado del objeto por cada avance para permitir regreso
	Observer
	State
		como maquina de estado
		wizzard cambienado la interaccin que itene ocn el de acuerdo a l estado en que esta
	Template mehtod
		Difiere los pasos exactos de un algoritmos a una sublcase
Patron command
	(Action, Transaction)
	Especificar, encolar y ejecutra peticiones en diferentes eimpos
	Callbacks
	Command
		Declara una intrefaz para ejecutra una opoeracion
	ConcreteCommand
		Exteinde Command
		Implementa metodo execuete
		REceiver
			Sabe ocmo se deben ejecutra las operaciones
	Invoker
Patron Observer
	Dependets, Publish-Subscribe
	Notifica a participantes y ya pueden realizar la operacion cuando se cambia de estado
	Dependencia de uno a muchos

Observer
	Observable
		Declara una intrefaz apra añadir oremover Observers del cliente
	ConcreteObservable
		Extiende Observable. Mantiene el estado del objeto y cuano cambia, notifica a los Observers ligados
	Observer
		Interfaz q define las operaciones a ser usadas para notificas a seste objeto
	ConcreteObserverA, Concrete Observer2
	Implementacino concretas de Observer
		Metodo notify
			seencarga de correr a toda la lista de observer que se haayn registrado en el 
Strategy
	Stratygy
		delcara la interface
	Concrete Strategy
		Cada concrete straetgy implementa el algoritmo
	Context
		manteine la referecncia dle objeto
		y dice si se ejecuta uno o el otro
Chain of responsibility
	puede usar command para regrepsentar peticones como objetos
bojetos Stare a menudo don Singleotns

Strategy te permite cmabiar la parte interna de un objet, mientras de Decoratro lo hace externamente

MVC
|dificir en tres componente s
	modelo 
	vista 
	controlador
		implementacon de un patron observer
		controller indica que algo cmabio y model y view son los q esta a escucha
Event-driven-Arquitectura
	emitters
		recojeon lso eventos
	channels
		conductos por donde va el mensaje
	consumirs 
		son los que consumen los eventos
Diferencia 
	Extendemos creando nueva clases y objetos con eso especifico
	decorator
		a una instancia le estamos añadiendo un comportameinto
Core j2ee patterns
	leer para empezar la programcacin en java
Ver patron DAO
Pregutnas

State patorn
El patrón de diseño State se utiliza cuando el comportamiento de un objeto cambia dependiendo del estado del mismo

Medietro
El patrón mediador define un objeto que encapsula cómo un conjunto de objetos interactúan
Proxy
El patrón Proxy es un patrón estructural que tiene como propósito proporcionar un subrogado ... puedan usar de manera indistinta. La clase SujetoReal: clase del objeto real que el proxy representa
Strategy
El patrón Estrategia (Strategy) es un patrón de diseño para el desarrollo de software. Se clasifica como patrón de comportamiento porque determina cómo se debe realizar el intercambio de mensajes entre diferentes objetos para resolver una tarea. El patrón estrategia permite mantener un conjunto de algoritmos de entre los cuales el objeto cliente puede elegir aquel que le conviene e intercambiarlo dinámicamente según sus necesidades.
Patrones arquitectura
Programación por capas
Tres niveles
Pipeline
Invocación implícita
Arquitectura en pizarra
Arquitectura dirigida por eventos, Presentación-abstracción-control
Peer-to-peer
Arquitectura orientada a servicios
Objetos desnudos
Modelo Vista Controlador
Singleton
	es un patrón de diseño diseñado para restringir la creación de objetos pertenecientes a una clase o el valor de un tipo a un único objeto.

Su intención consiste en garantizar que una clase sólo tenga una instancia y proporcionar un punto de acceso global a ella.
Visitor
	En programación orientada a objetos, el patrón visitor es una forma de separar el algoritmo de la estructura de un objeto.

Falladas (estudiaar)
	En que se enfoca un patron
		-----
	Posa categorias
		arquitecture,creacion,comportameinto
	Que patron de arquitectrau regresa el objeto de inmediato
		factory method
	Que patorn de diseño ayudan a relacionar  2 objeton sin intreface comun
		facade
	Que patron de disñeo serap la interface de la implementacion 
		facade
	En que caso utilizamos el paton Strategy
		para 2 algoritmos independientes
	Que patorn me permite definir un nueva operacion de la clase sin cambiarla
		---------
	Que patorn me ayuda encapsular una petion como objeto
		request
hola