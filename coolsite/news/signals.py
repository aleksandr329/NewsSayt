from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import News


# @receiver(post_save, sender=News)
# def product_created(instance, created, **kwargs):
#     if not created:
#         return
#
#     emails = User.objects.filter(
#         subscriptions__category=instance.category
#     ).values_list('email', flat=True)
#
#     subject = f'Новый товар в категории {instance.category}'
#
#     text_content = (
#         f'Новость: {instance.title}\n'
#         f'Текст: {instance.text}\n\n'
#         f'Ссылка на товар: http://127.0.0.1:8000{instance.get_absolute_url()}'
#     )
#     html_content = (
#         f'Новость: {instance.title}<br>'
#         f'Текст: {instance.text}<br><br>'
#         f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
#         f'Ссылка на товар</a>'
#     )
#     for email in emails:
#         msg = EmailMultiAlternatives(subject, text_content, None, [email])
#         msg.attach_alternative(html_content, "text/html")
#         msg.send()

#I checked this signal, it is fully working, a message has come to the indicated mail,
# about new news! But I decided to comment it out so that it would not accidentally send
# more messages and I would not be thrown into the BAN!