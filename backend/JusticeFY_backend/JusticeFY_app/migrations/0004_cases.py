# Generated by Django 5.0.4 on 2024-04-30 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JusticeFY_app', '0003_alter_lawyer_applytovc_alter_lawyer_cnr_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('CNR', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Case_Type', models.CharField(max_length=255)),
                ('Section_No', models.CharField(max_length=100)),
                ('Filing_Date', models.DateField()),
                ('City', models.CharField(max_length=255)),
                ('Lawyer_Username', models.CharField(max_length=255)),
                ('Judge_Username', models.CharField(max_length=255)),
                ('Description', models.TextField()),
            ],
        ),
    ]
