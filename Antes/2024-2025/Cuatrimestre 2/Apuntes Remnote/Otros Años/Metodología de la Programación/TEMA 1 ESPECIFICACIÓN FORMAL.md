-  _**1.1. Introducción**_  
    - Cuando se diseña un algoritmo se especifica y luego se implementa.
    - Especificación: Detallar cuidadosamente el problema a resolver
        - Destino:
            - Usuarios: La especificación debe recoger todo lo necesario para el uso correcto del algoritmo.
            - Implementador: Recoge los requisitos que cualquier implementación válida debe recoger.
        - El lenguaje natural no permite la precisión requerida si no se sacrifica la brevedad, lo cual es imprescindible en las especificaciones.
-  _**1.2. Lógica de proposiciones**_  
    - El punto (.) significa tal que.
    - Sintáxis:
        - ![](https://remnote-user-data.s3.amazonaws.com/4yILLNTsaCEFZkINGzeXJfPX6AAvUMSWj9us7OKmBxcND0EBuqfEErza-7qas75_lCF1BzwXhMD2nQu_DVygZtbXhvX7COrKnKZvi4oR0zV5LLdcXH3baaVprUbIupXR.png) 
    - Semántica:
        - Asigna a cada sentencia un valor de verdad, proponiendo diferentes valores concretos a cada variable proposicional.
            - Tablas de verdad: Presenta todas las interpretaciones posibles de las variables y les otorga valores de verdad a cada interpretación.
            - ![](https://remnote-user-data.s3.amazonaws.com/1l5Cy2zhtj_mqASATcNBDff_VEac8Bf5EdFbqG43azKY6lZIVMe6xWHqZOKV6NrDyCGwEwPPG74EsibeTN6bQa5YdvJmZaVwDzgTmzYE-DXR0EuZYk0ya6JT9tZX28q5.png) 
-  _**1.3. Lógica de predicados**_  
    - Sintaxis:
        - Extiende la lógica de proposiciones y permite hablar de objetos y relaciones entre ellos.
        - Las letras mayúsculas P, Q, R designan predicados, las minúsculas a, b,...,x,... designan variables.
        - ![](https://remnote-user-data.s3.amazonaws.com/u6gBBYNWBN-EWmmzrFo-UvLRtMpAUMD56alVwGixMUgSlUCCiCL--4_jRr0oMdCVwvc8fQ0mCTGWuaDCH-gJjUU5sT8Dpx5yrNkRNnU9L6wX7oolfGkybf7RFbBBOkVE.png) 
        - Variables libres: corresponden a variables del programa
        - Variables mudas o ligadas: Van asociadas a un tipo de cuantificador, ayudan a describir aspectos sobre el dominio.
        - ![](https://remnote-user-data.s3.amazonaws.com/ok6Vf4PRmi_4dbm2EDku47fsDMUoQlEJyvXKYSz3Rgo4ngCFvb6hVSJdoN07KI_7obnNEIjHGygCqGmOXzEgNppEZtq-w1jwIKvR3CmllMbrSMaBSc9P1LSMPTEiYOcK.png) 
        - ![](https://remnote-user-data.s3.amazonaws.com/_Grouk5-GqDFB4Lg0ujatITKTCgBPhsgq3kAinbAM9MW8GZ_7HDtJopfaMrlZdcFurrrQlQaI7uk3IDC-xZ1EGSQt-c8KtJz62JlDRBufVtCF5f6t7clBNqRBF5bBWKf.png) 
        - Las variables ligadas las nombraremos con letras griegas: ![](https://remnote-user-data.s3.amazonaws.com/qQSX4mhrvbl8LQyIJriD1A9cm8Y0RpIrUcDSi-jYXke_xnZ6-ipInW4g8KlxiyLiCKbq30j53pQOgdkZEUCtE0V7LCgslciRmZJu5C_DkQeyzyjST2ZrPyyfpAmdOBPP.png) 
        - ![](https://remnote-user-data.s3.amazonaws.com/aDQ6S9gl6Qdwd4BgQy7iL5ENvNXwdDk7e6uGcIoy-mvmjRiZTt2lGgStl7QCXbljwaSlQ8G2EvXtSLgbOEG_uF73owAOsUS7MUkcSmWteNfNHfIZClCPlRZD1iJ0aH8L.png) 
    - Semántica:
        - El valor de verdad de un predicado depende de los valores de las variables libres
        - ![](https://remnote-user-data.s3.amazonaws.com/ljkOdLBciGdgyR9nJZgz_2ztFwtqJA7Ap9mpm3U1W9zwtD8qW1zCOvQu03XLx68Ib3TUEWxb4rZnXU0kyaxd7i7DQ98dExKBHrteQvdgx4UDLyKNLRCw0GVMEZjey9-X.png) 
        - ![](https://remnote-user-data.s3.amazonaws.com/WdwLriJlg-_O8afJMw_fCqgJFxmZO4-errcy8PUPfDAC7gRNDofVj3SqWyjx3IGraT9AJTh-8SKlpTvmDuEGYxgcrN0GvkEfjmkcC_y47enL9SiABqmuovzAWMWetR_g.png) 
        - ![](https://remnote-user-data.s3.amazonaws.com/2JuUeVv_YZ_DOlEy_BgYqjWMKD2MKGrx9t0tpJOrD0pSPiznnbvQ1k0ps9nObcAXgRFrl-zAoVb4MRmdKauiOyOW8TPOQSbcjK1kWfcfB5Sa0rBXEDCxfWEYxsKdFoD1.png) 
        - Repasar las leyes de equivalencia en el aula virtual.
-  _**1.4. Especificación con predicados**_  
    - Un predicado P puede definirse a partir del conjunto de estados que lo satisfacen
    - **No te has enterado de nada** 
-  _**1.5. Especificación pre/post**_  




