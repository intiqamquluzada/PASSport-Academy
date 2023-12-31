# Generated by Django 3.2 on 2023-07-07 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pac', '0002_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=100)),
                ('meet_date', models.DateField()),
                ('meet_type', models.CharField(choices=[('Phone Call', 'Phone Call'), ('Google Meet', 'Google Meet'), ('Offline', 'Offline')], default='Offline', max_length=20)),
                ('education_degree', models.CharField(choices=[('Orta təhsil', 'Orta təhsil'), ('Bakalavr', 'Bakalavr'), ('Magistratura', 'Magistratura')], default='Bakalavr', max_length=100)),
                ('gpa', models.FloatField()),
                ('language_certificate', models.TextField()),
                ('interest_country', models.CharField(max_length=255)),
                ('interested_scholarship_programs', models.CharField(max_length=255)),
                ('work_experience', models.CharField(max_length=255)),
                ('is_met', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Konsultant',
                'verbose_name_plural': 'Konsultantlar',
                'ordering': ('-created_at',),
            },
        ),
    ]
