# Generated by Django 2.0.1 on 2018-05-01 13:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sessao',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.Usuario')),
            ],
        ),
    ]
