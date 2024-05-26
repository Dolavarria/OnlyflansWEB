from django import forms


#Agregamos sufijo Form a ContactForm para evitar conflictos con el modelo ContactForm
class ContactFormModelForm(forms.Form):
    customer_email=forms.EmailField(label='Correo')
    customer_name=forms.CharField(label='Nombre', max_length=64)
    message=forms.CharField(label='Mensaje')
    