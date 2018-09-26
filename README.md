# Curso Rápido de Python

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

Para ejecutar local

```bash
pelican --autoreload
```


Para crear un nuevo tema

```bash
mkdir -p themes/<your_theme_name>/{static/{css,js},templates}
touch themes/<your_theme_name>/templates/{archives.html,period_archives.html,author.html,authors.html,categories.html,category.html,index.html,page.html,tag.html,tags.html}
```
