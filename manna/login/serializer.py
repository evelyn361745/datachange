from manna.models import Infouser
class  InfoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infouser
        fields = "__all__"