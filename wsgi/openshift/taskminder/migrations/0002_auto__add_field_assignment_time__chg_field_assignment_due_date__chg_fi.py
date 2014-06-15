# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Assignment.time'
        db.add_column('taskminder_assignment', 'time',
                      self.gf('django.db.models.fields.TimeField')(null=True, default=None, blank=True),
                      keep_default=False)


        # Changing field 'Assignment.due_date'
        db.alter_column('taskminder_assignment', 'due_date', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Reading.due_date'
        db.alter_column('taskminder_reading', 'due_date', self.gf('django.db.models.fields.DateField')())
        # Adding field 'Test.time'
        db.add_column('taskminder_test', 'time',
                      self.gf('django.db.models.fields.TimeField')(null=True, default=None, blank=True),
                      keep_default=False)


        # Changing field 'Test.due_date'
        db.alter_column('taskminder_test', 'due_date', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):
        # Deleting field 'Assignment.time'
        db.delete_column('taskminder_assignment', 'time')


        # Changing field 'Assignment.due_date'
        db.alter_column('taskminder_assignment', 'due_date', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Reading.due_date'
        db.alter_column('taskminder_reading', 'due_date', self.gf('django.db.models.fields.DateTimeField')())
        # Deleting field 'Test.time'
        db.delete_column('taskminder_test', 'time')


        # Changing field 'Test.due_date'
        db.alter_column('taskminder_test', 'due_date', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        'taskminder.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'completed': ('django.db.models.fields.BooleanField', [], {}),
            'course': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['taskminder.Course']"}),
            'due_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
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
            'professor': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['taskminder.Professor']"})
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
        'taskminder.reading': {
            'Meta': {'object_name': 'Reading'},
            'completed': ('django.db.models.fields.BooleanField', [], {}),
            'course': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['taskminder.Course']"}),
            'due_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'taskminder.test': {
            'Meta': {'object_name': 'Test'},
            'completed': ('django.db.models.fields.BooleanField', [], {}),
            'course': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['taskminder.Course']"}),
            'due_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
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