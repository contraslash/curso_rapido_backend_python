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

        return super(SimpleUpload, self).form_valid(form=form)