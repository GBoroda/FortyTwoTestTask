from django.shortcuts import render
from django.http import Http404
from .models import Contact
import logging


logger = logging.getLogger(__name__)


def index(request):
    logger.info(request)
    if len(Contact.objects.all()) == 0:
        raise Http404("Contacts not found")
    else:
        contact = Contact.objects.first()
        logger.debug(contact)
        return render(request, 'index.html', {'contact': contact})
