from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def login(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.commit(request)
            return HttpResponseRedirect('/account/success')
    else:
        form = LoginForm()
    return render(request, 'login.html', { 'form': form })

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/account/login/')

def success(request):
    return HttpResponse('Success! Welcome ' + request.user.first_name + ' ' + request.user.last_name + '!')


class LoginForm(forms.Form):
    username = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={ 'placeholder': 'Username'}))
    password = forms.CharField(label="", max_length=100, widget=forms.PasswordInput(attrs={ 'placeholder': 'Password'}))

    def clean(self):
        self.user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if self.user is None:
            raise forms.ValidationError('Invalid username or password')
        return self.cleaned_data

    def commit(self, request):
        auth_login(request, self.user)
