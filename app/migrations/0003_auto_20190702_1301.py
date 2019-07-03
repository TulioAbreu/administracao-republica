# Generated by Django 2.2.1 on 2019-07-02 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_caixa_conta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta',
            name='setPaid',
            field=models.BooleanField(default=False, verbose_name='Paga'),
        ),
        migrations.CreateModel(
            name='MoradorPagouCaixa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pago', models.BooleanField(default=False)),
                ('caixa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Caixa')),
                ('morador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]