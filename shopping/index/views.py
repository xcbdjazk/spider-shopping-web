# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django import forms
from django.forms import widgets
from django.forms import fields
from index import models
# import os
# os.path.join()
from django.db.models import Q

# Create your views here.
# host_product=[]
# for i in range(1,200):
#     host_product.append(i)

class Paging(object) :

    ''' 生成分页'''
    def __init__(self,obj,current_page,counte_page,paging_page):
                    #obj 传入的数据对象
                    #current_page获取的当前页码
                    #counte_page 每页显示数据量
                    #paging_page 页码显示多少页
        self.obj=obj
        self.current_page=current_page
        self.counte_page=counte_page
        self.paging_page=paging_page
    def counte(self):
        current_page = int(self.current_page)
        # all_count_product = len(self.obj)  # 获取查询is_host的长度
        strat = (current_page - 1) * self.counte_page
        end = current_page * self.counte_page
        data_page = self.obj[strat:end]
        return data_page
    def paging_all(self):
        all_count_product = len(self.obj)  # 获取查询obj的长度
      #  v, y = divmod(all_count_product, 12)  # v:all_count_product/12的商，y ：余数
        return divmod(all_count_product, self.counte_page)
    def paging_f(self,v,y,path):
        if y:
            v += 1
        if v < self.paging_page:  # 分7页当总页数小于7
            start_page = 1
            end_page = v + 1
        else:
            if self.current_page <=self.paging_page//2+1:  # 当前页码小于4
                start_page = 1
                end_page = self.paging_page + 1
            elif self.current_page + 3 >= v:  # 当前页码+3大于最大页码
                start_page = v - self.paging_page + 1
                end_page = v + 1
            else:  # 其余正常情况分七页
                start_page = self.current_page - self.paging_page // 2
                end_page = self.current_page + self.paging_page// 2 + 1
        page_list = []
        page_list.append('''
                <li>
          <a href="%s?p=1" aria-label="Previous">
            <span aria-hidden="true">&laquo;&laquo;</span>
          </a>
        </li>
                '''%(path))
        if self.current_page == 1:
            temp = '''
        <li>
          <a href="javascript:void(0)" aria-label="Previous">
            <span aria-hidden="true">&laquo;</span>
          </a>
        </li>
                '''
        else:
            temp = '''<li>
          <a href="%s?p=%s" aria-label="Previous">
            <span aria-hidden="true">&laquo;</span>
          </a>
        </li>''' % (path,self.current_page - 1)
        page_list.append(temp)
        for i in range(start_page, end_page):
            if i == self.current_page:
                page_list.append("<li><a style='color:red' href='%s?p=%s'>%s</a></li>" % (path,i, i))
            else:
                page_list.append("<li><a href='%s?p=%s'>%s</a></li>" % (path,i, i))

        if not v:
            # print("aaaaaaaaaaaaaaaaaa",v)
            temp = '''<li>
                     <a href="javascript:void(0)" aria-label="Next">
                       <span aria-hidden="true">&raquo;</span>
                     </a>
                   </li>'''
        else:
            # print("aaaaaaaaaaaaaaaaaa", v)
            temp = '''<li>
          <a href="%s?p=%s" aria-label="Next">
            <span aria-hidden="true">&raquo;</span>
          </a>
        </li>''' % (path,self.current_page + 1)



        page_list.append(temp)
        if  v==0:
            v=1
        temp = '''<li>
                 <a href="%s?p=%s" aria-label="Next">
                   <span aria-hidden="true">&raquo;&raquo;</span>
                 </a>
               </li>''' % (path,v)
        page_list.append(temp)
        return page_list

def index_top(request):
    # from django.contrib.auth import authenticate, login
    #
    # if request.method == 'POST':
    #         username = request.POST.get('username')
    #
    # password = request.POST.get('password')
    # user = authenticate(username=username, password=password)
    # if user:
    #     if user.is_active:
    #         login(request, user)
    # return HttpResponseRedirect('/index/index_info')
    # request.user
    # username = '登录'
    if request.session['is_login']:
        username=models.User.objects.filter(uid=request.session['user']).first()
        username=username.name
        # print(username)
        return render(request, 'top.html', {'username': username})
    else:
        username = '登录'
    return render(request,'top.html',{'username':username})
#主页
def index_info(request):
    # print(request.session['is_login'])
    if request.method=="GET":
        # a=request.
        # print(a)
        host_product=models.Product.objects.filter(is_host=True)
        #分页
        current_page=request.GET.get("p",1)#获取当前页码
        current_page=int(current_page)
    #
    #     strat=(current_page-1)*12
    #     end=current_page*12
    #     data_page=host_product[strat:end]
    #     all_count_product = len(host_product)  # 获取查询is_host的长度
    #     v,y=divmod(all_count_product,12)#v:all_count_product/12的商，y ：余数
    #     print(v,y)
    #     if y:
    #         v+=1
    #     if v<7:#分7页当总页数小于7
    #         start_page=1
    #         end_page=v+1
    #     else:
    #         if current_page<=4:#当前页码小于4
    #             start_page=1
    #             end_page=7+1
    #         elif current_page+3>=v:#当前页码+3大于最大页码
    #             start_page=v-7+1
    #             end_page=v+1
    #         else:#其余正常情况分七页
    #             start_page=current_page-7//2
    #             end_page=current_page+7//2+1
    #     page_list=[]
    #     page_list.append('''
    #         <li>
    #   <a href="/index/index_info/?p=1" aria-label="Previous">
    #     <span aria-hidden="true">&laquo;&laquo;</span>
    #   </a>
    # </li>
    #         ''')
    #     if current_page==1:
    #         temp='''
    # <li>
    #   <a href="javascript:void(0)" aria-label="Previous">
    #     <span aria-hidden="true">&laquo;</span>
    #   </a>
    # </li>
    #         '''
    #     else:
    #         temp='''<li>
    #   <a href="/index/index_info/?p=%s" aria-label="Previous">
    #     <span aria-hidden="true">&laquo;</span>
    #   </a>
    # </li>'''%(current_page-1)
    #     page_list.append(temp)
    #     for i in range(start_page,end_page):
    #         if i== current_page:
    #             page_list.append("<li><a style='color:red' href='/index/index_info/?p=%s'>%s</a></li>"%(i,i))
    #         else:
    #             page_list.append("<li><a href='/index/index_info/?p=%s'>%s</a></li>" % (i, i))
    #     print(page_list)
    #     if current_page==v:
    #         temp='''<li>
    #   <a href="javascript:void(0)" aria-label="Next">
    #     <span aria-hidden="true">&raquo;</span>
    #   </a>
    # </li>'''
    #     else:
    #         temp='''<li>
    #   <a href="/index/index_info/?p=%s" aria-label="Next">
    #     <span aria-hidden="true">&raquo;</span>
    #   </a>
    # </li>'''%(current_page+1)
    #     page_list.append(temp)
    #     temp = '''<li>
    #          <a href="/index/index_info/?p=%s" aria-label="Next">
    #            <span aria-hidden="true">&raquo;&raquo;</span>
    #          </a>
    #        </li>'''%(v)
    #     page_list.append(temp)
        # host_product=models.Product.objects.all()
        pae=Paging(host_product,current_page,12,7)
        data_page=pae.counte()
        v,y=pae.paging_all()
        # print(v)
        page_list=pae.paging_f(v,y,'/index/index_info/')
        return render(request,"index.html",{'host_product':data_page,'page_list':page_list})
# 添加商城商品
def add_product(request):
    if request.method=="GET":
        return render(request,"add_product.html")
    elif request.method=="POST":
        name=request.POST.get("pname")
        img=request.FILES.get("img_path")
        import os
        file_path=os.path.join("static/product_img/",img.name)
        f=open(file_path,"wb")
        for i in img.chunks():
            f.write(i)
        ice=request.POST.get("price")
        ock=request.POST.get("Stock")
        ishost=request.POST.get('is_host')
        recom=request.POST.get('recommend')
        sort=request.POST.get('sort')

        models.Product.objects.create(
            pname=name,
            img_path=file_path,
            price=ice,
            Stock=ock,
            is_host=ishost,
            recommend=recom,
            product_class_id=sort,
        )

        return redirect("/index/addproduct")
# 商品详情页
def shopdetail(request,nid):
    # print(nid)
    if request.method=="GET":
        obj=models.Product.objects.filter(pid=nid).first()
        # host_product = models.Product.objects.filter(is_host=True)
        # size=len(host_product)
        # host_product=host_product[size-3:size]
        # return render(request,'shopdetail.html',{"obj":obj,'host_product':host_product})
        return render(request,'shopdetail.html',{"obj":obj})
    elif request.method=='POST':
        img_path=request.POST.get("img_path")
        print(img_path)
        return HttpResponse('ok')
#模糊查询Cookie
def login(request):
    u = request.POST.get('seek')

    # from django.utils.encoding import smart_str
    # u1=smart_str(u)
    # print(u1)
    # 对登录帐号进行验证，如果通过，执行下面
    # from django.utils.encoding import smart_str
    # u=smart_str(u)
    import json
    u=json.dumps(u)
    print(u)
    print(type(u),"#######")
    res = redirect('/index/seek/')
    res.set_cookie('seek',u)
    # res.set_cookie('cookie',"我是COOKIE")
    return res
#模糊查询结果
def seek(request):
    print('########################')
    seek = request.COOKIES.get('seek')
    # print(seek)
    import json

    seek=json.loads(seek)
    print(request.session.get("Checkcode"),"!@#$%^&^##")
    print(seek)

    if request.method=="GET":
            current_page = request.GET.get("p", 1)  # 获取当前页码
            seek1 = request.GET.get("seek", seek)  # 获取当前页码
            obj = models.Product.objects.filter(pname__icontains=seek1)
            current_page = int(current_page)
            pae = Paging(obj, current_page, 12, 7)
            data_page = pae.counte()
            v, y = pae.paging_all()
            page_list = pae.paging_f(v, y,'/index/seek/')
            return render(request,'seek.html',{"obj":data_page,"page_list":page_list})
#图片验证码
def check_code(request):
    from utils.check_code import create_validate_code
    img,code= create_validate_code()
    from io import BytesIO
    msstream = BytesIO()
    img.save(msstream, "PNG")
    # print(img,code)
    request.session['Checkcode']=code
    return HttpResponse(msstream.getvalue())
#注册页面
class Fm1(forms.Form):
    uname=fields.CharField(
        max_length=12,
        min_length=6,
        widget=widgets.TextInput(attrs={'class':'form-control','id':'inputPassword3',"placeholder":"请输入用户名"}),
        error_messages={'required':'用户名不能为空','max_length':'长度不能超过12位','min_length':'长度不能少于6位'}

    )
    pwd=fields.CharField(
        max_length=12,
        min_length=6,
        widget=widgets.PasswordInput(attrs={'class':'form-control','id':'inputPassword3',"placeholder":"请输入密码"})
    )
    name=fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control', 'id': 'usercaption', "placeholder": "请输入姓名"}),
        error_messages={'required':'姓名不能为空'})
    email=fields.EmailField(
        widget=widgets.TextInput(attrs={'class': 'form-control', 'id': 'inputEmail3', "placeholder": "请输入邮箱"}),
        error_messages={'required': '邮箱不能为空','invalid':'邮箱格式不对'}
    )
    gender=fields.CharField(
        # choices=((0,'男'),(1,'女')),
        # initial=0,
        widget=widgets.RadioSelect(attrs={'type':'date'})
    )
    # gender = fields.RegexField()

    dtime=fields.CharField(
        widget=widgets.DateInput(attrs={'type':'date','class': 'form-control'}),
        error_messages={'required': '邮箱不能为空'}
        )

        # widget=widgets.DateInput(attrs={'type':'date','class': 'form-control'}),


def register(request):
    err_code=''
    if request.method=="POST":
        is_existi= models.User.objects.filter(uname=request.POST.get('uname'))
        obj = Fm1(request.POST)
        if is_existi:
            err_code='用户名已存在'
            return render(request, 'register.html', {'obj': obj, "err_code": err_code})
        obj=Fm1(request.POST)
        obj.is_valid()
        b = obj.cleaned_data

        # c=request.POST.get("gender")
        # a=b.get('gender')
        # a=obj.cleaned_data
        # print(b,a,c,'###############')

        if  request.POST.get('checkcode').upper()==request.session['Checkcode'].upper():
            models.User.objects.create(**b)
            return redirect('/index/login_user/')
        else:
            err_code='验证码错误'
            return render(request,'register.html',{'obj': obj,"err_code":err_code})
    elif request.method=="GET":
        obj=Fm1()
        return render(request, "register.html", {'obj': obj,'err_code':err_code})
        # username=request.POST.get('username')
        # pwd=request.POST.get('password')
        # panme=request.POST.get('pname')
        # email=request.POST.get('email')
        # gender=request.POST.get('inlineRadioOptions')
        # dtime=request.POST.get('datetime')
        # print(username,pwd,panme,email,gender,dtime)
        # models.User.objects.create(
        #     uname=username,
        #     pwd=pwd,
        #     name=panme,
        #     email=email,
        #     gender=gender,
        #     dtime=dtime
        # )
    # return render(request,"register.html",{'obj':obj})
#登录页面
def login_user(request):
    if request.method=="POST":

        obj=Fm1(request.POST)
        obj.is_valid()
        user=models.User.objects.filter(uname=obj.cleaned_data.get("uname"),pwd=obj.cleaned_data.get("pwd")).first()
        if request.POST.get('checkcode').upper()==request.session['Checkcode'].upper():
            if user:
                request.session['is_login']=True
                request.session['user']=user.uid#用户id
                request.session['username']=user.name#用户名
                if request.POST.get('login_15'):
                    request.session.set_expiry(60*60*24*15)
                    # request.session.set_expiry(10)

                return redirect('/index/index_info/')
            else:
                err_user="用户名或密码错误"
                return render(request, 'login_user.html', {'obj': obj, "err_user": err_user})
        else:
            err_user="验证码错误"
            return render(request, 'login_user.html', {'obj': obj,"err_user":err_user})

    elif request.method=="GET":
        print(request.GET.get("next"))
        err_user=''
        obj = Fm1()
        return render(request,'login_user.html',{'obj':obj,"err_user":err_user})
#注销登录
def loginout(request):
    request.session.clear()
    return redirect('/index/index_info')
def cart(request):
    if request.session.get('is_login',None):
        if  request.method == "GET":
            obj=models.Cart.objects.filter(user_id=request.session.get('user'))
            # print(obj.values())
            return render(request, "cart.html",{"obj":obj})
        if request.method == "POST":
            img_path = request.POST.get("img_path")
            pname = request.POST.get("pname")
            price = float(request.POST.get("price"))
            import time
            ctime=time.strftime("%Y-%m-%d")
            models.Cart.objects.create(
                    img_path=img_path,
                    pname=pname,
                    price=price,
                    count=1,
                    totalprice=price*1,
                    ctime=ctime,
                    user_id=request.session['user']
                )
        print(price,type(price),'#####',ctime)
        return render(request,"cart.html")
    else:
        return redirect('/index/login_user')
def ttt(request):
    return render(request,"111.html")
def order(request):
    if request.method=="POST":
        a = request.POST.getlist('order')

        obj=[]
        import time


        for i in a:

            # obj.append(models.Cart.objects.filter(cid=i).values())
            x=models.Cart.objects.get(cid=i)
            obj=model_to_dict(x)
            ctime = time.strftime("%Y-%m-%d")
            models.Order_info.objects.create(
                # oid=obj['cid'],
                img_path=obj['img_path'],
                pname=obj['pname'],
                price=obj['price'],
                count=obj['count'],
                totalprice=obj['totalprice'],
                ctime=ctime,
                user_id=request.session['user']

            )
            models.Cart.objects.filter(cid=i).delete()
            # print(obj['cid'])
            # print(type(obj))
    return redirect('/index/order_info')
def spider(request):
    if request.method == "GET":
        obj=models.Spider_Porduct.objects.filter(spider_id__in=[1,2,3])
        current_page = request.GET.get("p", 1)  # 获取当前页码
        # seek1 = request.GET.get("seek", seek)  # 获取当前页码
        current_page = int(current_page)
        pae = Paging(obj, current_page, 18, 7)
        data_page = pae.counte()
        v, y = pae.paging_all()
        page_list = pae.paging_f(v, y, '/index/spider_nanzhuang/')
        return render(request, 'spider.html', {"obj": data_page, "page_list": page_list})
        # return render(request,'spider.html',{'obj': obj})
    # return render(request,'spider.html',{})
def taobao(request,nid):
    # spid=request.GET.get('spid')
    obj=models.Spider_Porduct.objects.filter(spider_id=nid)
    current_page = request.GET.get("p", 1)
    current_page = int(current_page)
    pae = Paging(obj, current_page, 18, 7)
    data_page = pae.counte()
    v, y = pae.paging_all()
    page_list = pae.paging_f(v, y, '/index/taobao-%s'%nid)
    return render(request, 'spider.html', {"obj": data_page, "page_list": page_list})
def order_info(request):
    if request.session.get('is_login',None):
        if request.method=="GET":
            obj = models.Order_info.objects.filter(user_id=request.session['user'])
            return render(request,"order_info.htm",{'obj':obj})
        elif request.method=="POST":
            a= request.POST.get('check_order')
            print(a)
            return render(request, "order_info.htm")
    else:
        return redirect("/index/login_user")
def spider_nvzhuang(request):
    if request.method == "GET":
        obj=models.Spider_Porduct.objects.filter(spider_id__in=[4,5,6,7,8,9,10])
        current_page = request.GET.get("p", 1)  # 获取当前页码
        # seek1 = request.GET.get("seek", seek)  # 获取当前页码
        current_page = int(current_page)
        pae = Paging(obj, current_page, 18, 7)
        data_page = pae.counte()
        v, y = pae.paging_all()
        page_list = pae.paging_f(v, y, '/index/spider_nvzhuang/')
        return render(request, 'spider_nvzhuang.html', {"obj": data_page, "page_list": page_list})
def taobao_nvzhuang(request,nid):
    if request.method=="GET":
        obj = models.Spider_Porduct.objects.filter(spider_id=nid)
        current_page = request.GET.get("p", 1)
        current_page = int(current_page)
        pae = Paging(obj, current_page, 18, 7)
        data_page = pae.counte()
        v, y = pae.paging_all()
        page_list = pae.paging_f(v, y, '/index/taobao_nvzhuang-%s/' % nid)
        return render(request, 'spider_nvzhuang.html', {"obj": data_page, "page_list": page_list})