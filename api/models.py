from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    OPTIONS = (
        ("security", "Security"),
        ("problem", "Problem"),
        ("questions", "Questions"),
        ("praise/criticism", "Praise/Criticism"),
        ("other", "Other")
    )

    first_name = models.CharField(
        max_length=100,
        help_text="First Name"
    )
    last_name = models.CharField(
        max_length=100,
        help_text="Last Name"
    )
    email = models.EmailField(_("Your E-Mail Address"),
                              max_length=100,
                              blank=True,
                              help_text="(not required but needed if you expect a answer)"
                              )
    options = models.CharField(
        choices=OPTIONS,
        max_length=100,
        default="questions"
    )
    message = models.TextField(
        max_length=1400,
        help_text="Please describe your matter."
    )
    date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f' {self.first_name}' \
               f' {self.last_name}' \
               f' {self.email}' \
               f' {self.options}' \
               f' {self.message} ' \
               f' {self.date}'


class PrivacaPolicy(models.Model):
    privacy_policy = models.FileField(upload_to="media")
