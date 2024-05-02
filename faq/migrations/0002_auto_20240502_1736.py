from django.db import migrations, models
import django.db.models.deletion
import datetime

def set_default_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    FAQ = apps.get_model('faq', 'FAQ')
    default_user = User.objects.get(username='admin') 
    FAQ.objects.update(created_by=default_user)

def apply_migration(apps, schema_editor):
    FAQ = apps.get_model('faq', 'FAQ')
    db_alias = schema_editor.connection.alias
    FAQ.objects.using(db_alias).all().update(created_at=datetime.datetime.now())

class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'), 
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faq',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.RunPython(apply_migration),
    ]