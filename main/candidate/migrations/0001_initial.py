# Generated by Django 4.2.2 on 2023-08-20 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidatedirectory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruiter_alert', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('role', models.IntegerField(blank=True, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('contact_no_primary', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('contact_no_alternate', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('referred_by_other', models.CharField(blank=True, max_length=250, null=True)),
                ('address_line', models.CharField(blank=True, max_length=255, null=True)),
                ('pincode', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('education_specialization_other', models.TextField(blank=True, null=True)),
                ('education_institution_other', models.TextField(blank=True, null=True)),
                ('years_of_experience', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('current_employer', models.CharField(blank=True, max_length=100, null=True)),
                ('current_designation', models.TextField(blank=True, null=True)),
                ('current_monthly_salary', models.IntegerField(blank=True, null=True)),
                ('expected_monthly_salary', models.IntegerField(blank=True, null=True)),
                ('notice_period', models.CharField(blank=True, max_length=50, null=True)),
                ('photo_path', models.TextField(blank=True, null=True)),
                ('resume_path', models.TextField(blank=True, null=True)),
                ('login_time', models.DateTimeField(blank=True, null=True)),
                ('logout_time', models.DateTimeField(blank=True, null=True)),
                ('ip_address', models.CharField(blank=True, max_length=15, null=True)),
                ('geo_location', models.CharField(blank=True, max_length=50, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('modified_date', models.DateTimeField(blank=True, null=True)),
                ('modified_by', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'candidatedirectory',
                'managed': False,
            },
        ),
    ]
