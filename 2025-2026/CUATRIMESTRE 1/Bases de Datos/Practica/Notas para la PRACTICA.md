## 1.-

. ¿Tienes que entender esto para el examen?

Sí, pero con un matiz.

No creo que tengas que memorizar de memoria cada línea exacta del script completo. Pero sí deberías entender y saber usar:

```
PRIMARY KEYFOREIGN KEYREFERENCESNOT NULLUNIQUECHECKON DELETE CASCADEON DELETE SET NULLALTER TABLEDROP TABLECREATE TABLE
```

El enunciado dice que la práctica no se entrega, pero que se evalúa en el examen y supone el 30% de la nota final; además, se evaluarán los conocimientos necesarios para realizarla y resolverla. Por tanto, la práctica funciona como **guía de estudio aplicada**: no entregas el script, pero el examen puede preguntarte cosas que requieren haber entendido este esquema.
Lo que más probablemente te interesa dominar es:

```
1. Por qué unas columnas son NOT NULL y otras admiten NULL.
2. Qué columnas son claves primarias.
3. Qué claves ajenas conectan cada tabla.
4. Qué ocurre al borrar filas según ON DELETE CASCADE / SET NULL / restringido.
5. Qué restricciones CHECK simulan reglas del enunciado.
6. Qué errores puede devolver Oracle si violas una restricción.
7. Cómo modificar restricciones con ALTER TABLE.
```