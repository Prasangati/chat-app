from django.test import TestCase
from django.core import mail
from django.urls import reverse
from django.test import TestCase
from django.contrib.messages import get_messages


class AboutEnquiryViewTests(TestCase):
    def test_about_enquiry_view_get(self):
        response = self.client.get(reverse('about_enquiry'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/about.html')
        self.assertContains(response, '<form')

    def test_about_enquiry_view_post_valid(self):
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'I am interested in learning more about your site.',
        }
        response = self.client.post(reverse('about_enquiry'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('about_enquiry'))
        self.assertEqual(len(mail.outbox), 1)  # Check if an email was sent
        self.assertIn('Email sent successfully.', [m.message for m in get_messages(response.wsgi_request)])

    def test_about_enquiry_view_post_invalid(self):
        form_data = {
            'name': '',
            'email': 'invalid-email',
            'message': '',
        }
        response = self.client.post(reverse('about_enquiry'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/about.html')
        self.assertEqual(len(mail.outbox), 0)  # No email should be sent
        self.assertIn('Form is not valid. Please correct the errors below.',
                      [m.message for m in get_messages(response.wsgi_request)])

    def test_about_enquiry_view_post_email_error(self):
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'I am interested in learning more about your site.',
        }

        # Simulate a failure in sending an email by using a bad recipient email.
        with self.settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'):
            response = self.client.post(reverse('about_enquiry'), data=form_data)
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, reverse('about_enquiry'))
            messages = [m.message for m in get_messages(response.wsgi_request)]
            self.assertIn('Email sent successfully.', messages)

# Create your tests here.
