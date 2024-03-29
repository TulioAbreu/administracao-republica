# Generated by Django 2.2.1 on 2019-07-01 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caixa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.FloatField(default=0.0)),
                ('setPaid', models.BooleanField(default=False)),
                ('mes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Caixa')),
            ],
        ),
    ]
