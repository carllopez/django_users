import csv

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView


from users.models import User
from users.templatetags.users_tags import eligible, bizzfuzz

class UserListView(ListView):

    model = User


class UserCreateView(CreateView):
    model = User
    fields = ['email', 'birthday', 'first_name', 'last_name']
    success_url = reverse_lazy('user-list')


class UserDetailView(DetailView):
    model = User


class UserUpdateView(UpdateView):
    model = User
    fields = ['email', 'birthday', 'first_name', 'last_name']
    success_url = reverse_lazy('user-list')


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('user-list')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class CsvView(View):

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="users.csv"'

        writer = csv.writer(response)
        writer.writerow(['Username', 'Birthday', 'Eligible', 'Random Number', 'BizzFuzz'])
        users = User.objects.all()
        for user in users:
            writer.writerow([user.email, user.birthday.strftime('%b. %d, %Y').replace(' 0', ' '), eligible(user.birthday), user.rnd_number, bizzfuzz(user.rnd_number)])
        return response





