from django import forms
from fichefrais.models import PieceJointe


class FormPieceJointe(forms.ModelForm):

    class Meta:
        model = PieceJointe
        fields = ["piece"]

    def __init__(self, *args, **kwargs):
        super(FormPieceJointe, self).__init__(*args, **kwargs)
        self.fields["piece"].required = False
