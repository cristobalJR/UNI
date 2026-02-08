#git
# Git
Es una herramienta de *control de versiones* local. 
GitBash, es la consola que te permite ejecutar comandos de git.
- Un **repositorio** es una colección de archivos de distintas versiones de un proyecto, pueden ser locales o remotos.
- **commit**: registros de los distintos cambios a lo largo de un proyecto, son el componente básico de la línea del tiempo de las versiones del software

Tres áreas o estados en GIT:
- **Directorio de trabajo**: Contiene los archivos y el directorio .git del repositorio. (working repository) *modificada* (modified) -> Donde estás o has modificado los datos
- **Área de preparación**: Conjunto de archivos y cambios que serán incluidos en el próximo commit. (staging area) *preparada* (staged) -> Contiene cambios que no son parte del repositorio pero se está preparando el commit
*aquí se hace el commit*
- **Repositorio (directorio .git)**: Contiene metadatos y las versiones de tu proyecto, es la parte que se copia cuando clonas un repositorio al PC. *confirmada* (committed) -> Ya se hizo el commit
# GitHub
Es un espacio de repositorios en la nube que permite enlazarse y utilizar las funciones de Git, para llevar un registro y control de versiones en la web.

# GitBash
## Comandos:
- cd Documents (Va a documents si existe dentro de este directorio)
- cd .. (va un nivel mas arriba(para atrás))
- cd  (vuelve al directorio raiz)
- mkdir prueba (Crea una carpeta llamada prueba en ese directorio)
- ls (nos permite ver el contenido de ese directorio)
- rmdir prueba (elimina la carpeta prueba si está en ese directorio)
- clear borra los comandos anteriores de la pantalla

- git init (Crear un repositorio)
- git status (te enseña el estado de el directorio de trabajo y del area de preparación)
- git add NombreArchivo, traquea los cambios sobre ese archivo para poder hacer commit)
- git rm  NombreArchivo (elimina del commit el archivo)
- git commit (abre el editor de texto default (vsCode) y te permite escribir ahí el mensaje del commit)
- git log (te enseña los commits anteriores)
- git log --oneline (te muestra commits, una sola línea por commit)
- git branch nombre-de-la-rama (crea una rama con ese nombre)
- git branch (enseña las ramas)
- git checkout nombre-de-la-rama (nos mueve a la rama de ese nombre)
- git checkout -b nombre-de-la-rama (crea desde la rama en la que estamos una rama con ese nombre y nos lleva hacia ella)
- git branch -m nombre-nuevo (cambia el nombre de la rama actual a nombre-nuevo)
- git branch -m nombre-actual nombre-nuevo (cambia la rama nombre-actual, de nombre a nombre-nuevo)
- git branch -d nombre-rama (elimina la rama del repositorio local nombre-rama, no debes de estar en la rama que estás eliminando)
- git merge rama-que-vamos-a-fusionar (debemos de estar en la rama que queremos cambiar y que prevalezca,  la rama-que-vamos-a-fusionar la podemos borrar después)
- una vez has solucionado los posibles conflictos de un merge:
	- git merge --continue (prepara el editor de texto para realizar el commit del merge), esto mismo puede no hacerse, ya que VSCode te abre un formulario en el explorador de archivos sin necesidad de este comando 
- git push origin main (intenta push a la rama origin, que es la remona, de la rama main)
- git pull origin main(actualiza el repositorio local con el repositorio remoto de la rama main remota=origin a la rama main local = main)
- git fetch origin (comprueba si el repositorio local está desactualizado con respecto al repositorio remoto origin = nombre en el repositorio local de la rama main del remoto)
## Commit:
Registran los cambios de los archivos en comparación a la versión anterior.
- git commit -m "Agregar archivo de texto" -> Si el commit es muy pequeño hacerlo así
- git commit (abre el editor de texto default (vsCode) y te permite escribir ahí el mensaje 
- git commit --amend (modifica un commit, mejor solo hacerlo en local para no modificar el historial de algo que otros pueden estar usando)

