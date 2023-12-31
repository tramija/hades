# Generated by Django 4.2.4 on 2023-08-31 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'ordering': ['id'], 'verbose_name': 'Tipo', 'verbose_name_plural': 'Tipos'},
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Types',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=9),
        ),
    ]
