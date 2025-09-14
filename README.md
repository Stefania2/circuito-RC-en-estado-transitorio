El código ejecuta programma que permite análizar un circuito RC en estado transitorio, el algoritmo que se ejecuta se basa en la constante
de tiempo (τ), y se calcula como el producto de la resistencia y la capacitancia (τ=R⋅C). El voltaje en el capacitor en función del tiempo (t)
se puede calcular con la fórmula:  

$$
V_{out}(t) = V_{in} \left( 1 - e^{-\frac{t}{\tau}} \right)
$$

Donde: 
• Vout(t) es el voltaje en el capacitor en el tiempo t.
• Vin el voltaje de entrada.
• Ҽ es la base del logaritmo natural (aproximadamente 2.71828).
• τ es la constante de tiempo del circuito

Este programa solicita al usuario ingresar el valor de la resistencia, la capacitancia, el voltaje de entrada y el número de tiempos a analizar. 
Luego, para cada tiempo ingresado, calcular y mostrar el voltaje en el capacitor.

Referencia:
Universidad Nacional Abierta y a Distancia. (s. f.). Lenguajes interpretados: Anexo 2 - Tarea 2 - Elementos constitutivos del lenguaje de programación.
Vicerrectoría Académica y de Investigación, ECBTI, Programa de Ingeniería Electrónica
