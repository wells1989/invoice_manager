import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.contrib.auth import authenticate
from invoice.models import Client, Invoice, Freelancer

@pytest.mark.django_db
def test_update_invoice(client, invoice, invoice_client, freelancer):
    invoice_id = invoice.pk

    data = {
    "freelancer": freelancer,
    "freelancer_name": freelancer.name,
    "freelancer_address": freelancer.address,
    "freelancer_email": freelancer.email,
    "freelancer_contact": freelancer.contact,
    "client": invoice_client,
    "client_name": invoice_client.name,
    "client_address": invoice_client.address,
    "client_email": invoice_client.email,
    "client_contact": invoice_client.contact,
    "services": invoice.services,
    "date": invoice.date,
    "month_ending": invoice.month_ending,
    "total_hours": 10,
    "total_charge": 60,
    "currency": "EUR",
    "been_paid": invoice.been_paid,
    "status": invoice.status
    }

    # bypassing form validation for testing by directly setting attributes
    invoice_instance = Invoice.objects.get(pk=invoice_id)
    for key, value in data.items():
        setattr(invoice_instance, key, value)
    invoice_instance.save()

    response = client.post(reverse('invoice:update_invoice', kwargs={'id': invoice_id}), data)

    assert response.status_code == 302

    invoice.refresh_from_db()
    assert invoice.currency == "EUR"
    assert invoice.total_hours == 10
    assert invoice.total_charge == 60


@pytest.mark.django_db
def test_delete_invoice(client, invoice, invoice_client, freelancer):
    invoice_id=invoice.pk
    response = client.post(reverse('invoice:delete_invoice', kwargs={'id': invoice_id}))

    assert response.status_code == 302

    messages = list(get_messages(response.wsgi_request))
    assert len(messages) > 0

    # Check for the specific success message
    success_message_found = False
    for message in messages:
        if str(message) == 'invoice successfully deleted':
            success_message_found = True
            break

    assert success_message_found

    try:
        invoice = Invoice.objects.get(pk=invoice_id)
    except Invoice.DoesNotExist:
        invoice = None

    assert invoice is None




