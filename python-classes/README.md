## POO
La Programación Orientada a Objetos (POO) es un paradigma de programación que organiza el código en estructuras llamadas objetos, los cuales son instancias de clases. En la POO, todo se considera "de primera clase", lo que significa que los objetos tienen atributos y métodos asociados a ellos.

Una clase es una plantilla o definición que describe las propiedades y comportamientos comunes que tendrán los objetos que se crearán a partir de ella.

Un objeto es una instancia concreta de una clase. Representa una entidad específica y tiene sus propios valores para los atributos definidos en la clase. La instancia es el proceso de crear un objeto a partir de una clase.

La diferencia entre una clase y un objeto radica en que una clase es una entidad abstracta que define la estructura y el comportamiento de los objetos, mientras que un objeto es una entidad concreta creada a partir de una clase.

Un atributo es una característica o propiedad de un objeto. Define el estado y las características de un objeto. Puede ser cualquier tipo de dato, como una variable, una lista, un diccionario, etc.

Los atributos public, protected y private son modificadores de acceso que se utilizan para controlar la visibilidad y el acceso a los atributos de una clase. En Python, no existen atributos estrictamente privados, pero se utiliza la convención de nombrar los atributos con un guion bajo al inicio (_atributo) para indicar que son de uso interno y se recomienda no acceder directamente a ellos desde fuera de la clase. Los atributos sin guion bajo al inicio se consideran públicos y son accesibles desde cualquier parte del programa. Por otro lado, los atributos con doble guion bajo al inicio (__atributo) se consideran privados y Python los renombra internamente para evitar colisiones con atributos de otras clases.

El término "self" se refiere a la instancia actual de una clase y se utiliza dentro de los métodos de la clase para acceder a los atributos y métodos de esa instancia.

Un método es una función definida dentro de una clase que define el comportamiento de los objetos de esa clase. Los métodos pueden acceder y manipular los atributos de un objeto.

El método especial __init__ es un constructor en Python que se ejecuta automáticamente cuando se crea una nueva instancia de una clase. Se utiliza para inicializar los atributos de la instancia.

La abstracción de datos se refiere al proceso de simplificar y representar características esenciales de un objeto, ocultando los detalles innecesarios. El encapsulamiento de datos es el principio de POO que combina los datos y los métodos relacionados en una sola entidad, la clase, y oculta los detalles internos del objeto. La ocultación de información se refiere a la restricción de acceso a ciertos atributos o métodos de una clase, lo que evita el acceso no autorizado y mantiene la integridad de los datos.

Una propiedad es una forma de encapsular un atributo y controlar su acceso mediante los métodos getter y setter. Proporciona una interfaz para leer, escribir o manipular el valor de un atributo.

En Python, la diferencia entre un atributo y una propiedad radica en que un atributo es una variable que almacena un valor, mientras que una propiedad es un atributo especial que tiene métodos asociados para obtener, establecer o eliminar su valor.

La forma pitónica (idiomática) de

 escribir getters y setters en Python es utilizando los decoradores @property, @atributo.setter y @atributo.deleter. Estos decoradores permiten acceder a los atributos como si fueran propiedades directas, ocultando la implementación real de los métodos getter, setter y deleter.

Para crear dinámicamente nuevos atributos en instancias existentes de una clase, se puede utilizar la sintaxis de asignación simple. Por ejemplo, objeto.nuevo_atributo = valor.

Para vincular atributos a objetos y clases, se puede asignar un valor directamente a un atributo dentro de la clase o dentro de un método utilizando "self". También se pueden definir atributos de clase, que son compartidos por todas las instancias de una clase.

El atributo especial __dict__ de una clase o instancia de una clase es un diccionario que contiene los nombres y los valores de todos los atributos definidos en la clase o instancia.

Python busca los atributos de un objeto o clase en varios lugares: primero en la propia instancia (atributos de objeto), luego en la clase y sus superclases (atributos de clase) y finalmente en la clase base de todas las clases (atributos especiales).

La función getattr se utiliza para obtener el valor de un atributo de un objeto dado su nombre. Si el atributo no existe, se puede proporcionar un valor predeterminado para devolver en su lugar.

```python```