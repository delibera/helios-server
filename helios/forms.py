"""
Forms for Helios
"""

from django import forms
from django.conf import settings

from .fields import SplitDateTimeField
from .models import Election
from .widgets import SplitSelectDateTimeWidget


class ElectionForm(forms.Form):
  short_name = forms.SlugField(max_length=40, label="Nombre Corto", help_text='sin espacios, formará parte de la URL para tus elecciones, ej. mi-club-2010')
  name = forms.CharField(max_length=100, label="Nombre", widget=forms.TextInput(attrs={'size':60}), help_text='el nombre para tus elecciones, ej. Elecciones Mi Club 2010')
  description = forms.CharField(max_length=4000, label="Descripción", widget=forms.Textarea(attrs={'cols': 70, 'wrap': 'soft'}), required=False)
  election_type = forms.ChoiceField(label="tipo", choices = Election.ELECTION_TYPES)
  use_voter_aliases = forms.BooleanField(required=False, initial=False, label="Usar alias de votantes", help_text='Si se selecciona, las identidades de los votantes serán reemplazadas por un alias, ej. "V12", en el centro de seguimiento de papeletas.')
  #use_advanced_audit_features = forms.BooleanField(required=False, initial=True, help_text='disable this only if you want a simple election with reduced security but a simpler user interface')
  randomize_answer_order = forms.BooleanField(required=False, initial=False, label="Orden de respuestas aleatorias", help_text='activa esto si quieres que las respuestas a las preguntas aparezcan en un orden aleatorio para cada votante.')
  private_p = forms.BooleanField(required=False, initial=False, label="¿Privado?", help_text='Unas elecciones privadas son solo visibles para los votantes registrados.')
  help_email = forms.CharField(required=False, initial="", label="Dirección de Correo de Ayuda", help_text='Una dirección de correo que los votantes deberían contactar si necesitan ayuda.')
  
  if settings.ALLOW_ELECTION_INFO_URL:
    election_info_url = forms.CharField(required=False, initial="", label="la URL a un documento PDF que contiene información extra de las elecciones, ej. biografías del candidato y declaraciones.")
  
  # times
  voting_starts_at = SplitDateTimeField(label="La votación comienza el", help_text = 'fecha y hora UTC del comienzo de la votación.',
                                   widget=SplitSelectDateTimeWidget, required=False)
  voting_ends_at = SplitDateTimeField(label="La votación acaba el", help_text = 'fecha y hora UTC de la finalización de la votación.',
                                   widget=SplitSelectDateTimeWidget, required=False)

class ElectionTimeExtensionForm(forms.Form):
  voting_extended_until = SplitDateTimeField(help_text = 'UTC date and time voting extended to',
                                   widget=SplitSelectDateTimeWidget, required=False)
  
class EmailVotersForm(forms.Form):
  subject = forms.CharField(max_length=80)
  body = forms.CharField(max_length=4000, widget=forms.Textarea)
  send_to = forms.ChoiceField(label="Send To", initial="all", choices= [('all', 'all voters'), ('voted', 'voters who have cast a ballot'), ('not-voted', 'voters who have not yet cast a ballot')])

class TallyNotificationEmailForm(forms.Form):
  subject = forms.CharField(max_length=80)
  body = forms.CharField(max_length=2000, widget=forms.Textarea, required=False)
  send_to = forms.ChoiceField(label="Send To", choices= [('all', 'all voters'), ('voted', 'only voters who cast a ballot'), ('none', 'no one -- are you sure about this?')])

class VoterPasswordForm(forms.Form):
  voter_id = forms.CharField(max_length=50, label="Voter ID")
  password = forms.CharField(widget=forms.PasswordInput(), max_length=100)

