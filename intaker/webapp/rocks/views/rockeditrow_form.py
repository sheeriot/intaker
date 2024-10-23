from django import forms
from ..models import Rock, Lake
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
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
        # self.fields['name'].label = "Rock Name"
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='col-md-2 m-0 p-0'),
                Column('marker_id', css_class='col-md-1 m-0 p-0'),
                Column('status', css_class='col-md-2 m-0 p-0'),
                Column('latitude', css_class='col-md-2 m-0 p-0'),
                Column('longitude', css_class='col-md-2 m-0 p-0'),
                Column('depth', css_class='col-md-1 m-0 p-0'),
                Column('size', css_class='col-md-1 m-0 p-0'),
                Column(Submit('submit', 'Update'), css_class='col-md-1 m-0 p-0')
            )
        )