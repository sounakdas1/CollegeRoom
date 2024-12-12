from django import forms
from .models import Chats,Replies,CreateTopic
class ChatForm(forms.ModelForm):
    class Meta:
        model = Chats
        fields = ['chats','image','pdf']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Replies
        fields = ['reply']

class TopicForm(forms.ModelForm):
    class Meta:
        model = CreateTopic
        fields = ['name','description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter topic name','required': 'required'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter topic description'}),
        }