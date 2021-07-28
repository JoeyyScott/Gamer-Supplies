# Generated by Django 3.2.5 on 2021-07-28 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplies', '0002_auto_20210726_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address_line_1', models.CharField(max_length=50)),
                ('address_line_2', models.CharField(max_length=50)),
                ('town_or_city', models.CharField(max_length=50)),
                ('county', models.CharField(blank=True, max_length=50, null=True)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(max_length=40)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='CrateItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('crateitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crateitems', to='checkout.order')),
                ('supply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplies.supply')),
            ],
            options={
                'verbose_name_plural': 'Crate Items',
            },
        ),
    ]
