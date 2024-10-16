from django import forms
from .models import Rock
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Field, Row, Column


class RockForm(forms.ModelForm):
    class Meta:
        model = Rock
        fields = [
                'lake',
                'name', 'marker_id', 'status',
                'latitude', 'longitude',
                'depth', 'size',
                'more_info'
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.fields['lake'].label = "Lake Name"
        self.fields['name'].label = "Rock Name"
        self.fields['marker_id'].label = "Marker ID"
        self.helper.layout = Layout(
            Row(
                Column('lake', css_class='col-md-4 mx-1'),
            ),
            Row(
                Column('marker_id', css_class='col-md-2 mx-1'),
                Column('name', css_class='col-md-4 mx-1'),
                Column('status', css_class='col-md-4 mx-1')
            ),
            Row(
                Column('latitude', css_class='col-md-3 mx-1'),
                Column('longitude', css_class='col-md-3 mx-1'),
            ),
            Row(
                Column('depth', css_class='col-md-3 mx-1'),
                Column('size', css_class='col-md-3 mx-1'),
            ),
            Field('more_info'),
            Submit('submit', 'Submit', css_class='button white'),
        )