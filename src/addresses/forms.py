from django import forms

from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            # 'billing_profile',
            # 'address_type',
            'address_line_1',
            'state',
            'address_line_2',
            'city',
            'country',

        ]

        labels = {
            "address_line_1": "Địa chỉ",
            "address_line_2": "Quận",
            "city": "Thành phố",
            "country": "Quốc gia",
            "state": "Phường",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address_line_1'].widget.attrs.update({'class': 'form-control'})
        self.fields['address_line_2'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].widget.attrs.update({'class': 'form-control'})
        self.fields['country'].widget.attrs.update({'class': 'form-control'})
        self.fields['state'].widget.attrs.update({'class': 'form-control'})
