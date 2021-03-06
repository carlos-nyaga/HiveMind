# Generated by Django 2.1.1 on 2018-09-30 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='This Represents the Users First Name.', max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(help_text='This Represents the Users Last Name.', max_length=255, verbose_name='Last Name')),
                ('school_id', models.CharField(help_text='This Represents the Users School ID.', max_length=20, unique=True, verbose_name='School ID')),
                ('email', models.EmailField(help_text='This Represents the Users Email.', max_length=254, unique=True, verbose_name='Email')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='This Represents the Users Phone Number.', max_length=128, verbose_name='Phone Number')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id', 'school_id', 'last_name'],
            },
        ),
    ]
