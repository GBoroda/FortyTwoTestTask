# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Contact


class ContactTest(TestCase):
    fixtures = ['initial_data.json']

    def test_contact_exist(self):
        """  contact on page  """
        contact = Contact.objects.first()
        response = self.client.get(reverse('index.html'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, contact.name)

    def test_contacts_in_db(self):
        """ contact in db """
        contact = Contact.objects.first()
        self.assertIsNotNone(contact)

    def test_few_contacts_in_db(self):
        """ 2 or more contacts in db """
        self.assertEqual(Contact.objects.all().count(), 1)
        Contact.objects.create(name='Some',
                               surname='Some',
                               date_of_birth='1990-06-06',
                               bio='some text',
                               skype='skypeID',
                               email='some@gmail.com',
                               jabber='some@jabber.cc',
                               other='some other txt')
        self.assertEqual(Contact.objects.all().count(), 2)
        page = self.client.get(reverse('index.html'))
        self.assertContains(page, Contact.objects.get(pk=1).name)
        self.assertNotContains(page, Contact.objects.get(pk=2).name)

    def test_none_contacts_in_db(self):
        """ 0 contact in db """
        Contact.objects.all().delete()
        self.assertEqual(Contact.objects.all().count(), 0)
        response = self.client.get(reverse('index.html'))
        self.assertEqual(response.status_code, 404)

    def test_utf8_on_page(self):
        """ testing utf8 data on the page """
        page = self.client.get(reverse('index.html'))
        contact = Contact.objects.first()
        contact.name = u'Михаил'
        self.assertContains(page, contact.name)
