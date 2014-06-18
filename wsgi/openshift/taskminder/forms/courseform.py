__author__ = 'Q'
from django import forms
from taskminder.models import Course, Country, Province, University
import selectable.forms as selectable
from taskminder.lookup import ProvinceLookup


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_name','course_code','course_section','professor')

    def save(self, commit=True):
        course = Course(
            course_name=self.cleaned_data.get("course_name"),
            course_code=self.cleaned_data.get("course_code"),
            section=self.cleane_data.get("course_section")
        ).save(commit=False)
        course.add_professor(self.cleaned_data.get('professor'))
        if commit:
            course.save()
        return course






class JoinCourseForm(forms.Form):
    country = forms.ModelChoiceField(queryset=Country.objects.order_by('name'))
    province =selectable.AutoCompleteSelectField(
        lookup_class=ProvinceLookup,
        label='Province/State',
        required=True,
        widget=selectable.AutoComboboxSelectWidget    )

    university = forms.ModelChoiceField(queryset=University.objects.order_by('name'))