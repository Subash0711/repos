from Users.models  import  Users
from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password

class userRegisterService:
    @classmethod
    def adduser(cls, request):
        name = request.POST.get('username')
        email = request.POST.get('usermail')
        mobile = request.POST.get('usermobile')
        country = request.POST.get('usercountry')  
        nationality = request.POST.get('usernationality')
        role = request.POST.get('userrole')
        password = request.POST.get('userpassword')  
        encryptpassword = make_password(password)
        data = Users(name=name, email=email, country=country, nationality=nationality, role=role, mobile=mobile,
                     password=encryptpassword)
        data.save()
        return render(request, template_name='login_template.html')

class userLoginService:
    @classmethod
    def userAuthentication(cls,request):
        email =request.POST.get('usermail')
        password =request.POST.get('userpassword')
        try:
            existUser=Users.objects.filter(email=email).first()
            template='user_base_template.html'
            if existUser:
                if check_password(password,existUser.password):
                    cntData=Users.objects.filter(role=existUser.role) 
                    data={'users':cntData,'role':existUser.role}
                    return render(request=None,template_name=template,context=data)
                return render(request,'login_template.html',{'exception':'Please Check your Password'})
        except AttributeError: 
            return render(request,'login_template.html',{'exception':'Please Check your Username'})