# Generated by Django 3.2.2 on 2021-05-11 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compiler', '0005_auto_20210512_0307'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_pratice_solution',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
