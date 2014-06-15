# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Reading.pages'
        db.alter_column('taskminder_reading', 'pages', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

    def backwards(self, orm):

        # Changing field 'Reading.pages'
        db.alter_column('taskminder_reading', 'pages', self.gf('django.db.models.fields.CharField')(default='all', max_length=20))

    models = {
        'taskminder.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'completed': ('django.db.models.fields.BooleanField', [], {}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['taskminder.Course']"}),
            'due_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.TimeField', [], {'blank': 'True', 'default': 'None', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
            'professor': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['taskminder.Professor']"})
        },
        'taskminder.professor': {
            'Meta': {'object_name': 'Professor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'universities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['taskminder.University']"})
        },
        'taskminder.province': {
            'Meta': {'object_name': 'Province'},
            'country': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['taskminder.Country']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'taskminder.reading': {
            'Meta': {'object_name': 'Reading'},
            'completed': ('django.db.models.fields.BooleanField', [], {}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['taskminder.Course']"}),
            'due_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'taskminder.test': {
            'Meta': {'object_name': 'Test'},
            'completed': ('django.db.models.fields.BooleanField', [], {}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['taskminder.Course']"}),
            'due_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.TimeField', [], {'blank': 'True', 'default': 'None', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'taskminder.university': {
            'Meta': {'object_name': 'University'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'province': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['taskminder.Province']", 'unique': 'True'})
        }
    }

    complete_apps = ['taskminder']