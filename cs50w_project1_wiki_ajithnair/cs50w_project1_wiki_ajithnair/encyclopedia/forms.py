import re
from .util import list_entries

from django import forms


class NewPageForm(forms.Form):
    """Used to create a new page"""

    title = forms.CharField(
        max_length=100,
        required=True
    )

    entry = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def checkTitle(self):
        """Checks if title exists"""

        title = self.cleaned_data.get('title')
        if title in list_entries():
            raise forms.ValidationError('Unfortunately this title already exists, please select another!')

        return title

    def save_entry_to_file(self, title, entry):
        """Used to save entry to file *.md"""

        with open(f'./entries/{title}.md', 'x') as ef:
            ef.write(f'# {title}\n' + entry)


class EditPageForm(NewPageForm):
    """Used to edit pre-existing entries"""

    def checkTitle(self):
        title = self.cleaned_data.get('title')
        return title

    def update_entry_file(self, title, entry):
        """Used to update entry file *.md"""

        with open(f'./entries/{title}.md', 'w') as ef:
            ef.write(f'# {title}\n' + entry)


class SearchForm(forms.Form):
    """Used to search"""

    keyword = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Search Encyclopedia'}))