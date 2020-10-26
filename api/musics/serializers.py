from django.utils.timezone import now
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from rest_framework import serializers
from musics.models import Music


class MusicSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()

    class Meta:
        model = Music
        # fields = '__all__'
        fields = ('id', 'song', 'singer', 'last_modify_date', 'created', 'days_since_created')

    @extend_schema_field(OpenApiTypes.INT)
    def get_days_since_created(self, obj):
        return (now() - obj.created).days
