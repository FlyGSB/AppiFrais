from django import forms
from fichefrais.models import PieceJointe


class FormPieceJointe(forms.ModelForm):
    """
    Formulaire d'ajout d'une Piece Jointe (Justificatif)
    """
    class Meta:
        model = PieceJointe
        fields = ["piece"]

    def __init__(self, *args, **kwargs):
        super(FormPieceJointe, self).__init__(*args, **kwargs)
        self.fields["piece"].required = False
