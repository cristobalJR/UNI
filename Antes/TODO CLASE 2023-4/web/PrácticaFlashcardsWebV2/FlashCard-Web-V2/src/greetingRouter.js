// indexRouter.js
import express from 'express';
import preguntasService from './preguntasService.js';

const router = express.Router();

router.get('/', (req, res) => {
  const data = {
    preguntas: preguntasService.getPreguntas(),
  };

  res.render('index', data);
});

//AJAX
router.get('/getPreguntas', (req, res) => {
  const limit = Number(req.query.limit) || 5;
  const skip = Number(req.query.skip) || 0;

  const data = {
    preguntas: preguntasService.getPreguntas().slice(skip, skip + limit),
  };

  res.json(data);
});
//AJAX
router.get('/getFiltro', (req, res) => {
  const data = {
    preguntas: preguntasService.getPreguntas(),
  };

  res.json(data);
});

router.get('/getPreguntasPorTema', (req, res) => {
  try {
    const tema = req.query.tema;

    if(!tema){
      const data = {
        preguntas: preguntasService.getPreguntas().slice(0, 5),
      };
      res.json(data);
    } else {
      // Filtra las preguntas por el tema proporcionado
      const preguntasFiltradas = Array.from(preguntasService.getPreguntas().values())
        .filter(pregunta => pregunta.tema === tema);
      // Devuelve las preguntas filtradas como JSON
      res.json({ preguntas: preguntasFiltradas });
    }
  } catch (error) {
    res.status(404).redirect(`/error/obetenerPregunta/Error al obtener las preguntas por tema`)
  }
});

router.get('/getComentariosPorId', (req, res) => {
  try {
    const id = req.query.id;
    
    // Filtra las preguntas por el tema proporcionado
    const preguntasFiltradas = Array.from(preguntasService.getPreguntas().values())
    .filter(pregunta => pregunta.id == id);
    // Devuelve las preguntas filtradas como JSON
    res.json({ comentarios: preguntasFiltradas[0].comentarios });
  } catch (error) {
    res.status(404).redirect(`/error/obetenerPregunta/Error al obtener los comentarios`)
  }
});

router.get('/delComentariosPorId', (req, res) => {
  try {
    const id = req.query.id;
    const comentario_a_eliminar = req.query.comentario_a_eliminar;
    preguntasService.borrarComentario(id, comentario_a_eliminar);
    // Filtra las preguntas por el tema proporcionado
    const preguntasFiltradas = Array.from(preguntasService.getPreguntas().values())
    .filter(pregunta => pregunta.id == id);
    // Devuelve las preguntas filtradas como JSON
    res.json({ comentarios: preguntasFiltradas[0].comentarios });
  } catch (error) {
    res.status(404).redirect(`/error/obetenerPregunta/Error al obtener los comentarios`)
  }
});

router.get('/detalle/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const pregunta = preguntasService.getPreguntaById(id);

  const data = {
    preguntas: pregunta,
  };
  res.render('detalle', data);
});


router.get('/respuesta/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const data = {
      preguntas: preguntasService.getPreguntaById(id),
    };
    res.render('respuesta', data);
  });

router.get('/error/:id/:eror_mes', (req, res) => {
  const id = parseInt(req.params.id);
  const data = {
    errores: {id: req.params.id,
              error_msg: req.params.eror_mes
              },
  };
  
  res.render('error404', data);
});

router.get('/verificarPregunta', (req, res) => {
  const pregunta = req.query.pregunta;

  // Verificar si la pregunta ya existe en la base de datos (simulado)
  const preguntasEnBaseDeDatos = preguntasService.getPreguntas().map(pregunta => pregunta.pregunta);
  const existe = preguntasEnBaseDeDatos.includes(pregunta);

  // Devolver el resultado como JSON
  res.json({ existe });
});

// Ruta para realizar la búsqueda de preguntas
router.get('/searchPreguntas', (req, res) => {
  try{
    const searchTerm = req.query.searchTerm;

    // Realizar la búsqueda utilizando tu servicio de preguntas
    if (!searchTerm){
        const data = {
          preguntas: preguntasService.getPreguntas().slice(0, 5),
        };
        res.json(data);
    } else {
        const preguntasEncontradas = Array.from(preguntasService.getPreguntas().values())
        .filter(pregunta => pregunta.pregunta.toLowerCase().includes(searchTerm.toLowerCase()));

        // Enviar los resultados como respuesta JSON
        res.json({ preguntas: preguntasEncontradas });
    }
  } catch (error) {
    res.status(404).redirect(`/error/searchPreguntas/Error al buscar termino`)
  }
});

router.post('/addComentario/:id', (req, res) => {
  const id = parseInt(req.params.id)
  const ComentarioNuevo = req.body.ComentarioNuevo;
  const ComentarioNuevoRelevancia = req.body.nuevoComentarioScore;
  const ComentarioNuevoUsuario = req.body.nuevoComentarioUsuario;
  if(ComentarioNuevo){
    preguntasService.agregarComentario(id, ComentarioNuevo, ComentarioNuevoRelevancia, ComentarioNuevoUsuario);
  }
  res.redirect(`/detalle/${id}`)
});

router.post('/addPregunta', (req, res) => {
  const { pregunta, respuesta, imagenPregunta, imagenRespuesta, tema, dificultad, comentario } = req.body;

  // Comprabamos las entradas
  if (![pregunta].every(texto => typeof texto === 'string')) {
    res.status(404).redirect(`/error/nuevaPregunta/La pregunta introducida no es tipo texto`)
  }
  const preguntasEnBaseDeDatos = preguntasService.getPreguntas().map(pregunta => pregunta.pregunta);
  const existe = preguntasEnBaseDeDatos.includes(pregunta);
  if (existe) {
    res.status(404).redirect(`/error/nuevaPregunta/La pregunta ya existe`);
  }
  if (![respuesta].every(texto => typeof texto === 'string')) {
    res.status(404).redirect(`/error/nuevaPregunta/La respuesta no es de tipo texto`)
  }
  if (respuesta.length<50) {
    res.status(404).redirect(`/error/nuevaPregunta/La respuesta tiene que tener longitud entre 50 y 500 carcateres`)
  }
  if (respuesta.length>450) {
    res.status(404).redirect(`/error/nuevaPregunta/La respuesta tiene que tener longitud entre 50 y 500 carcateres`)
  }
  if (![tema].every(texto => typeof texto === 'string')) {
    res.status(404).redirect(`/error/nuevaPregunta/El tema introducido no es de tipo texto`)
  }
  if (!['baja', 'media', 'alta'].includes(dificultad.toLowerCase())) {
    res.status(404).redirect(`/error/nuevaPregunta/La dificultad seleccionada no es valido`)
  }
  const patronUrl = /^(https?):\/\/[^\s/$.?#].[^\s]*$/;
  if (![imagenPregunta].every(url => patronUrl.test(url))) {
    res.status(404).redirect(`/error/nuevaPregunta/La url de la imagen de pregunta no es una url valida`)
  }
  if (![imagenRespuesta].every(url => patronUrl.test(url))) {
    res.status(404).redirect(`/error/nuevaPregunta/La url de la imagen de respuesta no es una url valida`)
  }
  
  // Llamar al servicio de preguntas para agregar la pregunta
  const nueva_pregunta = {imagen_pregunta_url: imagenPregunta, imagen_respuesta_url: imagenRespuesta, pregunta: pregunta, respuesta: respuesta, tema: tema, dificultad: dificultad, comentarios: [comentario] }
  const addPregunta = preguntasService.addPregunta(nueva_pregunta);
  if(addPregunta){
    res.redirect("/")
  } else{
    res.status(404).redirect(`/error/nuevaPregunta/No se pudo agregar la nueva pregunta`)  }
});

router.post('/actualizarPregunta/:id', (req, res) => {
  const id = parseInt(req.params.id)
  const { old_pregunta, pregunta, respuesta, imagenPregunta, imagenRespuesta, tema, dificultad, comentario } = req.body;

  // Comprabamos las entradas
  if (![pregunta].every(texto => typeof texto === 'string')) {
    res.status(404).redirect(`/error/actualizarPregunta/La pregunta introducida no es tipo texto`)
  }
  const preguntasEnBaseDeDatos = preguntasService.getPreguntas().map(pregunta => pregunta.pregunta);
  const existe = preguntasEnBaseDeDatos.includes(pregunta);
  if (existe && pregunta != old_pregunta) {
    res.status(404).redirect(`/error/nuevaPregunta/La pregunta ya existe`);
  }
  if (![respuesta].every(texto => typeof texto === 'string')) {
    res.status(404).redirect(`/error/actualizarPregunta/La respuesta no es de tipo texto`)
  }
  if (respuesta.length<50) {
    res.status(404).redirect(`/error/nuevaPregunta/La respuesta tiene que tener longitud entre 50 y 500 carcateres`)
  }
  if (respuesta.length>500) {
    res.status(404).redirect(`/error/nuevaPregunta/La respuesta tiene que tener longitud entre 50 y 500 carcateres`)
  }
  if (![tema].every(texto => typeof texto === 'string')) {
    res.status(404).redirect(`/error/actualizarPregunta/El tema introducido no es de tipo texto`)
  }
  if (!['baja', 'media', 'alta'].includes(dificultad.toLowerCase())) {
    res.status(404).redirect(`/error/actualizarPregunta/La dificultad seleccionada no es valido`)
  }
  const patronUrl = /^(https?):\/\/[^\s/$.?#].[^\s]*$/;
  if (![imagenPregunta].every(url => patronUrl.test(url))) {
    res.status(404).redirect(`/error/actualizarPregunta/La url de la imagen de pregunta no es una url valida`)
  }
  if (![imagenRespuesta].every(url => patronUrl.test(url))) {
    res.status(404).redirect(`/error/actualizarPregunta/La url de la imagen de respuesta no es una url valida`)
  }

  // Llamar al servicio de preguntas para agregar la pregunta
   const actualizarPregunta = preguntasService.actualizarPregunta(old_pregunta, id, imagenPregunta, imagenRespuesta, pregunta, respuesta, dificultad, tema, comentario);
   if(actualizarPregunta){
    res.redirect(`/detalle/${id}`)
  } else{
    res.status(404).redirect(`/error/actualizarPregunta/No se pudo agregar la nueva pregunta`)  }
});

router.post('/delete/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const deletedPregunta = preguntasService.deletePregunta(id);

  if (deletedPregunta) {
    // Puedes redirigir a la página principal o hacer algo más aquí
    res.redirect('/');
  } else {
    res.status(404).redirect(`/error/${id}/Elemento no encontrado`);
  }
});

router.get('/crearFlashcard', (req, res) => {
  res.render('crearFlashcard');
});

router.get('/edit/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const pregunta = preguntasService.getPreguntaById(id);
  res.status(302).render('editarFlashcard', pregunta);
});

export default router;
