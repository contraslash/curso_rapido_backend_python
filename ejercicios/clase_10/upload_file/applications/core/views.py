import csv
from django.shortcuts import render
from  django.views.generic import FormView


from . import (
    forms
)


class SimpleUpload(FormView):
    form_class = forms.FileForm
    template_name = "upload_file.html"
    success_url = "/"

    def form_valid(self, form):
        print(form.cleaned_data)
        archivo = form.cleaned_data.get("file")
        # readed_file = archivo.read().decode()
        # print(archivo.readlines())
        binary_lines = archivo.readlines()
        decoded_lines = [line.decode() for line in binary_lines]
        posts = list()
        reader = csv.reader(decoded_lines)
        # Skip first line
        next(reader)
        for r in reader:
            print(r)

        return super(SimpleUpload, self).form_valid(form=form)