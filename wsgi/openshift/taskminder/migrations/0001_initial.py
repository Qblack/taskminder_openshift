# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table('taskminder_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('taskminder', ['Country'])

        # Adding model 'Province'
        db.create_table('taskminder_province', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('country', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['taskminder.Country'])),
        ))
        db.send_create_signal('taskminder', ['Province'])

        # Adding model 'University'
        db.create_table('taskminder_university', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('province', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['taskminder.Province'])),
        ))
        db.send_create_signal('taskminder', ['University'])

        # Adding model 'Professor'
        db.create_table('taskminder_professor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('taskminder', ['Professor'])

        # Adding M2M table for field universities on 'Professor'
        m2m_table_name = db.shorten_name('taskminder_professor_universities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('professor', models.ForeignKey(orm['taskminder.professor'], null=False)),
            ('university', models.ForeignKey(orm['taskminder.university'], null=False))
        ))
        db.create_unique(m2m_table_name, ['professor_id', 'university_id'])

        # Adding model 'Course'
        db.create_table('taskminder_course', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('course_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('course_section', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('professor', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['taskminder.Professor'])),
        ))
        db.send_create_signal('taskminder', ['Course'])

        # Adding model 'Assignment'
        db.create_table('taskminder_assignment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('due_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('course', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['taskminder.Course'])),
            ('completed', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('taskminder', ['Assignment'])

        # Adding model 'Reading'
        db.create_table('taskminder_reading', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('due_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('course', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['taskminder.Course'])),
            ('pages', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('completed', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('taskminder', ['Reading'])

        # Adding model 'Test'
        db.create_table('taskminder_test', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('due_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('course', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['taskminder.Course'])),
            ('completed', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('taskminder', ['Test'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table('taskminder_country')

        # Deleting model 'Province'
        db.delete_table('taskminder_province')

        # Deleting model 'University'
        db.delete_table('taskminder_university')

        # Deleting model 'Professor'
        db.delete_table('taskminder_professor')

        # Removing M2M table for field universities on 'Professor'
        db.delete_table(db.shorten_name('taskminder_professor_universities'))

        # Deleting model 'Course'
        db.delete_table('taskminder_course')

        # Deleting model 'Assignment'
        db.delete_table('taskminder_assignment')

        # Deleting model 'Reading'
        db.delete_table('taskminder_reading')

        # Deleting model 'Test'
        db.delete_table('taskminder_test')


    models = {
        'taskminder.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'completed': ('django.db.models.fields.BooleanField', [], {}),
            'course': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['taskminder.Course']"}),
            'due_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'due_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'taskminder.test': {
            'Meta': {'object_name': 'Test'},
            'completed': ('django.db.models.fields.BooleanField', [], {}),
            'course': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['taskminder.Course']"}),
            'due_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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