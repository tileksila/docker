from rest_framework import serializers
from mainapp.models import DONE, IN_PROGRESS, InnerTraid, STATUS
import datetime


class InnerTraidDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = InnerTraid
        fields = (
            'id','name','status','date_create','date_update','date_finished',
        )

        read_only_fields = (
             'id','name','date_create','date_update','date_finished',
        )

    def update(self, instance, validated_data):
        if validated_data.get('status') == IN_PROGRESS:
            instance.status = IN_PROGRESS
            instance.date_update = datetime.datetime.now()
        elif validated_data.get('status') == DONE:
            instance.status = DONE
            instance.date_update = datetime.datetime.now()
        instance.save()

        return instance