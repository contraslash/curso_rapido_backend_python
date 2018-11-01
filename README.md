# Curso de backend con Python

Curso rápido de aplicaciones web con [Python](https://python.org) para [Devhack](https://www.devhack.co/).

En este repositorio encontrará:

- [content](content): Todo el contenido del curso: presentaciones y artículos
- [ejercicios](ejercicios): Código en Python correspondiente a cada clase
- [output](output): Una versión compilada de la página del curso
- [project](project): Referencias a repositorios con código de los proyectos realizados en este curso
- [themes](themes): Tema de Pelican para construir el sitio estático

Este sitio fue construido usando [Pelican](https://blog.getpelican.com/)

Para configurar el ambiente de desarrollo

```bash
# Create an environment
conda create --name curso_rapido_python
# Activate the environment
source activate curso_rapido_python
# Install pelican dependencies
conda install -c conda-forge pelican
conda install -c conda-forge markdown

# And for live reload
conda install -c conda-forge livereload
```

Alternativa con virtualenv
```bash
mkvirtualenv  -p python3 curso_rapido_python

pip install pelican
pip install markdown
pip install livereload
```

Para ejecutar local

```bash
pelican --autoreload
```


Para crear un nuevo tema

```bash
mkdir -p themes/<your_theme_name>/{static/{css,js},templates}
touch themes/<your_theme_name>/templates/{archives.html,period_archives.html,author.html,authors.html,categories.html,category.html,index.html,page.html,tag.html,tags.html}
```
