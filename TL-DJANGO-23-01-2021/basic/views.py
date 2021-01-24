from django.shortcuts import render ,redirect
from django.http import HttpResponse, JsonResponse
from .util import otp_generator, send_otp_email, validate_otp
from .models import Profile  , Country  , State , User , language_list, filter_details
from itertools import chain
import json
from django.core.paginator import Paginator
from django import template
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request , user_id) : 
    request.session['userid'] = user_id
    return render( request , 'search.html')

def home(request):
    return render(request ,'VI/Homepage/index.html')

def loginPage(request):
    return render(request ,'VI/LoginPage/index.html')

def register(request):
    return render(request ,'VI/Registration-Page/index.html')

def validate_email(new_email):
    validateuser = User.objects.raw("select * from user where email_id = '"+ new_email + "';")
    if  validateuser  :
        for i in validateuser : 
            return True
    else:
        return False

def sndRegister(request):
    username = request.GET.get('username')
    email = request.GET.get('email')
    pwd = request.GET.get('pwd')
    usertype = request.GET.get('type')
    otp = request.GET.get('otp')

    sent_otp = request.session['auth_otp']
    sent_email = request.session['auth_email']
    
    result = validate_otp(otp, sent_otp, email, sent_email)

    if not result["success"]:
        return redirect('register')

    result = {"success": True, "message": "User Registered"}
    userentryqry = User.objects.create(username=username, email_id=email, password=pwd, role_id=usertype)
    #if user exist - go to search page
    if  userentryqry  :
        request.session['userid'] = userentryqry.id
        return render( request , 'VI/Profilepage-01/index.html')
    else:
        return redirect('register')


def sendOtp(request):
    return render(request, 'otp.html')

def send_otp(request):
    email = request.GET.get('email')

    validation = validate_email(email)
    if not validation:
        otp = otp_generator()
        otp_status = send_otp_email(email, otp)
        if not otp_status:
            result = {"success": False, "message": "incorrect email"}
            return render( request , 'otp.html')

        request.session["auth_otp"] = otp
        request.session["auth_email"] = email
        # cache.set('{0}_auth_otp'.format(request.session.session_key), otp, 120)
        # cache.set('{0}_auth_email'.format(request.session.session_key), email, 120)
    
        result = {"successs": True, "message": "otp sent"}
        return render( request , 'VI/Registration-Page/index.html')
    else:
        return redirect('sendOtp')


def login(request):
    username = request.GET.get('email')
    password = request.GET.get('pwd')
    userexistqry =  User.objects.raw(" select id , role_id from user where username = '" + username + "' and password = '" + password + "' ; ")
    for i in userexistqry : 
        print(i.id)
        print(i.role_id)
    print(userexistqry)
    #if user exist - go to search page
    if  userexistqry  :
        for i in userexistqry : 
            request.session['userid'] = i.id
            return redirect('search')
        return render( request , 'search.html' , {'se' : asd })
    else:
        return redirect('home')
    return render(request ,'simpleLogin.html')


def profile_one(request):
    return render(request ,'VI/Profilepage-01/index.html')

def profile_two(request):
    return render(request ,'VI/Profilepage-02/index.html')

def create_profile_one(request):
    fname=request.GET.get('fname')
    country=request.GET.get('country')
    phone=request.GET.get('phone')
    skills=request.GET.get('skills')
    lname=request.GET.get('lname')
    state=request.GET.get('state')
    skype=request.GET.get('skype')
    exp=request.GET.get('exp')
    
    result = Profile.objects.create(
                first_name = fname,
                last_name = lname,
                country_id = country,
                state_id = state,
                mobile_number = phone,
                skype_id = skype,
                skill_id = skills,
                experience = exp,
                user_id = request.session['userid']
            ),

    print(result)
    return render(request ,'VI/Profilepage-02/index.html')

def create_profile_two(request):
    currentPosition = request.GET.get('currentPosition')
    language = request.GET.get('language')
    certifications = request.GET.get('certifications')
    portfolio = request.GET.get('portfolio')
    hrs = request.GET.get('hrs')
    bio = request.GET.get('bio')
    user_id = request.session['userid']

    result = Profile.objects.filter(user_id = user_id).update(
                current_position =currentPosition,
                portfolio_link =portfolio,
                hours_per_week =hrs,
                bio =bio
            )
    print(result)
    return render(request , 'search.html')

def search(request) :
    
    user_id = str(  request.session['userid'] )
    #print(user_id)
    user_type =  User.objects.raw(" select id , role_id from user where id = " + user_id + "  ; ")
     
    for i in user_type : 
        type_user =  i.role_id 
        #print(i.role_id )   

    #we got the user type 

    required_string = "profile.id, profile.first_name ,  profile.last_name , profile.experience , profile.user_id , profile.current_position , state.state , country.country , skill.skills " 
    #tables_used = " profile  , country , state , skill , user ,  filter_details "
    tables_used = " profile  , country , state , skill , user  "
    # condition_string = "profile.country_id = country.id and profile.state_id = state.id and profile.skill_id = skill.id and profile.user_id = user.id  and  filter_details.user_id = profile.user_id  " 
    condition_string = "profile.country_id = country.id and profile.state_id = state.id and profile.skill_id = skill.id and profile.user_id = user.id   " 
    #set user type 
    user_type = int( type_user ) 
    user_type = 1 + (user_type )%2  
    user_type  = str(  user_type )
    condition_string = condition_string  + " and user.role_id =  " + user_type + " " 

    #set the hourly rate 
    hourly_query = ""
    add_on = 0  
    if  request.GET.get('hourlyrate1')  :
        if add_on == 1 : 
            hourly_query = hourly_query + " or " 

        add_on = 1  

        hourly_query = hourly_query + " ( profile.hourly_rate < 5  )  " 
    
    
    if  request.GET.get('hourlyrate2')  :
        if add_on == 1 : 
            hourly_query = hourly_query + " or " 

        add_on = 1  

        hourly_query = hourly_query + " ( profile.hourly_rate  >=  5 and profile.hourly_rate  < 10  )  " 
    
    
    if  request.GET.get('hourlyrate3')  :
        if add_on == 1 : 
            hourly_query = hourly_query + " or " 

        add_on = 1  

        hourly_query = hourly_query + " ( profile.hourly_rate >= 10 and profile.hourly_rate  < 100    )  " 
    
    
    if  request.GET.get('hourlyrate4')  :
        if add_on == 1 : 
            hourly_query = hourly_query + " or " 

        add_on = 1  

        hourly_query = hourly_query + " ( profile.hourly_rate >= 100  )  " 
    
    


    if len (hourly_query ) : 
        hourly_query =  " and  ( " + hourly_query + " ) " 
    

    #now add the value of the location

    if request.GET.get('location') : 
        condition_string = condition_string + "  and  " + "  profile.location = " + " '" + request.GET.get('location') + "' " 


    #now add the value of the language

    if request.GET.get('language') : 
        condition_string = condition_string + "  and  " + "  profile.language = " + " '" + request.GET.get('language') + "' " 

    #now add the value of the talent 


    talent_query = ""
    add_on = 0  
    if  request.GET.get('Beginner')  :
        if add_on == 1 : 
            talent_query = talent_query + " or " 

        add_on = 1  

        talent_query = talent_query + " ( profile.talent = 'Beginner' )  " 
    
    if  request.GET.get('Intermediate')  :
        if add_on == 1 : 
            talent_query = talent_query + " or " 

        add_on = 1  

        talent_query = talent_query + " ( profile.talent = 'Intermediate' )  " 
    
    if  request.GET.get('Expert')  :
        if add_on == 1 : 
            talent_query = talent_query + " or " 

        add_on = 1  

        talent_query = talent_query + " ( profile.talent = 'Expert' )  " 
    if  request.GET.get('Super Expert')  :
        if add_on == 1 : 
            talent_query = talent_query + " or " 

        add_on = 1  

        talent_query = talent_query + " ( profile.talent = 'Super Expert' )  " 
    
    


    if len (talent_query ) : 
        talent_query =  " and  ( " + talent_query + " ) " 
    


    # add the search string 
    fname = request.GET.get('fname')
    if fname is None : 
        fname = '' 


    search_string = " and (  profile.first_name  REGEXP '" + "^" + fname + "' or  profile.last_name REGEXP '^" + fname +"' "  +   " or LOWER( skill.skills ) REGEXP LOWER ( '" + fname + "' )" + ")" 

    # add the skill string 




    if fname == '' :
        search_string = ""
    print(condition_string)

    cla = request.GET.get('section') 
    if cla != None :
        search_string = search_string   + " and skill.skill_description = '" + cla + "'"


    query_string = " select  " + required_string + "  from  "  +  tables_used + " where  "  + condition_string + hourly_query  + talent_query + search_string + " ; "
    print(query_string)
    bsd =  Profile.objects.raw( query_string )

    pgno = 1
    try : 
        pgno = int(request.GET.get('page') )
    except :
        pgno  = 1 
    data = Paginator(bsd  , 2 )
    asd = data.page(pgno)


    if asd != None : 
        for i in asd : 
            if i.skills == None : 
                i.skill = {}
                continue  
            i.skill =  json.loads( i.skills )
        #print( type (  json.loads( i.skills ) ) )
    #select profile.id, first_name ,  last_name , experience , profile.user_id , current_position , state , country , skills   from profile  , country , state , skill , filter_details  where profile.country_id = country.id and profile.state_id = state.id and profile.skill_id = skill.id and profile.user_id = filter_details.user_id and filter_details.language like "E%";
    
    #paginator tesst 



    locations = Country.objects.all()
    language_list_ht =  language_list.objects.all()


    #inputs


    inputs = {}
    try : 
        inputs['search_bar']   =  fname
    except : 
        inputs['search_bar'] =''
        
    try : 
        if request.GET.get('hourlyrate1') :
            inputs['hourlyrate1']   =  1 
        else : 
            inputs['hourlyrate1'] = 0 
    except : 
        inputs['hourlyrate1'] = 0
    try : 
        if request.GET.get('hourlyrate2') :
            inputs['hourlyrate2']   =  1 
        else : 
            inputs['hourlyrate2'] = 0 
    except : 
        inputs['hourlyrate2'] = 0
    try : 
        if request.GET.get('hourlyrate3') :
            inputs['hourlyrate3']   =  1 
        else : 
            inputs['hourlyrate3'] = 0 
    except : 
        inputs['hourlyrate3'] = 0
    try : 
        if request.GET.get('hourlyrate4') :
            inputs['hourlyrate4']   =  1 
        else : 
            inputs['hourlyrate4'] = 0 
    except : 
        inputs['hourlyrate4'] = 0
    try : 
        if request.GET.get('Beginner') :
            inputs['Beginner']   =  1 
        else : 
            inputs['Beginner'] = 0 
    except : 
        inputs['Beginner'] = 0
    try : 
        if request.GET.get('Intermediate') :
            inputs['Intermediate']   =  1 
        else : 
            inputs['Intermediate'] = 0 
    except : 
        inputs['Intermediate'] = 0
    try : 
        if request.GET.get('Expert') :
            inputs['Expert']   =  1 
        else : 
            inputs['Expert'] = 0 
    except : 
        inputs['Expert'] = 0
    try : 
        if request.GET.get('Super Expert') :
            inputs['Super_Expert']   =  1 
        else : 
            inputs['Super_Expert'] = 0 
    except : 
        inputs['Super_Expert'] = 0
    try : 
         inputs['location'] =  request.GET.get('location')
    except : 
        inputs['location'] =''
    try : 
        inputs['language'] = request.GET.get('language')
    except : 
        inputs['language'] =''
    if inputs['language'] == None : 
        inputs['language'] = '' 
    if inputs['location'] == None : 
        inputs['location'] = ''
    
    try :
        inputs['section'] = request.GET.get('section')
    except :
        inputs['section'] =None
    try : 
        inputs['nextpage'] = int(request.GET.get('page') ) +1

    except :
        inputs['nextpage'] = 2
    
    if asd.has_next() == False  :
        inputs['nextpage'] = None 
    try : 
        inputs['prepage'] = int(request.GET.get('page') ) - 1
         
    except :
        inputs['prepage'] = None
        
    if asd.has_previous() == False  : 
        inputs['prepage'] = None 

    return render( request , 'index.html' , {'inputs':inputs , 'se' : asd , 'type' : type_user , 'locations' : locations , 'language_list_ht' : language_list_ht ,'pre' :   hourly_query  + talent_query + search_string    })

