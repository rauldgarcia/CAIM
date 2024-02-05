Instituto de Investigaciones en Inteligencia Artificial - Universidad Veracruzana

**Aprendizaje Automático Algoritmo CAIM**

El algoritmo CAIM desarrollado por Lukasz A. Kurgan y Krzysztof J. Cios, sirve para discretizar variables continuas para posteriormente ser procesadas por algoritmos de aprendizaje automático. La finalidad es encontrar la mejor combinación de rangos en los cuales clasificar los datos de la variable a discretizar, sin perder información relevante para el entrenamiento y que los datos sean lo suficientemente representativo del problema a resolver. Este algoritmo es de discretización supervisada, ya que se necesita saber las clases a las que pertenece cada ejemplo y busca maximizar la interdependencia entre la clase y el atributo y generar el menor numero posible de intervalos discretos, ademas de no necesitar que el usuario defina un número especifico de intervalos.

El algoritmo CAIM requiere un conjunto de M ejemplos, donde cada ejemplo pertenece a solo una clase S, ademas cada uno de los valores continuos que tiene la variable en el conjunto de ejemplos se denomina como F. Existe un esquema de discretización D en F con n numero de intervalos: 

![](Aspose.Words.0531b61e-ebb4-4f07-974d-7e5f088507b7.001.png)

D0 es el valor mínimo y dn es el valor máximo del atributo en F y los valores están acomodados de manera ascendente. Estos valores de intervalos son posteriormente utilizados para crear la matriz quanta:

![](Aspose.Words.0531b61e-ebb4-4f07-974d-7e5f088507b7.002.png)

Para el calculo del valor se utiliza la siguiente formula: 

![](Aspose.Words.0531b61e-ebb4-4f07-974d-7e5f088507b7.003.png)

Donde n es el número de intervalos, r itera a través de todos los intervalos, maxr es el valor máximo entre todos los valores qir (valor máximo de la columna r) M+r es el total de valores continuos del atributo F que están dentro del intervalo (dr-1, dr].

Pseudocodigo:

` `Paso 1:

1. Encontrar el valor máximo dn y mínimo d0 de Fi
1. Formar un conjunto de todos los valores distintos de Fi, colocados en orden ascendente, crear una variable B que contendrá la siguiente información: d0, todos los valores intermedios sin repetir, dn.
1. Crear una variable D que contendrá el esquema de discretización e inicializara con D:{[d0, dn]} y GlobalCAIM=0

Paso2:

1. Inicializar una variable K=1
1. Tentativamente agregue algún limite de B que no se encuentre en D y calcular su correspondiente CAIM
1. Después de todas las posibles adiciones han sido probadas aceptar la de mayor valor de CAIM
1. si (CAIM>GlobalCAIM o K<S) entonces actualizar D con el aceptado en el paso 2.3 y establecer GlobalCAIM=CAIM, si no terminar
1. establecer K=K+1 y repetir a partir de 2.2

Al probar con la base de datos de Iris encuentra que los mejores intervalos para discretizar son los siguientes:

SepalLengthCm

El mejor intervalo de discretización es: [[4.3, 4.35], [4.35, 5.8], [5.8, 7.9]]

SepalWidthCm

El mejor intervalo de discretización es: [[2.0, 2.1], [2.1, 4.0], [4.0, 4.4]]

PetalLengthCm

El mejor intervalo de discretización es: [[1.0, 1.05], [1.05, 1.9], [1.9, 6.9]]

PetalWidthCm

El mejor intervalo de discretización es:

[[0.1, 0.15000000000000002], [0.15000000000000002, 0.4], [0.4, 2.5]]

Y al utilizar la base de datos discretizada para clasificación con el algoritmo Naive Bayes en WEKA, se obtiene una precisión de 78.66%, el cual al compararlo con el algoritmo interno de WEKA para discretizar resulta ser de menor precisión, ya que con el de WEKA se obtiene una precisión de 96%, por lo cual habría que mejorar el algoritmo para obtener mejores resultados al obtenido.

Referencias:

Kurgan, Lukasz & Cios, Krzysztof. (2004). CAIM discretization algorithm. Knowledge and Data Engineering, IEEE Transactions on. 16. 145- 153. 10.1109/TKDE.2004.1269594. 
Aprendizaje Automático
