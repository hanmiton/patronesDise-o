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
	- principio subsitucion liskov
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