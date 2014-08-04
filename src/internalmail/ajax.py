from django.utils import simplejson
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.template.loader import render_to_string
from .models import InternalMail

@dajaxice_register
def email_get(request,iid):

	emailget = InternalMail.objects.get(Ticketid=iid)
	emailget.is_read = True
	emailget.save()
	render = render_to_string('internalmails/getmail.html',{'emailget': emailget})
	dajax = Dajax()
	dajax.assign('#mailbox','innerHTML',render)

	return dajax.json()