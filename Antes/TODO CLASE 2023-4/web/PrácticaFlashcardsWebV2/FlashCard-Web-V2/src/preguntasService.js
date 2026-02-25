// preguntasService.js
const preguntas = new Map();
let nextId = 0

const preguntasService = {
  getPreguntas: () => {
    return[...preguntas.values()]
  },


  getPreguntaById: (id) => {
    return preguntas.get(id)
  },

  addPregunta: (newPregunta) => {
    let id = nextId++;
    preguntas.id = id;
    newPregunta.id = id
    preguntas.set(preguntas.id, newPregunta);
    return preguntas;
  },

  updatePregunta: (id, pregunta, respuesta) => {
    const preguntaToUpdate = preguntas.get(id);
    if (preguntaToUpdate) {
        preguntaToUpdate.pregunta = pregunta;
        preguntaToUpdate.respuesta = respuesta;
        return preguntaToUpdate;
    }
    return null;
  },

  deletePregunta: (id) => {
    return preguntas.delete(id);
  },

  agregarComentario: (id, nuevoComentario, ComentarioNuevoRelevancia, ComentarioNuevoUsuario) => {
    const pregunta = preguntas.get(id);

    // Verifica si la pregunta existe
    if (pregunta) {
        // Agrega el nuevo comentario a la lista de comentarios de la pregunta
        const comentario_crear = []
        comentario_crear.push(nuevoComentario)
        comentario_crear.push(ComentarioNuevoRelevancia)
        comentario_crear.push(ComentarioNuevoUsuario)
        pregunta.comentarios.push(comentario_crear);
    } else {
        res.status(404).redirect(`/error/AgregarComentario/No se pudo agregar el comentario`)
    }
  },

  borrarComentario: (id, comentario_a_eliminar) => {
    let id_comentario = parseInt(id);
    const pregunta = preguntas.get(id_comentario);
    if (pregunta) {
      // Agrega el nuevo comentario a la lista de comentarios de la pregunta
      pregunta.comentarios.pop(comentario_a_eliminar);
    } else {
        res.status(404).redirect(`/error/EliminarComentario/No se pudo eliminar el comentario`)
    }
  },

  actualizarPregunta: (old_pregunta, id, imagen_pregunta_url, imagen_respuesta_url, pregunta, respuesta, dificultad, tema, nuevoComentario) => {
    const preguntaToUpdate = preguntas.get(id);
    // Verifica si la pregunta existe
    if (preguntaToUpdate) {
        // Actualiza los datos de la pregunta
        if (old_pregunta != pregunta) {
          preguntaToUpdate.imagen_pregunta_url = imagen_pregunta_url;
        }
        preguntaToUpdate.imagen_respuesta_url = imagen_respuesta_url;
        preguntaToUpdate.pregunta = pregunta;
        preguntaToUpdate.respuesta = respuesta;
        preguntaToUpdate.dificultad = dificultad;
        preguntaToUpdate.tema = tema;
        
        // Agrega el nuevo comentario a la lista de comentarios de la pregunta
        return preguntaToUpdate.comentarios.push(nuevoComentario);
    } else {
      res.status(404).redirect(`/error/AgregarComentario/No se pudo actualizar la pregunta`)
    }
  },

};

export default preguntasService;

preguntasService.addPregunta({imagen_pregunta_url: "https://previews.123rf.com/images/aprillrain/aprillrain2212/aprillrain221200638/196354278-달에-앉아-우주-비행사의-만화-이미지-고품질-일러스트레이션.jpg", imagen_respuesta_url: "https://formacionparaformadores.com/wp-content/uploads/2015/01/Ser-Formador-preguntas-y-re-630x315.jpg", pregunta: "¿Cuanto es 2+2?", respuesta: "Es un hecho establecido hace demasiado tiempo que un lector se distraerá con el contenido del texto de un sitio mientras que mira su diseño. El punto de usar Lorem Ipsum es que tiene una distribución más o menos normal de las letras, al contrario de usar textos como por ejemploaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", tema: "3", dificultad: "baja", comentarios: [["Prueba1", "1", "admin"], ["Prueba2", "1", "admin"]] })
preguntasService.addPregunta({imagen_pregunta_url: "https://previews.123rf.com/images/aprillrain/aprillrain2212/aprillrain221200638/196354278-달에-앉아-우주-비행사의-만화-이미지-고품질-일러스트레이션.jpg", imagen_respuesta_url: "https://formacionparaformadores.com/wp-content/uploads/2015/01/Ser-Formador-preguntas-y-re-630x315.jpg", pregunta: "¿Quien es el CEO de SpaceX?", respuesta: "Es un hecho establecido hace demasiado tiempo que un lector se distraerá con el contenido del texto de un sitio mientras que mira su diseño. El punto de usar Lorem Ipsum es que tiene una distribución más o menos normal de las letras, al contrario de usar textos como por ejemploaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", tema: "6", dificultad: "alta", comentarios: [] })
preguntasService.addPregunta({imagen_pregunta_url: "https://previews.123rf.com/images/aprillrain/aprillrain2212/aprillrain221200638/196354278-달에-앉아-우주-비행사의-만화-이미지-고품질-일러스트레이션.jpg", imagen_respuesta_url: "https://formacionparaformadores.com/wp-content/uploads/2015/01/Ser-Formador-preguntas-y-re-630x315.jpg", pregunta: "¿Cuanto es 2*2?", respuesta: "Es un hecho establecido hace demasiado tiempo que un lector se distraerá con el contenido del texto de un sitio mientras que mira su diseño. El punto de usar Lorem Ipsum es que tiene una distribución más o menos normal de las letras, al contrario de usar textos como por ejemploaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", tema: "9", dificultad: "media", comentarios: [] })
preguntasService.addPregunta({imagen_pregunta_url: "https://previews.123rf.com/images/aprillrain/aprillrain2212/aprillrain221200638/196354278-달에-앉아-우주-비행사의-만화-이미지-고품질-일러스트레이션.jpg", imagen_respuesta_url: "https://formacionparaformadores.com/wp-content/uploads/2015/01/Ser-Formador-preguntas-y-re-630x315.jpg", pregunta: "¿Cuál es la capital de Francia?", respuesta: "Es un hecho establecido hace demasiado tiempo que un lector se distraerá con el contenido del texto de un sitio mientras que mira su diseño. El punto de usar Lorem Ipsum es que tiene una distribución más o menos normal de las letras, al contrario de usar textos como por ejemploaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", tema: "7", dificultad: "media", comentarios: [] })
preguntasService.addPregunta({imagen_pregunta_url: "https://previews.123rf.com/images/aprillrain/aprillrain2212/aprillrain221200638/196354278-달에-앉아-우주-비행사의-만화-이미지-고품질-일러스트레이션.jpg", imagen_respuesta_url: "https://formacionparaformadores.com/wp-content/uploads/2015/01/Ser-Formador-preguntas-y-re-630x315.jpg", pregunta: "¿En qué año se fundó la ONU?", respuesta: "Es un hecho establecido hace demasiado tiempo que un lector se distraerá con el contenido del texto de un sitio mientras que mira su diseño. El punto de usar Lorem Ipsum es que tiene una distribución más o menos normal de las letras, al contrario de usar textos como por ejemploaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", tema: "8", dificultad: "alta", comentarios: [] })
preguntasService.addPregunta({imagen_pregunta_url: "https://previews.123rf.com/images/aprillrain/aprillrain2212/aprillrain221200638/196354278-달에-앉아-우주-비행사의-만화-이미지-고품질-일러스트레이션.jpg", imagen_respuesta_url: "https://formacionparaformadores.com/wp-content/uploads/2015/01/Ser-Formador-preguntas-y-re-630x315.jpg", pregunta: "¿Cuál es el símbolo químico del oro?", respuesta: "Es un hecho establecido hace demasiado tiempo que un lector se distraerá con el contenido del texto de un sitio mientras que mira su diseño. El punto de usar Lorem Ipsum es que tiene una distribución más o menos normal de las letras, al contrario de usar textos como por ejemploaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", tema: "5", dificultad: "media", comentarios: [] })
preguntasService.addPregunta({imagen_pregunta_url: "https://previews.123rf.com/images/aprillrain/aprillrain2212/aprillrain221200638/196354278-달에-앉아-우주-비행사의-만화-이미지-고품질-일러스트레이션.jpg", imagen_respuesta_url: "https://formacionparaformadores.com/wp-content/uploads/2015/01/Ser-Formador-preguntas-y-re-630x315.jpg", pregunta: "¿Quién escribió 'Cien años de soledad'?", respuesta: "Es un hecho establecido hace demasiado tiempo que un lector se distraerá con el contenido del texto de un sitio mientras que mira su diseño. El punto de usar Lorem Ipsum es que tiene una distribución más o menos normal de las letras, al contrario de usar textos como por ejemploaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", tema: "4", dificultad: "alta", comentarios: [] })
preguntasService.addPregunta({imagen_pregunta_url: "https://previews.123rf.com/images/aprillrain/aprillrain2212/aprillrain221200638/196354278-달에-앉아-우주-비행사의-만화-이미지-고품질-일러스트레이션.jpg", imagen_respuesta_url: "https://formacionparaformadores.com/wp-content/uploads/2015/01/Ser-Formador-preguntas-y-re-630x315.jpg", pregunta: "¿Cuál es el río más largo del mundo?", respuesta: "Es un hecho establecido hace demasiado tiempo que un lector se distraerá con el contenido del texto de un sitio mientras que mira su diseño. El punto de usar Lorem Ipsum es que tiene una distribución más o menos normal de las letras, al contrario de usar textos como por ejemploaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", tema: "2", dificultad: "alta", comentarios: [] })
preguntasService.addPregunta({imagen_pregunta_url: "https://previews.123rf.com/images/aprillrain/aprillrain2212/aprillrain221200638/196354278-달에-앉아-우주-비행사의-만화-이미지-고품질-일러스트레이션.jpg", imagen_respuesta_url: "https://formacionparaformadores.com/wp-content/uploads/2015/01/Ser-Formador-preguntas-y-re-630x315.jpg", pregunta: "¿En qué año llegó el hombre a la luna por primera vez?", respuesta: "Es un hecho establecido hace demasiado tiempo que un lector se distraerá con el contenido del texto de un sitio mientras que mira su diseño. El punto de usar Lorem Ipsum es que tiene una distribución más o menos normal de las letras, al contrario de usar textos como por ejemploaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", tema: "6", dificultad: "alta", comentarios: [] })
preguntasService.addPregunta({imagen_pregunta_url: "https://previews.123rf.com/images/aprillrain/aprillrain2212/aprillrain221200638/196354278-달에-앉아-우주-비행사의-만화-이미지-고품질-일러스트레이션.jpg", imagen_respuesta_url: "https://formacionparaformadores.com/wp-content/uploads/2015/01/Ser-Formador-preguntas-y-re-630x315.jpg", pregunta: "¿Cuál es la fórmula química del agua?", respuesta: "Es un hecho establecido hace demasiado tiempo que un lector se distraerá con el contenido del texto de un sitio mientras que mira su diseño. El punto de usar Lorem Ipsum es que tiene una distribución más o menos normal de las letras, al contrario de usar textos como por ejemploaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", tema: "5", dificultad: "baja", comentarios: [] })
preguntasService.addPregunta({imagen_pregunta_url: "https://previews.123rf.com/images/aprillrain/aprillrain2212/aprillrain221200638/196354278-달에-앉아-우주-비행사의-만화-이미지-고품질-일러스트레이션.jpg", imagen_respuesta_url: "https://formacionparaformadores.com/wp-content/uploads/2015/01/Ser-Formador-preguntas-y-re-630x315.jpg", pregunta: "¿Quién pintó la Mona Lisa?", respuesta: "Es un hecho establecido hace demasiado tiempo que un lector se distraerá con el contenido del texto de un sitio mientras que mira su diseño. El punto de usar Lorem Ipsum es que tiene una distribución más o menos normal de las letras, al contrario de usar textos como por ejemploaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", tema: "4", dificultad: "alta", comentarios: [] })
preguntasService.addPregunta({imagen_pregunta_url: "https://previews.123rf.com/images/aprillrain/aprillrain2212/aprillrain221200638/196354278-달에-앉아-우주-비행사의-만화-이미지-고품질-일러스트레이션.jpg", imagen_respuesta_url: "https://formacionparaformadores.com/wp-content/uploads/2015/01/Ser-Formador-preguntas-y-re-630x315.jpg", pregunta: "¿Cuál es la montaña más alta del mundo?", respuesta: "Es un hecho establecido hace demasiado tiempo que un lector se distraerá con el contenido del texto de un sitio mientras que mira su diseño. El punto de usar Lorem Ipsum es que tiene una distribución más o menos normal de las letras, al contrario de usar textos como por ejemploaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", tema: "2", dificultad: "alta", comentarios: [] })
preguntasService.addPregunta({imagen_pregunta_url: "https://previews.123rf.com/images/aprillrain/aprillrain2212/aprillrain221200638/196354278-달에-앉아-우주-비행사의-만화-이미지-고품질-일러스트레이션.jpg", imagen_respuesta_url: "https://formacionparaformadores.com/wp-content/uploads/2015/01/Ser-Formador-preguntas-y-re-630x315.jpg", pregunta: "¿Qué planeta es conocido como el planeta rojo?", respuesta: "Es un hecho establecido hace demasiado tiempo que un lector se distraerá con el contenido del texto de un sitio mientras que mira su diseño. El punto de usar Lorem Ipsum es que tiene una distribución más o menos normal de las letras, al contrario de usar textos como por ejemploaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", tema: "9", dificultad: "media", comentarios: [] })
preguntasService.addPregunta({imagen_pregunta_url: "https://previews.123rf.com/images/aprillrain/aprillrain2212/aprillrain221200638/196354278-달에-앉아-우주-비행사의-만화-이미지-고품질-일러스트레이션.jpg", imagen_respuesta_url: "https://formacionparaformadores.com/wp-content/uploads/2015/01/Ser-Formador-preguntas-y-re-630x315.jpg", pregunta: "¿En qué año comenzó la Segunda Guerra Mundial?", respuesta: "Es un hecho establecido hace demasiado tiempo que un lector se distraerá con el contenido del texto de un sitio mientras que mira su diseño. El punto de usar Lorem Ipsum es que tiene una distribución más o menos normal de las letras, al contrario de usar textos como por ejemploaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", tema: "8", dificultad: "alta", comentarios: [] })
preguntasService.addPregunta({imagen_pregunta_url: "https://previews.123rf.com/images/aprillrain/aprillrain2212/aprillrain221200638/196354278-달에-앉아-우주-비행사의-만화-이미지-고품질-일러스트레이션.jpg", imagen_respuesta_url: "https://formacionparaformadores.com/wp-content/uploads/2015/01/Ser-Formador-preguntas-y-re-630x315.jpg", pregunta: "¿Cuál es el órgano más grande del cuerpo humano?", respuesta: "Es un hecho establecido hace demasiado tiempo que un lector se distraerá con el contenido del texto de un sitio mientras que mira su diseño. El punto de usar Lorem Ipsum es que tiene una distribución más o menos normal de las letras, al contrario de usar textos como por ejemploaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", tema: "1", dificultad: "media", comentarios: [] })
