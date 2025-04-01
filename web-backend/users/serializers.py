from rest_framework import serializers
from .models import CustomUser

# ✅ 現有的（保留，用於查詢/顯示使用者）
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'bio', 'date_joined']
        read_only_fields = ['id', 'username']  # username 不可被修改

# ✅ 新增註冊用的 Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']  # bio 可選加

    def create(self, validated_data):
        return CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )