from django.shortcuts import render
from django.contrib.auth.views import LoginView, auth_login
from django.contrib import messages
from django import http
# Create your views here.


class Login(LoginView):

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        messages.add_message(
            self.request,
            messages.ERROR,
            "Logged in successfully"
        )
        return http.HttpResponseRedirect("/")

    def form_invalid(self, form):
        print("FORM INVALID")
        messages.add_message(
            self.request,
            messages.ERROR,
            "Username or Password is invalid"
        )
        return self.render_to_response({"form": form})