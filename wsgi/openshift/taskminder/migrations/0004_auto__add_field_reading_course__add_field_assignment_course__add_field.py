# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Reading.course'
        db.add_column('taskminder_reading', 'course',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['taskminder.Course']),
                      keep_default=False)

        # Removing M2M table for field course on 'Reading'
        db.delete_table(db.shorten_name('taskminder_reading_course'))

        # Adding field 'Assignment.course'
        db.add_column('taskminder_assignment', 'course',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['taskminder.Course']),
                      keep_default=False)

        # Removing M2M table for field course on 'Assignment'
        db.delete_table(db.shorten_name('taskminder_assignment_course'))

        # Adding field 'Test.course'
        db.add_column('taskminder_test', 'course',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['taskminder.Course']),
                      keep_default=False)

        # Removing M2M table for field course on 'Test'
        db.delete_table(db.shorten_name('taskminder_test_course'))


    def backwards(self, orm):
        # Deleting field 'Reading.course'
        db.delete_column('taskminder_reading', 'course_id')

        # Adding M2M table for field course on 'Reading'
        m2m_table_name = db.shorten_name('taskminder_reading_course')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('reading', models.ForeignKey(orm['taskminder.reading'], null=False)),
            ('course', models.ForeignKey(orm['taskminder.course'], null=False))
        ))
        db.create_unique(m2m_table_name, ['reading_id', 'course_id'])

        # Deleting field 'Assignment.course'
        db.delete_column('taskminder_assignment', 'course_id')

        # Adding M2M table for field course on 'Assignment'
        m2m_table_name = db.shorten_name('taskminder_assignment_course')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('assignment', models.ForeignKey(orm['taskminder.assignment'], null=False)),
            ('course', models.ForeignKey(orm['taskminder.course'], null=False))
        ))
        db.create_unique(m2m_table_name, ['assignment_id', 'course_id'])

        # Deleting field 'Test.course'
        db.delete_column('taskminder_test', 'course_id')

        # Adding M2M table for field course on 'Test'
        m2m_table_name = db.shorten_name('taskminder_test_course')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('test', models.ForeignKey(orm['taskminder.test'], null=False)),
            ('course', models.ForeignKey(orm['taskminder.course'], null=False))
        ))
        db.create_unique(m2m_table_name, ['test_id', 'course_id'])


    models = {
        'taskminder.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'completed': ('django.db.models.fields.BooleanField', [], {}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['taskminder.Course']"}),
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
            'country': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['taskminder.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'taskminder.reading': {
            'Meta': {'object_name': 'Reading'},
            'completed': ('django.db.models.fields.BooleanField', [], {}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['taskminder.Course']"}),
            'due_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'taskminder.test': {
            'Meta': {'object_name': 'Test'},
            'completed': ('django.db.models.fields.BooleanField', [], {}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['taskminder.Course']"}),
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