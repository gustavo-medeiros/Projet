# Generated by Django 2.1.15 on 2020-04-30 07:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Members', models.ManyToManyField(related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'projet',
            },
        ),
    ]
