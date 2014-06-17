# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Completion.user'
        db.alter_column('taskminder_completion', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['taskminder.UserProfile']))
        # Adding unique constraint on 'UserProfile', fields ['username']
        db.create_unique('taskminder_userprofile', ['username'])


    def backwards(self, orm):
        # Removing unique constraint on 'UserProfile', fields ['username']
        db.delete_unique('taskminder_userprofile', ['username'])


        # Changing field 'Completion.user'
        db.alter_column('taskminder_completion', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

    models = {
        'taskminder.completion': {
            'Meta': {'object_name': 'Completion'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['taskminder.Task']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['taskminder.UserProfile']"})
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
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['taskminder.UserProfile']"})
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
        'taskminder.task': {
            'Meta': {'object_name': 'Task'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['taskminder.Course']"}),
            'due_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'time': ('django.db.models.fields.TimeField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'taskminder.university': {
            'Meta': {'object_name': 'University'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'province': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['taskminder.Province']"})
        },
        'taskminder.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'program': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'universities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['taskminder.University']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['taskminder']