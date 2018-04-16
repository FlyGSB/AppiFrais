from django import forms
from fichefrais.models import PiecesJointe


class FormPieceJointe(forms.ModelForm):

    class Meta:
        model = PiecesJointe
        fields = ["piece"]

    def __init__(self, *args, **kwargs):
        super(FormPieceJointe, self).__init__(*args, **kwargs)
        self.fields["piece"].required = False
