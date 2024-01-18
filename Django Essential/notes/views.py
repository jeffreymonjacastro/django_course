from django.shortcuts import render
# from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from .forms import NotesForm
from .models import Notes

## view that lists all notes
# def list(request):
#   all_notes = Notes.objects.all()
#   return render(request, 'notes/notes_list.html', {
#     'notes': all_notes
#   })

class NotesListView(LoginRequiredMixin, ListView):
  model = Notes
  context_object_name = 'notes'
  template_name = 'notes/notes_list.html'
  login_url = '/admin'

  def get_queryset(self):
    return self.request.user.notes.all()


## View that shows a single note
# def detail(request, pk):
#   try:
#     note = Notes.objects.get(pk=pk)
#   except Notes.DoesNotExist:
#     raise Http404("Note doesn't not exist")
  
#   return render(request, 'notes/notes_detail.html', {
#     'note': note
#   })


class NotesDetailView(DetailView):
  model = Notes
  context_object_name = 'note'
  template_name = 'notes/notes_detail.html'


## View that creates a new note
class NotesCreateView(CreateView):
  model = Notes
  form_class = NotesForm
  success_url = '/smart/notes'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user = self.request.user
    self.object.save()
    return HttpResponseRedirect(self.get_success_url())

## View that updates a note
class NotesUpdateView(UpdateView):
  model = Notes
  form_class = NotesForm
  success_url = '/smart/notes'


class NotesDeleteView(DeleteView):
  model = Notes
  success_url = '/smart/notes'
  template_name = 'notes/notes_delete.html'