import mysql.connector
import fastapi
from fastapi import FastAPI,Request,Form,requests,Response,Header,Cookie
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,RedirectResponse
from typing import Annotated
import bcrypt
import app.ath as ath
import app.db as db
import time
import math
import datetime

app= FastAPI()
templates=Jinja2Templates(directory='app/templates')
mydb = mysql.connector.connect(
    host="parking-project-database.mysql.database.azure.com",
    user="Zebi",
    password="18082001Rak.",
    db="parking",
    tls_versions=['TLSv1.1', 'TLSv1.2']
)
cur=mydb.cursor(buffered=True)
fmt="%Y-%m-%d-%H-%M"
#DIC={'AP-NL': {'state': 'Andhra Pradesh', 'city': 'Nellore'}, 'AP-TP': {'state': 'Andhra Pradesh', 'city': 'Tirupati'}, 'AP-KL': {'state': 'Andhra Pradesh', 'city': 'Kurnool'}, 'AP-AN': {'state': 'Andhra Pradesh', 'city': 'Anantapur'}, 'AP-VP': {'state': 'Andhra Pradesh', 'city': 'Visakhapatnam'}, 'AR-SP': {'state': 'Arunachal Pradesh', 'city': 'Seppa'}, 'AR-WK': {'state': 'Arunachal Pradesh', 'city': 'Wakro'}, 'AR-RP': {'state': 'Arunachal Pradesh', 'city': 'Rupa'}, 'AR-ZT': {'state': 'Arunachal Pradesh', 'city': 'Zemithang'}, 'AR-BM': {'state': 'Arunachal Pradesh', 'city': 'Bameng'}, 'AS-GW': {'state': 'Assam', 'city': 'Guwahati'}, 'AS-SL': {'state': 'Assam', 'city': 'Silchar'}, 'AS-DB': {'state': 'Assam', 'city': 'Dibrugarh'}, 'AS-JR': {'state': 'Assam', 'city': 'Jorhat'}, 'AS-NG': {'state': 'Assam', 'city': 'Nagaon'}, 'BR-PT': {'state': 'Bihar', 'city': 'Patna'}, 'BR-GY': {'state': 'Bihar', 'city': 'Gaya'}, 'BR-BS': {'state': 'Bihar', 'city': 'Bihar Sharif'}, 'BR-BG': {'state': 'Bihar', 'city': 'Bhagalpur'}, 'BR-MF': {'state': 'Bihar', 'city': 'Muzaffarpur'}, 'CG-RP': {'state': 'Chattisgarh', 'city': 'Raipur'}, 'CG-RG': {'state': 'Chattisgarh', 'city': 'Raigarh'}, 'CG-BL': {'state': 'Chattisgarh', 'city': 'Bhilai'}, 'CG-KB': {'state': 'Chattisgarh', 'city': 'Korba'}, 'CG-AB': {'state': 'Chattisgarh', 'city': 'Ambikapur'}, 'GA-PJ': {'state': 'Goa', 'city': 'Panaji'}, 'GA-MP': {'state': 'Goa', 'city': 'Mapusa'}, 'GA-PN': {'state': 'Goa', 'city': 'Ponda'}, 'GA-MR': {'state': 'Goa', 'city': 'Mormugao'}, 'GA-PR': {'state': 'Goa', 'city': 'Pernem'}, 'GJ-JN': {'state': 'Gujarat', 'city': 'Jamnagar'}, 'GJ-RK': {'state': 'Gujarat', 'city': 'Rajkot'}, 'GJ-SR': {'state': 'Gujarat', 'city': 'Surat'}, 'GJ-VD': {'state': 'Gujarat', 'city': 'Vadodara'}, 'GJ-AD': {'state': 'Gujarat', 'city': 'Ahmedabad'}, 'HR-AB': {'state': 'Haryana', 'city': 'Ambala'}, 'HR-PN': {'state': 'Haryana', 'city': 'Panipat'}, 'HR-FD': {'state': 'Haryana', 'city': 'Faridabad'}, 'HR-KN': {'state': 'Haryana', 'city': 'Karnal'}, 'HR-GG': {'state': 'Haryana', 'city': 'Gurugram'}, 'HP-CM': {'state': 'Himachal Pradesh', 'city': 'Chamba'}, 'HP-KL': {'state': 'Himachal Pradesh', 'city': 'Kullu'}, 'HP-SL': {'state': 'Himachal Pradesh', 'city': 'Solan'}, 'HP-MN': {'state': 'Himachal Pradesh', 'city': 'Manali'}, 'HP-SM': {'state': 'Himachal Pradesh', 'city': 'Shimla'}, 'JH-DG': {'state': 'Jharkhand', 'city': 'Deoghar'}, 'JH-BK': {'state': 'Jharkhand', 'city': 'Bokaro'}, 'JH-RN': {'state': 'Jharkhand', 'city': 'Ranchi'}, 'JH-DN': {'state': 'Jharkhand', 'city': 'Dhanbad'}, 'JH-JM': {'state': 'Jharkhand', 'city': 'Jamshedpur'}, 'KA-KB': {'state': 'Karnataka', 'city': 'Kalaburagi'}, 'KA-SM': {'state': 'Karnataka', 'city': 'Shivamogga'}, 'KA-VJ': {'state': 'Karnataka', 'city': 'Vijaypura'}, 'KA-MN': {'state': 'Karnataka', 'city': 'Mangaluru'}, 'KA-BG': {'state': 'Karnataka', 'city': 'Bengaluru'}, 'KL-KM': {'state': 'Kerala', 'city': 'Kollam'}, 'KL-TS': {'state': 'Kerala', 'city': 'Thrissur'}, 'KL-KC': {'state': 'Kerala', 'city': 'Kochi'}, 'KL-TV': {'state': 'Kerala', 'city': 'Thiruvanantpuram'}, 'KL-KZ': {'state': 'Kerala', 'city': 'Kozhikode'}, 'MP-UJ': {'state': 'Madhya Pradesh', 'city': 'Ujjain'}, 'MP-GW': {'state': 'Madhya Pradesh', 'city': 'Gwalior'}, 'MP-JB': {'state': 'Madhya Pradesh', 'city': 'Jabalpur'}, 'MP-BH': {'state': 'Madhya Pradesh', 'city': 'Bhopal'}, 'MP-IN': {'state': 'Madhya Pradesh', 'city': 'Indore'}, 'MH-ND': {'state': 'Maharashtra', 'city': 'Nanded'}, 'MH-SL': {'state': 'Maharashtra', 'city': 'Solapur'}, 'MH-AG': {'state': 'Maharashtra', 'city': 'Aurangabad'}, 'MH-NS': {'state': 'Maharashtra', 'city': 'Nashik'}, 'MH-MB': {'state': 'Maharashtra', 'city': 'Mumbai'}, 'MN-MR': {'state': 'Manipur', 'city': 'Moirang'}, 'MN-TB': {'state': 'Manipur', 'city': 'Thoubal'}, 'MN-UN': {'state': 'Manipur', 'city': 'Ukhrul North'}, 'MN-UK': {'state': 'Manipur', 'city': 'Ukhrul'}, 'MN-SG': {'state': 'Manipur', 'city': 'Saitu-Gamphazol'}, 'ML-MS': {'state': 'Meghalaya', 'city': 'Mawsmai'}, 'ML-SL': {'state': 'Meghalaya', 'city': 'Shillong'}, 'ML-PN': {'state': 'Meghalaya', 'city': 'Pynursla'}, 'ML-MW': {'state': 'Meghalaya', 'city': 'Mawphlang'}, 'ML-SB': {'state': 'Meghalaya', 'city': 'Shella Bholaganj'}, 'MZ-LN': {'state': 'Mizoram', 'city': 'Lunglei'}, 'MZ-LW': {'state': 'Mizoram', 'city': 'Lawngtlai'}, 'MZ-KL': {'state': 'Mizoram', 'city': 'Kolasib'}, 'MZ-CM': {'state': 'Mizoram', 'city': 'Champhai'}, 'MZ-AZ': {'state': 'Mizoram', 'city': 'Aizawl'}, 'NL-MK': {'state': 'Nagaland', 'city': 'Mokokchung'}, 'NL-LN': {'state': 'Nagaland', 'city': 'Longleng'}, 'NL-KH': {'state': 'Nagaland', 'city': 'Kohima'}, 'NL-KP': {'state': 'Nagaland', 'city': 'Kiphire'}, 'NL-DM': {'state': 'Nagaland', 'city': 'Dimapur'}, 'OR-BM': {'state': 'Odisha', 'city': 'Brahmapur'}, 'OR-RK': {'state': 'Odisha', 'city': 'Rourkela'}, 'OR-CT': {'state': 'Odisha', 'city': 'Cuttack'}, 'OR-BN': {'state': 'Odisha', 'city': 'Bhubaneswar'}, 'OR-BD': {'state': 'Odisha', 'city': 'Bhadrak'}, 'PB-LD': {'state': 'Punjab', 'city': 'Ludhiana'}, 'PB-BT': {'state': 'Punjab', 'city': 'Bathinda'}, 'PB-AM': {'state': 'Punjab', 'city': 'Amritsar'}, 'PB-KP': {'state': 'Punjab', 'city': 'Kapurthala'}, 'PB-HS': {'state': 'Punjab', 'city': 'Hoshiarpur'}, 'RJ-JS': {'state': 'Rajasthan', 'city': 'Jaisalmer'}, 'RJ-BK': {'state': 'Rajasthan', 'city': 'Bikaner'}, 'RJ-JD': {'state': 'Rajasthan', 'city': 'Jodhpur'}, 'RJ-UD': {'state': 'Rajasthan', 'city': 'Udaipur'}, 'JP': {'state': 'Rajasthan', 'city': 'Jaipur'}, 'SK-GR': {'state': 'Sikkim', 'city': 'Gor'}, 'SK-SR': {'state': 'Sikkim', 'city': 'Soreng'}, 'SK-GT': {'state': 'Sikkim', 'city': 'Gangtok'}, 'SK-GL': {'state': 'Sikkim', 'city': 'Gyalshing'}, 'SK-WS': {'state': 'Sikkim', 'city': 'West Sikkim'}, 'TN-TJ': {'state': 'Tamil Nadu', 'city': 'Thanjavur'}, 'TN-MD': {'state': 'Tamil Nadu', 'city': 'Madurai'}, 'TN-CM': {'state': 'Tamil Nadu', 'city': 'Coimbatore'}, 'TN-CN': {'state': 'Tamil Nadu', 'city': 'Chennai'}, 'TN-TP': {'state': 'Tamil Nadu', 'city': 'Tiruchirappalli'}, 'TS-NZ': {'state': 'Telangana', 'city': 'Nizamabad'}, 'TS-MD': {'state': 'Telangana', 'city': 'Medak'}, 'TS-KR': {'state': 'Telangana', 'city': 'Karimnagar'}, 'TS-WR': {'state': 'Telangana', 'city': 'Warangal'}, 'TS-HD': {'state': 'Telangana', 'city': 'Hyderabad'}, 'TR-BS': {'state': 'Tripura', 'city': 'Bishalgarh'}, 'TR-KS': {'state': 'Tripura', 'city': 'Kailashahar'}, 'TR-UD': {'state': 'Tripura', 'city': 'Udaipur'}, 'TR-DM': {'state': 'Tripura', 'city': 'Dharmanagar'}, 'TR-AG': {'state': 'Tripura', 'city': 'Agartala'}, 'UK-RD': {'state': 'Uttarakhand', 'city': 'Rudrapur'}, 'UK-HL': {'state': 'Uttarakhand', 'city': 'Haldwani'}, 'UK-RK': {'state': 'Uttarakhand', 'city': 'Roorkee'}, 'UK-HD': {'state': 'Uttarakhand', 'city': 'Haridwar'}, 'UK-DD': {'state': 'Uttarakhand', 'city': 'Dehradun'}, 'UP-GZ': {'state': 'Uttar Pradesh', 'city': 'Ghaziabad'}, 'UP-VR': {'state': 'Uttar Pradesh', 'city': 'Varanasi'}, 'UP-KN': {'state': 'Uttar Pradesh', 'city': 'Kanpur'}, 'UP-PG': {'state': 'Uttar Pradesh', 'city': 'Prayagraj'}, 'UP-LK': {'state': 'Uttar Pradesh', 'city': 'Lucknow'}, 'WB-JD': {'state': 'West Bengal', 'city': 'Jhalda'}, 'WB-GB': {'state': 'West Bengal', 'city': 'Gorubathan'}, 'WB-KP': {'state': 'West Bengal', 'city': 'Kalimpong'}, 'WB-KL': {'state': 'West Bengal', 'city': 'Kolkata'}, 'WB-RB': {'state': 'West Bengal', 'city': 'Rimbik'}}

@app.get("/")
async def welcome(request:Request):
    return templates.TemplateResponse('index.html',{"request":request, "avail":db.avail()})

# @app.get("/login",response_class=HTMLResponse)
# async def login(request:Request):
#     return templates.TemplateResponse("login.html", {"request":request, "error":[]})

@app.get("/login",response_class=HTMLResponse)
async def login(request:Request):
    token=request.cookies.get("authorization")
    u = ath.is_ath(token)
    print(u)
    print(token)
    if (u == ath.e) or not(token==u['token']):
        return templates.TemplateResponse("login.html", {"request":request, "error":[]})
    else:
        tm = datetime.datetime.now() + datetime.timedelta(minutes=10)
        exp= datetime.datetime.strptime(ath.dec(token)["expiry"], fmt)
        avail = db.avail()
        if tm>exp:
            tkn = ath.crt(u['email'])
            print(tkn)
            db.updtoken(u['email'], tkn)
            response.set_cookie(key="authorization", value=tkn)
        if u.get("isadmin")==1:
            return templates.TemplateResponse("hmpgadm.html", {"request":request, "avail":avail})
        else:
            return templates.TemplateResponse("hmpg.html", {"request":request, "avail":avail, "wallet":u.get("wallet")})
    
    

@app.post("/login")
async def login(request: Request,response: Response, username:str=Form(), password:str=Form()):
    errors=[]
    email = username
    password = password.encode("UTF-8")
    u=db.getuser(email)
    cur.execute(f"select email,pswd from users where email = '{email}'")
    t=[c for c in cur.fetchall()]
    if u=={}:
        errors.append("Email not Found")
        return templates.TemplateResponse("login.html", {"request":request, "error":["Email not Found"]})
    passed=bcrypt.checkpw(password, u["pswd"])
    if not passed:
        errors.append("Wrong Password")
        return templates.TemplateResponse("login.html", {"request":request, "error":["Wrong Password"]})
    token = ath.crt(email)
    db.updtoken(email, token)
    resp = RedirectResponse("/hmpg")
    resp.set_cookie(key="authorization", value=token)
    return resp

@app.get("/register", response_class=HTMLResponse)
async def register(request:Request):
    return templates.TemplateResponse("register.html", {"request":request, "error":[]})


@app.post("/register")
async def register(request: Request, name:str=Form(), username:str=Form(), password:str=Form(), isadmin:str=Form()):
    errors=[] 
    if '@' not in username:
        errors.append("E-mail not valid.")
    u=db.getuser(username)
    if not(u=={}):
        errors=["E-mail is already in use."]
    if len(password)<6:
        errors.append("Password is too small.(Needs to be bigger than 6 characters)")
    if not(errors == []):
        return templates.TemplateResponse("register.html", {"request":request, "error":errors})
    db.adduser(name, username, password, isadmin)
    return templates.TemplateResponse("login.html", {"request":request, "error":["Registered, Please Login"]})

@app.get("/hmpg")
async def hmpg(request: Request, response: Response):
    token=request.cookies.get("authorization")
    u = ath.is_ath(token)
    print(u)
    print(token)
    if (u == ath.e) or not(token==u['token']):
        return RedirectResponse("/login")
    else:
        tm = datetime.datetime.now() + datetime.timedelta(minutes=10)
        exp= datetime.datetime.strptime(ath.dec(token)["expiry"], fmt)
        avail = db.avail()
        if tm>exp:
            tkn = ath.crt(u['email'])
            print(tkn)
            db.updtoken(u['email'], tkn)
            response.set_cookie(key="authorization", value=tkn)
        if u.get("isadmin")==1:
            return templates.TemplateResponse("hmpgadm.html", {"request":request, "avail":avail})
        else:
            return templates.TemplateResponse("hmpg.html", {"request":request, "avail":avail, "wallet":u.get("wallet")})

@app.post("/hmpg", response_class=HTMLResponse)
async def hmpg(request: Request, response: Response):
    token=request.cookies.get("authorization")
    u = ath.is_ath(token)
    print(u)
    print(token)
    if (u == ath.e) or not(token==u['token']):
        return RedirectResponse("/login")
    else:
        tm = datetime.datetime.now() + datetime.timedelta(minutes=10)
        exp= datetime.datetime.strptime(ath.dec(token)["expiry"], fmt)
        avail = db.avail()
        if tm>exp:
            tkn = ath.crt(u['email'])
            print(tkn)
            db.updtoken(u['email'], tkn)
            response.set_cookie(key="authorization", value=tkn)
        if u.get("isadmin")==1:
            return templates.TemplateResponse("hmpgadm.html", {"request":request, "avail":avail})
        else:
            return templates.TemplateResponse("hmpg.html", {"request":request, "avail":avail, "wallet":u.get("wallet")})

@app.get("/refillwallet")
async def refillwallet(request: Request):
    token=request.cookies.get("authorization")
    u = ath.is_ath(token)
    if (u == ath.e) or not(token==u.get("token")):
        return RedirectResponse("/login")
    else:
        return templates.TemplateResponse("refillwallet.html", {"request":request})

@app.post("/refillwallet")
async def refillwallet(request: Request,password:str=Form(),amount:str=Form()):
    token=request.cookies.get("authorization")
    u = ath.is_ath(token)
    if (u == ath.e) or not(token==u.get("token")):
        return RedirectResponse("/login")
    else:
        pswd=password.encode("UTF-8")
        passed=bcrypt.checkpw(pswd, u.get("pswd"))
        if passed:
            db.add_to_wallet(u, amount)
        return RedirectResponse("/hmpg")


@app.get("/logout")
async def logout(request: Request,response: Response):
    token=request.cookies.get("authorization")
    u = ath.is_ath(token)
    if (u == ath.e) or not(token==u.get("token")):
        return RedirectResponse("/login")
    else:
        db.updtoken(u['email'], "none")
        resp = RedirectResponse("/login")
        resp.set_cookie("authorization",value="none")
        return resp

@app.get("/book")
async def hmpg(request: Request):
    token=request.cookies.get("authorization")
    u = ath.is_ath(token)
    if (u == ath.e) or not(token==u.get("token")):
        return RedirectResponse("/login")
    else:
        return templates.TemplateResponse("book.html", {"request":request, "rows":db.get_booking_list()})

@app.post("/book")
async def hmpg(request: Request, state:str=Form(default="")):
    token=request.cookies.get("authorization")
    u = ath.is_ath(token)
    if (u == ath.e) and not(token==u.get("token")):
        return RedirectResponse("/login")
    else:
        return templates.TemplateResponse("book.html", {"request":request, "rows":db.get_booking_list_by_state(state)})
    
@app.get("/book/{code}")
async def bookaspot(request:Request, code:str ):
    token=request.cookies.get("authorization")
    u = ath.is_ath(token)
    if (u == ath.e) or not(token==u.get("token")):
        return RedirectResponse("/login")
    else:
        s=db.get_spot(code)
        if s.get("available")<=0 and u.get("wallet")>0:
            pass
        else:
            db.book_spot(u, s)
        return RedirectResponse("/book")

@app.get("/rel")
async def release(request:Request):
    token=request.cookies.get("authorization")
    u = ath.is_ath(token)
    if (u == ath.e) or not(token==u.get("token")):
        return RedirectResponse("/login")
    else:
        return templates.TemplateResponse("release.html", {"request":request, "rows":db.get_release_list(u)})

@app.get("/rel/{code}/{booked}")
async def releasesing(request:Request,code:str,booked:str):
    token=request.cookies.get("authorization")
    u = ath.is_ath(token)
    if (u == ath.e) or not(token==u.get("token")):
        return RedirectResponse("/login")
    else:
        db.release_spot(u, code, booked)
        return RedirectResponse("/rel")

@app.get("/history")
async def histry(request:Request):
    token=request.cookies.get("authorization")
    u = ath.is_ath(token)
    if (u == ath.e) or not(token==u.get("token")):
        return RedirectResponse("/login")
    else:
        if u.get("isadmin")==1:
            return templates.TemplateResponse("histryadmin.html", {"request":request, "rows":db.get_history(u)})
        else:
            return templates.TemplateResponse("histry.html", {"request":request, "rows":db.get_history(u)})

@app.get("/history/{userid}")
async def histryadmn(request:Request,userid:int):
    token=request.cookies.get("authorization")
    u = ath.is_ath(token)
    if (u == ath.e) or not(token==u.get("token")) or not(u.get("isadmin")==1):
        return RedirectResponse("/login")
    else:
        return templates.TemplateResponse("historyuser.html", {"request":request, "rows":db.get_user_history(userid)})

@app.get("/bookedadmin")
async def bookedadmn(request:Request):
    token=request.cookies.get("authorization")
    u = ath.is_ath(token)
    if (u == ath.e) or not(token==u.get("token")) or not(u.get("isadmin")==1):
        return RedirectResponse("/login")
    else:
        return templates.TemplateResponse("bookedadmin.html", {"request":request, "rows":db.get_booking_history()})

@app.get("/revstate")
async def revstate(request:Request):
    token=request.cookies.get("authorization")
    u = ath.is_ath(token)
    if (u == ath.e) or not(token==u.get("token")) or not(u.get("isadmin")==1):
        return RedirectResponse("/login")
    else:
        return templates.TemplateResponse("revstate.html", {"request":request, "rows":db.get_revenue_statewise()})

@app.get("/revcities")
async def revcities(request:Request):
    token=request.cookies.get("authorization")
    u = ath.is_ath(token)
    if (u == ath.e) or not(token==u.get("token")) or not(u.get("isadmin")==1):
        return RedirectResponse("/login")
    else:
        return templates.TemplateResponse("revcities.html", {"request":request, "rows":db.get_revenue_citywise()})

@app.get("/revcity/{state}")
async def revcities(request:Request,state:str):
    token=request.cookies.get("authorization")
    u = ath.is_ath(token)
    if (u == ath.e) or not(token==u.get("token")) or not(u.get("isadmin")==1):
        return RedirectResponse("/login")
    else:
        return templates.TemplateResponse("revcity.html", {"request":request,"state":state, "rows":db.get_revenue_for_state(state)})
