from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML, Button, Submit


class SearchForm(forms.Form):
    wo_no = forms.CharField(required=False, label="工單號碼")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_show_errors = True

        self.helper.layout = Layout(
            Div(
                Div('wo_no', css_class='col-md-10'),
                Div(Submit('search', '查詢', css_class='btn btn-info'),
                    css_class='col-md-2 d-flex align-items-center search_btn_fix pt-3'),
                css_class='row'),
        )
