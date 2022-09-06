from django import forms 
from .models import Article
# class ArticleForm(forms.Form):
#     NATION_A = 'kr'
#     NATION_B = 'ch'
#     NATION_C = 'jp'
#     NATIONS_CHOICES =[
#         (NATION_A,'한국'),
#         (NATION_B,'중국'),
#         (NATION_C,'일본'),
#     ]
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     nation = forms.ChoiceField(choices= NATIONS_CHOICES)
#     nation = forms.ChoiceField(choices= NATIONS_CHOICES, widget=forms.RadioSelect)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget=forms.TextInput(
            attrs={         # attributes 딕셔너리
                'class':'my-title form-control',
                'placeholder':'Enter the title',
                'maxlength':10,

            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content form-control',
                'placeholder':'Enter the content',
                'rows':5,
                'cols':50,
            }
        ),
        error_messages={
            'required': 'Please enter your content'
        }
    )

    class Meta:             # ModelForm의 정보를 작성하는 곳
        model = Article     # 어떤 모델을 기반으로 할지, 호출 안하고 참조 
                            #  => 함수자체를 그대로 전달해 다른함수에서 필요한 시점에 호출
        fields = '__all__'           # 어떤 모델 필드 중 어떤 것을 출력할지, 
        # all : Article 에서 사용자로부터 입력받는 모든 필드를 의미 
        #exclude = ('title',)        # 빼는 거