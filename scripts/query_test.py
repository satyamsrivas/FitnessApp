from users.models import User,FitnessProfile
from django.db.models.functions import Upper,Length,Coalesce
from django.db import connection
from django.db.models import Avg,Q,Sum,Min,Max,Count,StdDev,Variance,F,Q,Value,CharField,Subquery

def run():
    # user = User.objects.filter().values_list('first_name',flat=True)
    # print(user)
    #AGGREGATE FUNCTION
    # queryset = FitnessProfile.objects.filter(age__gte=20)
    # print(queryset.aggregate(
    #     min = Min('age'),
    #     max = Max('age'),
    #     avg = Avg('age')
    # ))
    #ANNOTATE FUNCTION
    # users = User.objects.annotate(name_len=Length('first_name')).values('first_name','name_len')
    # print(users)

    #F() EXPRESSION
    # fit_profile = FitnessProfile.objects.annotate(avg_age=Avg('age')).filter(age__gte=F('avg_age')).values_list('user__first_name',flat=True).distinct()
    # print(fit_profile) 

    #Coalesce
    # fit_profile = FitnessProfile.objects.annotate(u_bmi=Coalesce('bmi_test',Value('age'))).values('u_bmi')
    # print(fit_profile)

    #Subquery
    user = User.objects.filter(is_staff=True)
    fit_profile = FitnessProfile.objects.filter(user__id__in=Subquery(user.values_list('id',flat=True)))
    print(fit_profile)



    print(connection.queries)