import mysql.connector
import bcrypt
import datetime
import math
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from sqlalchemy.ext.automap import automap_base

engine=sqlalchemy.create_engine('mysql+mysqlconnector://Zebi:18082001Rak.@parking-project-database.mysql.database.azure.com/parking',echo=True)
session = sessionmaker(bind=engine)
dic={'AP-NL': {'state': 'Andhra Pradesh', 'city': 'Nellore'}, 'AP-TP': {'state': 'Andhra Pradesh', 'city': 'Tirupati'}, 'AP-KL': {'state': 'Andhra Pradesh', 'city': 'Kurnool'}, 'AP-AN': {'state': 'Andhra Pradesh', 'city': 'Anantapur'}, 'AP-VP': {'state': 'Andhra Pradesh', 'city': 'Visakhapatnam'}, 'AR-SP': {'state': 'Arunachal Pradesh', 'city': 'Seppa'}, 'AR-WK': {'state': 'Arunachal Pradesh', 'city': 'Wakro'}, 'AR-RP': {'state': 'Arunachal Pradesh', 'city': 'Rupa'}, 'AR-ZT': {'state': 'Arunachal Pradesh', 'city': 'Zemithang'}, 'AR-BM': {'state': 'Arunachal Pradesh', 'city': 'Bameng'}, 'AS-GW': {'state': 'Assam', 'city': 'Guwahati'}, 'AS-SL': {'state': 'Assam', 'city': 'Silchar'}, 'AS-DB': {'state': 'Assam', 'city': 'Dibrugarh'}, 'AS-JR': {'state': 'Assam', 'city': 'Jorhat'}, 'AS-NG': {'state': 'Assam', 'city': 'Nagaon'}, 'BR-PT': {'state': 'Bihar', 'city': 'Patna'}, 'BR-GY': {'state': 'Bihar', 'city': 'Gaya'}, 'BR-BS': {'state': 'Bihar', 'city': 'Bihar Sharif'}, 'BR-BG': {'state': 'Bihar', 'city': 'Bhagalpur'}, 'BR-MF': {'state': 'Bihar', 'city': 'Muzaffarpur'}, 'CG-RP': {'state': 'Chattisgarh', 'city': 'Raipur'}, 'CG-RG': {'state': 'Chattisgarh', 'city': 'Raigarh'}, 'CG-BL': {'state': 'Chattisgarh', 'city': 'Bhilai'}, 'CG-KB': {'state': 'Chattisgarh', 'city': 'Korba'}, 'CG-AB': {'state': 'Chattisgarh', 'city': 'Ambikapur'}, 'GA-PJ': {'state': 'Goa', 'city': 'Panaji'}, 'GA-MP': {'state': 'Goa', 'city': 'Mapusa'}, 'GA-PN': {'state': 'Goa', 'city': 'Ponda'}, 'GA-MR': {'state': 'Goa', 'city': 'Mormugao'}, 'GA-PR': {'state': 'Goa', 'city': 'Pernem'}, 'GJ-JN': {'state': 'Gujarat', 'city': 'Jamnagar'}, 'GJ-RK': {'state': 'Gujarat', 'city': 'Rajkot'}, 'GJ-SR': {'state': 'Gujarat', 'city': 'Surat'}, 'GJ-VD': {'state': 'Gujarat', 'city': 'Vadodara'}, 'GJ-AD': {'state': 'Gujarat', 'city': 'Ahmedabad'}, 'HR-AB': {'state': 'Haryana', 'city': 'Ambala'}, 'HR-PN': {'state': 'Haryana', 'city': 'Panipat'}, 'HR-FD': {'state': 'Haryana', 'city': 'Faridabad'}, 'HR-KN': {'state': 'Haryana', 'city': 'Karnal'}, 'HR-GG': {'state': 'Haryana', 'city': 'Gurugram'}, 'HP-CM': {'state': 'Himachal Pradesh', 'city': 'Chamba'}, 'HP-KL': {'state': 'Himachal Pradesh', 'city': 'Kullu'}, 'HP-SL': {'state': 'Himachal Pradesh', 'city': 'Solan'}, 'HP-MN': {'state': 'Himachal Pradesh', 'city': 'Manali'}, 'HP-SM': {'state': 'Himachal Pradesh', 'city': 'Shimla'}, 'JH-DG': {'state': 'Jharkhand', 'city': 'Deoghar'}, 'JH-BK': {'state': 'Jharkhand', 'city': 'Bokaro'}, 'JH-RN': {'state': 'Jharkhand', 'city': 'Ranchi'}, 'JH-DN': {'state': 'Jharkhand', 'city': 'Dhanbad'}, 'JH-JM': {'state': 'Jharkhand', 'city': 'Jamshedpur'}, 'KA-KB': {'state': 'Karnataka', 'city': 'Kalaburagi'}, 'KA-SM': {'state': 'Karnataka', 'city': 'Shivamogga'}, 'KA-VJ': {'state': 'Karnataka', 'city': 'Vijaypura'}, 'KA-MN': {'state': 'Karnataka', 'city': 'Mangaluru'}, 'KA-BG': {'state': 'Karnataka', 'city': 'Bengaluru'}, 'KL-KM': {'state': 'Kerala', 'city': 'Kollam'}, 'KL-TS': {'state': 'Kerala', 'city': 'Thrissur'}, 'KL-KC': {'state': 'Kerala', 'city': 'Kochi'}, 'KL-TV': {'state': 'Kerala', 'city': 'Thiruvanantpuram'}, 'KL-KZ': {'state': 'Kerala', 'city': 'Kozhikode'}, 'MP-UJ': {'state': 'Madhya Pradesh', 'city': 'Ujjain'}, 'MP-GW': {'state': 'Madhya Pradesh', 'city': 'Gwalior'}, 'MP-JB': {'state': 'Madhya Pradesh', 'city': 'Jabalpur'}, 'MP-BH': {'state': 'Madhya Pradesh', 'city': 'Bhopal'}, 'MP-IN': {'state': 'Madhya Pradesh', 'city': 'Indore'}, 'MH-ND': {'state': 'Maharashtra', 'city': 'Nanded'}, 'MH-SL': {'state': 'Maharashtra', 'city': 'Solapur'}, 'MH-AG': {'state': 'Maharashtra', 'city': 'Aurangabad'}, 'MH-NS': {'state': 'Maharashtra', 'city': 'Nashik'}, 'MH-MB': {'state': 'Maharashtra', 'city': 'Mumbai'}, 'MN-MR': {'state': 'Manipur', 'city': 'Moirang'}, 'MN-TB': {'state': 'Manipur', 'city': 'Thoubal'}, 'MN-UN': {'state': 'Manipur', 'city': 'Ukhrul North'}, 'MN-UK': {'state': 'Manipur', 'city': 'Ukhrul'}, 'MN-SG': {'state': 'Manipur', 'city': 'Saitu-Gamphazol'}, 'ML-MS': {'state': 'Meghalaya', 'city': 'Mawsmai'}, 'ML-SL': {'state': 'Meghalaya', 'city': 'Shillong'}, 'ML-PN': {'state': 'Meghalaya', 'city': 'Pynursla'}, 'ML-MW': {'state': 'Meghalaya', 'city': 'Mawphlang'}, 'ML-SB': {'state': 'Meghalaya', 'city': 'Shella Bholaganj'}, 'MZ-LN': {'state': 'Mizoram', 'city': 'Lunglei'}, 'MZ-LW': {'state': 'Mizoram', 'city': 'Lawngtlai'}, 'MZ-KL': {'state': 'Mizoram', 'city': 'Kolasib'}, 'MZ-CM': {'state': 'Mizoram', 'city': 'Champhai'}, 'MZ-AZ': {'state': 'Mizoram', 'city': 'Aizawl'}, 'NL-MK': {'state': 'Nagaland', 'city': 'Mokokchung'}, 'NL-LN': {'state': 'Nagaland', 'city': 'Longleng'}, 'NL-KH': {'state': 'Nagaland', 'city': 'Kohima'}, 'NL-KP': {'state': 'Nagaland', 'city': 'Kiphire'}, 'NL-DM': {'state': 'Nagaland', 'city': 'Dimapur'}, 'OR-BM': {'state': 'Odisha', 'city': 'Brahmapur'}, 'OR-RK': {'state': 'Odisha', 'city': 'Rourkela'}, 'OR-CT': {'state': 'Odisha', 'city': 'Cuttack'}, 'OR-BN': {'state': 'Odisha', 'city': 'Bhubaneswar'}, 'OR-BD': {'state': 'Odisha', 'city': 'Bhadrak'}, 'PB-LD': {'state': 'Punjab', 'city': 'Ludhiana'}, 'PB-BT': {'state': 'Punjab', 'city': 'Bathinda'}, 'PB-AM': {'state': 'Punjab', 'city': 'Amritsar'}, 'PB-KP': {'state': 'Punjab', 'city': 'Kapurthala'}, 'PB-HS': {'state': 'Punjab', 'city': 'Hoshiarpur'}, 'RJ-JS': {'state': 'Rajasthan', 'city': 'Jaisalmer'}, 'RJ-BK': {'state': 'Rajasthan', 'city': 'Bikaner'}, 'RJ-JD': {'state': 'Rajasthan', 'city': 'Jodhpur'}, 'RJ-UD': {'state': 'Rajasthan', 'city': 'Udaipur'}, 'JP': {'state': 'Rajasthan', 'city': 'Jaipur'}, 'SK-GR': {'state': 'Sikkim', 'city': 'Gor'}, 'SK-SR': {'state': 'Sikkim', 'city': 'Soreng'}, 'SK-GT': {'state': 'Sikkim', 'city': 'Gangtok'}, 'SK-GL': {'state': 'Sikkim', 'city': 'Gyalshing'}, 'SK-WS': {'state': 'Sikkim', 'city': 'West Sikkim'}, 'TN-TJ': {'state': 'Tamil Nadu', 'city': 'Thanjavur'}, 'TN-MD': {'state': 'Tamil Nadu', 'city': 'Madurai'}, 'TN-CM': {'state': 'Tamil Nadu', 'city': 'Coimbatore'}, 'TN-CN': {'state': 'Tamil Nadu', 'city': 'Chennai'}, 'TN-TP': {'state': 'Tamil Nadu', 'city': 'Tiruchirappalli'}, 'TS-NZ': {'state': 'Telangana', 'city': 'Nizamabad'}, 'TS-MD': {'state': 'Telangana', 'city': 'Medak'}, 'TS-KR': {'state': 'Telangana', 'city': 'Karimnagar'}, 'TS-WR': {'state': 'Telangana', 'city': 'Warangal'}, 'TS-HD': {'state': 'Telangana', 'city': 'Hyderabad'}, 'TR-BS': {'state': 'Tripura', 'city': 'Bishalgarh'}, 'TR-KS': {'state': 'Tripura', 'city': 'Kailashahar'}, 'TR-UD': {'state': 'Tripura', 'city': 'Udaipur'}, 'TR-DM': {'state': 'Tripura', 'city': 'Dharmanagar'}, 'TR-AG': {'state': 'Tripura', 'city': 'Agartala'}, 'UK-RD': {'state': 'Uttarakhand', 'city': 'Rudrapur'}, 'UK-HL': {'state': 'Uttarakhand', 'city': 'Haldwani'}, 'UK-RK': {'state': 'Uttarakhand', 'city': 'Roorkee'}, 'UK-HD': {'state': 'Uttarakhand', 'city': 'Haridwar'}, 'UK-DD': {'state': 'Uttarakhand', 'city': 'Dehradun'}, 'UP-GZ': {'state': 'Uttar Pradesh', 'city': 'Ghaziabad'}, 'UP-VR': {'state': 'Uttar Pradesh', 'city': 'Varanasi'}, 'UP-KN': {'state': 'Uttar Pradesh', 'city': 'Kanpur'}, 'UP-PG': {'state': 'Uttar Pradesh', 'city': 'Prayagraj'}, 'UP-LK': {'state': 'Uttar Pradesh', 'city': 'Lucknow'}, 'WB-JD': {'state': 'West Bengal', 'city': 'Jhalda'}, 'WB-GB': {'state': 'West Bengal', 'city': 'Gorubathan'}, 'WB-KP': {'state': 'West Bengal', 'city': 'Kalimpong'}, 'WB-KL': {'state': 'West Bengal', 'city': 'Kolkata'}, 'WB-RB': {'state': 'West Bengal', 'city': 'Rimbik'}}

Base = automap_base()
Base.prepare(autoload_with=engine)
Users = Base.classes.users
States = Base.classes.states
History = Base.classes.history
Booked = Base.classes.booked

mydb = mysql.connector.connect(
    host="parking-project-database.mysql.database.azure.com",
    user="Zebi",
    password="18082001Rak.",
    db="parking",
    tls_versions=['TLSv1.1', 'TLSv1.2']
)
cur=mydb.cursor(buffered=True)
fmt="%Y-%m-%d-%H-%M"

def avail():
    with session() as ssn:
        rs=ssn.query(func.sum(States.available)).first()
        return rs[0]

# def avail():
#     cur.execute("select sum(available) from states")
#     return int(cur.fetchone()[0])

def getuser(email:str):
    with session() as ssn:
        u = ssn.query(Users).filter(Users.email==email).first()
        if u is None:
            return {}
        else:
            return vars(u)
            # return {
            #     "userid":u.userid,
            #     "name":u.name,
            #     "email":u.email,
            #     "pswd":u.pswd,
            #     "isadmin":u.isadmin,
            #     "wallet":u.wallet,
            #     "token":u.token
            # }

# def getuser(email:str) -> dict:
#     cur.execute(f"select * from users where email = {email}")
#     t=list(cur.fetchone())
#     if t==[]:
#         return {}
#     else:
#         return {
#             "userid":t[0],
#             "name":t[1],
#             "email":t[2],
#             "pass":t[3],
#             "isadmin":t[4],
#             "wallet":t[5],
#             "token":t[6]
#         }

def updtoken(email:str, token:str):
    with session() as ssn:
        u = ssn.query(Users).filter(Users.email==email).first()
        u.token=token
        ssn.commit()

# def updtoken(email:str, token:str):
#     cur.execute(f"update users set token = '{token}' where email='{email}'")
#     mydb.commit()

def adduser(name,email,password,isadmin):
    pswd=password.encode("utf-8")
    pswd=bcrypt.hashpw(pswd, bcrypt.gensalt())
    pswd=pswd.decode("utf-8")
    with session() as ssn:
        u=Users(
            name=name,
            email=email,
            pswd=pswd,
            isadmin=isadmin,
            wallet=0,
            token='none'
        )
        ssn.add(u)
        ssn.commit()

# def adduser(name,email,password,isadmin):
#     pswd=password.encode("utf-8")
#     pswd=bcrypt.hashpw(pswd, bcrypt.gensalt())
#     pswd=pswd.decode("utf-8")
#     cur.execute(f"Insert into users (name, email, pass, isadmin, wallet, token) values ('{name}','{email}','{pswd}',{int(isadmin)},0,'none')")
#     mydb.commit()

def add_to_wallet(u,amount):
    with session() as ssn:
        u = ssn.query(Users).filter(Users.userid == u.get("userid")).first()
        u.wallet += amount
        ssn.commit()

# def add_to_wallet(u:dict, amount:int):
#     cur.execute(f"update users set wallet=wallet+{amount} where email='{u.get('email')}'")
#     mydb.commit()

# def clear_token(u:dict):
#     cur.execute(f"update users set token='none' where email = '{u.get('email')}'")
#     mydb.commit()

def get_booking_list():
    with session() as ssn:
        spots=ssn.query(States).all()
        return [[row.state, row.city, row.available, row.code] for row in spots]

# def get_booking_list():
#     cur.execute(f"select state,city,available,code from states")
#     rows=[i for i in cur.fetchall()]
#     return rows

def get_booking_list_by_state(state:str):
    with session() as ssn:
        spots = ssn.query(States).filter(States.state.like(f"%{state}%")).all()
        return [[row.state, row.city, row.avaialble, row.code] for row in spots]

# def get_booking_list_by_state(state:str):
#     cur.execute(f"select state,city,available,code from states where state like '%{state}%'")
#     rows=[i for i in cur.fetchall()]
#     return rows

def get_spot(code:str):
    with session() as ssn:
        spot=ssn.query(States).filter(States.code==code).first()
        return vars(spot)

# def get_spot(code:str):
#     cur.execute(f"select state,city,available,code from states where code='{code}'")
#     c=cur.fetchone()
#     d={
#         "state":c[0],
#         "city":c[1],
#         "avaialble":c[2],
#         "code":c[3]
#     }
#     return d

def book_spot(u,s):
    with session() as ssn:
        booked = datetime.datetime.now().strftime(fmt)
        b=Booked(
            userid=u['userid'],
            state=s['state'],
            city=s['state'],
            booked=booked,
            code=s['code'],
        )
        ssn.add(b)
        ssn.commit()

# def book_spot(u:dict,s:dict):
#     booked = datetime.datetime.now().strftime(fmt)
#     cur.execute(f"insert into booked values ({u['userid']},'{s['state']}','{s['city']}','{booked}','{s['code']}')")
#     cur.execute(f"update states set available = available-1 where code = '{s['code']}'")
#     mydb.commit()

def get_release_list(u):
    with session() as ssn:
        lis=ssn.query(Booked).filter(Booked.userid==u['userid'])
        return [[r.state, r.city, r.booked, r.code] for r in lis]

# def get_release_list(u:dict):
#     cur.execute(f"select state, city, booked, code from booked where userid='{u['userid']}'")
#     c=[i for i in cur.fetchall()]
#     return c

def release_spot(u,code,booked):
    with session() as ssn:
        released = datetime.datetime.now().strftime(fmt)
        ssn.query(Booked).filter(
            Booked.userid==u['userid'],
            Booked.code==code,
            Booked.booked==booked
        ).first().delete()
        ssn.add(History(
            userid=u['userid'],
            state=dic[code]["state"],
            city=dic[code]["city"],
            booked=booked,
            released=released
        ))
        delta=datetime.datetime.strptime(released, fmt) - datetime.datetime.strptime(booked, fmt)
        hrs=math.ceil((delta.total_seconds())/3600)
        s=ssn.query(States).filter(States.code == code)
        s.hours += hrs
        s.avaialble += 1
        user=ssn.query(Users).filter(Users.userid == u['userid'])
        user -= hrs*50
        ssn.commit()

# def release_spot(u,code,booked):
#     userid=u.get("userid")
#     cur.execute(f"select state,city from booked where userid={userid} and code = '{code}' and booked = '{booked}'")
#     t=cur.fetchone()
#     state=t[0]
#     city=t[1]
#     released = datetime.datetime.now().strftime(fmt)
#     cur.execute(f"delete from booked where userid={userid} and code = '{code}' and booked = '{booked}' limit 1")
#     cur.execute(f"insert into history values ({userid},'{state}','{city}','{booked}','{released}')")
#     cur.execute(f"update states set available = available + 1 where code = '{code}'")
#     delta=datetime.datetime.strptime(released, fmt) - datetime.datetime.strptime(booked, fmt)
#     hrs=math.ceil((delta.total_seconds())/3600)
#     cur.execute(f"update users set wallet = wallet - {hrs * 50} where userid = {userid}")
#     cur.execute(f"update states set hours = hours+{hrs} where code = '{code}'")
#     mydb.commit()

def get_history(u:dict):
    with session() as ssn:
        if u['isadmin']==1:
            h=ssn.query(History).all()
            return [[r.userid,r.state,r.city,r.booked,r.released] for r in h]
        else:
            h=ssn.query(History).filter(History.userid == u['userid']).all()
            return [[r.state,r.city,r.booked,r.released] for r in h]

# def get_history(u:dict):
#     if u.get("isadmin")==1:
#         cur.execute(f"select * from history")
#         c=[i for i in cur.fetchall()]
#         return c
#     else:
#         cur.execute(f"select state, city, booked, released from history where userid='{u.get('userid')}'")
#         c=[i for i in cur.fetchall()]
#         return c

def get_user_history(userid:int):
    with session() as ssn:
        h=ssn.query(History).filter(History.userid == userid).all()
        return [[r.userid,r.state,r.city,r.booked,r.released] for r in h]

# def get_user_history(userid:int):
#     cur.execute(f"select * from history where userid={userid}")
#     c=[i for i in cur.fetchall()]
#     return c

def get_booking_history():
    with session() as ssn:
        h=ssn.query(Booked).all()
        return [[r.userid, r.state, r.city, r.booked] for r in h]

# def get_booking_history():
#     cur.execute(f"select * from booked")
#     c=[i for i in cur.fetchall()]
#     return c

def get_revenue_statewise():
    with session() as ssn:
        h=ssn.query(States.state, func.sum(States.hours) * 50).group_by(States.state).all()
        return [list(i) for i in h]

# def get_revenue_statewise():
#     cur.execute(f"select state,sum(hours)*50 from states group by state")
#     c=[i for i in cur.fetchall()]
#     return c

def get_revenue_citywise():
    with session() as ssn:
        h=ssn.query(States.state, States.city, States.hours * 50).all()
        return [list(i) for i in h]

# def get_revenue_citywise():
#     cur.execute(f"select state,city,hours*50 from states")
#     c=[i for i in cur.fetchall()]
#     return c

def get_revenue_for_state(state:str):
    with session() as ssn:
        h=ssn.query(States.city, States.hours * 50).filter(States.state == state).all()
        return [list(i) for i in h]

# def get_revenue_for_state(state:str):
#     cur.execute(f"select city,hours*50 from states where state = '{state}'")
#     c=[i for i in cur.fetchall()]
#     return c
