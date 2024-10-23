from django import forms
from ..models import Rock, Lake
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from icecream import ic

class RockEditRowForm(forms.ModelForm):
    class Meta:
        model = Rock
        fields = [
            'name', 'marker_id', 'status',
            'latitude', 'longitude',
            'depth', 'size',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Row(
                Column(Field('name', template='tablefields.html'), css_class='col-md-2 m-0 p-0'),
                Column(Field('marker_id', template='tablefields.html'), css_class='col-md-1 m-0 p-0'),
                Column(Field('status', template='tablefields.html'), css_class='col-md-2 m-0 p-0'),
                Column(Field('latitude', template='tablefields.html'), css_class='col-md-2 m-0 p-0'),
                Column(Field('longitude', template='tablefields.html'), css_class='col-md-2 m-0 p-0'),
                Column(Field('depth', template='tablefields.html'), css_class='col-md-1 m-0 p-0'),
                Column(Field('size', template='tablefields.html'), css_class='col-md-1 m-0 p-0'),
                Column(Submit('submit', 'Update', css_class="px-1 py-0 m-0 mb-1 tableedit"), css_class='col-md-1 m-0 p-0')
            )
        )