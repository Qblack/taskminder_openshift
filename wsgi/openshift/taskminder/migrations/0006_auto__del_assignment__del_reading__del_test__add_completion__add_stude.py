# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Assignment'
        db.delete_table('taskminder_assignment')

        # Deleting model 'Reading'
        db.delete_table('taskminder_reading')

        # Deleting model 'Test'
        db.delete_table('taskminder_test')

        # Adding model 'Completion'
        db.create_table('taskminder_completion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['taskminder.Task'])),
            ('completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('taskminder', ['Completion'])

        # Adding model 'Student'
        db.create_table('taskminder_student', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['auth.User'])),
            ('program', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('taskminder', ['Student'])

        # Adding M2M table for field universities on 'Student'
        m2m_table_name = db.shorten_name('taskminder_student_universities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('student', models.ForeignKey(orm['taskminder.student'], null=False)),
            ('university', models.ForeignKey(orm['taskminder.university'], null=False))
        ))
        db.create_unique(m2m_table_name, ['student_id', 'university_id'])

        # Adding model 'Task'
        db.create_table('taskminder_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('due_date', self.gf('django.db.models.fields.DateField')()),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['taskminder.Course'])),
            ('pages', self.gf('django.db.models.fields.CharField')(blank=True, max_length=20, null=True)),
            ('time', self.gf('django.db.models.fields.TimeField')(default=None, blank=True, null=True)),
        ))
        db.send_create_signal('taskminder', ['Task'])

        # Adding M2M table for field students on 'Course'
        m2m_table_name = db.shorten_name('taskminder_course_students')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('course', models.ForeignKey(orm['taskminder.course'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['course_id', 'user_id'])


    def backwards(self, orm):
        # Adding model 'Assignment'
        db.create_table('taskminder_assignment', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('due_date', self.gf('django.db.models.fields.DateField')()),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['taskminder.Course'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('completed', self.gf('django.db.models.fields.BooleanField')()),
            ('time', self.gf('django.db.models.fields.TimeField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal('taskminder', ['Assignment'])

        # Adding model 'Reading'
        db.create_table('taskminder_reading', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pages', self.gf('django.db.models.fields.CharField')(null=True, max_length=20, blank=True)),
            ('due_date', self.gf('django.db.models.fields.DateField')()),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['taskminder.Course'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('completed', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('taskminder', ['Reading'])

        # Adding model 'Test'
        db.create_table('taskminder_test', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('due_date', self.gf('django.db.models.fields.DateField')()),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['taskminder.Course'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('completed', self.gf('django.db.models.fields.BooleanField')()),
            ('time', self.gf('django.db.models.fields.TimeField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal('taskminder', ['Test'])

        # Deleting model 'Completion'
        db.delete_table('taskminder_completion')

        # Deleting model 'Student'
        db.delete_table('taskminder_student')

        # Removing M2M table for field universities on 'Student'
        db.delete_table(db.shorten_name('taskminder_student_universities'))

        # Deleting model 'Task'
        db.delete_table('taskminder_task')

        # Removing M2M table for field students on 'Course'
        db.delete_table(db.shorten_name('taskminder_course_students'))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'taskminder.completion': {
            'Meta': {'object_name': 'Completion'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['taskminder.Task']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'taskminder.country': {
            'Meta': {'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'taskminder.course': {
            'Meta': {'object_name': 'Course'},
            'course_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'course_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'course_section': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'professor': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['taskminder.Professor']"}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.User']"})
        },
        'taskminder.professor': {
            'Meta': {'object_name': 'Professor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'universities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['taskminder.University']"})
        },
        'taskminder.province': {
            'Meta': {'object_name': 'Province'},
            'country': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['taskminder.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'taskminder.student': {
            'Meta': {'object_name': 'Student'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'program': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'universities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['taskminder.University']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['auth.User']"})
        },
        'taskminder.task': {
            'Meta': {'object_name': 'Task'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['taskminder.Course']"}),
            'due_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'time': ('django.db.models.fields.TimeField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'taskminder.university': {
            'Meta': {'object_name': 'University'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'province': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['taskminder.Province']"})
        }
    }

    complete_apps = ['taskminder']