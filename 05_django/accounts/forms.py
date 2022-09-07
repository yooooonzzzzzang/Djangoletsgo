from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # model = User    # 장고 직접 참조 권장안함 get_user_model 사용
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        # 필요한 것만 선택
        fields = ('email', 'first_name', 'last_name',)
