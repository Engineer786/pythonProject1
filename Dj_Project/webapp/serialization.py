from rest_framework import serializers
from webapp.models import Employee
# def validate_employee(value):
#     if value[0].islower():
#         raise serializers.ValidationError('Name must be started with capital letter')
class EmpSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # emp_id = serializers.IntegerField()
    # name = serializers.CharField(max_length=50, validators=[validate_employee])
    # salary = serializers.DecimalField(max_digits=10, decimal_places=2)
    # job = serializers.CharField(max_length=60)
    # company = serializers.CharField(max_length=60)
    class Meta:
        model = Employee
        fields = '__all__'

    def validate(self, data):
        name = data.get('name')
        if name[0].islower():
            raise serializers.ValidationError('Name must be started with capital letter')

        salary = data.get('salary')
        if salary< 10000:
            raise serializers.ValidationError('Salary must be greater than 10000')



        return data
    # def validate_salary(self, value):
    #     if value < 10000:
    #         raise serializers.ValidationError("Salary must be greater than 10000")
    #     return value

    def create(self, validated_data):
        emp = Employee.objects.create(**validated_data)
        return emp

    def update(self, instance, validated_data):
        instance.emp_id = validated_data.get('emp_id', instance.emp_id)
        instance.name = validated_data.get('name', instance.name)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.job = validated_data.get('job', instance.job)
        instance.company = validated_data.get('company', instance.company)
        instance.save()
        return instance