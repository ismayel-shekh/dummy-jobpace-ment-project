# Generated by Django 4.2.11 on 2024-05-21 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=255)),
                ('required_skills', models.TextField()),
                ('image', models.ImageField(upload_to='opportunities/image/')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opportunities', to='organizations.organization')),
            ],
        ),
    ]