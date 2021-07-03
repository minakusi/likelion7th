from django.forms import ModelForm, Form
from .models import Catlist

class CatlistPost(ModelForm):
    class Meta:
        model = Catlist
        fields = ['name', 'furious','gender', 'age','family','food','touch','catimage','mapimage','info']
        labels = {
            'name':'고양이 애칭',
            'age':'나이',
            'gender':'성별',
            'info':'상세정보'

        }
     
   
        
class Catupdate(ModelForm):
    class Meta:
        model = Catlist
        fields = [ 'name', 'age', 'gender', 'info', 'catimage' ,'pos_y', 'pos_x' ]       
