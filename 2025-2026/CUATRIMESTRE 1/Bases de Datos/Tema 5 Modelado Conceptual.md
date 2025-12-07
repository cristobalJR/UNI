# Etapas del modelado conceptual

 ![[Tema 5 Modelado Conceptual(etapasModeladoConceptual).png]]
# Modelado conceptual
¿Cómo pasamos del esquema percibido al esquema conceptual?
➢ Transformas frases en <u>lenguaje natural</u> a <u>elementos modelo E/R</u>
Para ello utilizamos el enfoque lingüístico *Chen*:
1. Un substantivo como sujeto o complemento directo, es en general, una entidad, aunque podría ser atributo
2. Los nombres propios suelen indicar ejemplares de una entidad
3. Un verbo transitivo o una frase verbal es una interrelación
4. Una preposición o frase preposicional entre dos nombres suele ser una interrelación, o también puede establecer una asociación entre una entidad y sus atributos.
5. Otras consideraciones:
	**a)** Los verbos ser y tener
	- "ES UN": corresponde al concepto de generalización
	- "Tiene": Según la acepción del verbo, puede corresponder a
		- Una interrelación general entre entidades
		- Una asociación de las entidades con sus atributos
	**b)** El número de las entidades (singular/plural) puede implicar ciertos tipos, cardinalidades o grados de las interrelaciones
	**c)** Es preferible considerar el objeto de datos como entidad, en lugar de como atributo, en los siguientes casos:
	- Si el objeto de datos tiene asociados otros atributos
		- Si las áreas de un departamento tienen a su vez otros atributos, como responsables de área, fecha, etc... conviene crear una entidad AREA
	- Si el objeto de datos estuviese relacionado con otras entidades.
		- Si el área la hubiéramos considerado como un atributo de departamento, no podríamos reflejar las posibles interrelaciones existentes entre las áreas y los empleados.
	**d)** Un mismo atributo no puede aparecer en distintas entidades de datos. Si esto ocurre debemos plantearnos la existencia de una interrelación no identificada entre dichas entidades