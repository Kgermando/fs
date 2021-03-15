# Generated by Django 3.1.7 on 2021-03-15 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('WEBSITE', 'WEBSITE'), ('SOFTWARE', 'SOFTWARE'), ('MOBILE', 'MOBILE'), ('WEBAPP', 'WEBAPP')], max_length=8)),
                ('slug', models.SlugField(blank=True, help_text='Laissez ce champ vide', unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='MotCles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('SANTE', 'SANTE'), ('EDUCATION', 'EDUCATION'), ('BUSINESS', 'BUSINESS'), ('AGRICULTURE', 'AGRICULTURE'), ('iNDUSTRIE', 'iNDUSTRIE'), ('TELECOMMUNICATION', 'TELECOMMUNICATION'), ('MEDIA', 'MEDIA'), ('E-COMMERCE', 'E-COMMERCE'), ('EVENEMENT', 'EVENEMENT'), ('TRANSPORT', 'TRANSPORT'), ('RESSOURCE HUMAINES', 'RESSOURCE HUMAINES'), ('BANK', 'BANK'), ('ONG', 'ONG'), ('ENTREPRISE', 'ENTREPRISE'), ('MINE', 'MINE'), ('HABILLEMENT', 'HABILLEMENT'), ('SALON', 'SALON'), ('SERVICE', 'SERVICE')], max_length=18)),
                ('slug', models.SlugField(blank=True, help_text='Laissez ce champ vide', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('CLAIRE', 'CLAIRE'), ('CLASSIC', 'CLASSIC'), ('SOMBRE', 'SOMBRE')], max_length=8)),
                ('slug', models.SlugField(blank=True, help_text='Laissez ce champ vide', unique=True)),
            ],
        ),
    ]