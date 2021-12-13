class user_data:
    def __init__(self):
        self.location=input("Enter your area:")


    def h_dis(self,location):
        if self.location=="tambaram":
            self.nonveg=[{"hotel1":"salem rr","rate":"3-star"},
                    {"hotel2":"thalapakatti","rate":"5-star"},
                    {"hotel3":"quality restauarant","rate":"5-star"},
                    {"hotel4":"dine and fun","rate":"4-star"},
                    {"hotel5":"alif","rate":"4-star"}]


        
            self.veg=[{"hotel6":"namma veedu vasantha bhavan","rate":"4-star"},
                    {"hotel7":"sangeetha veg","rate":"5-star"},
                    {"hotel8":"annachi mess","rate":"5-star"},
                    {"hotel9":"new aryaas","rate":"4-star"},
                    {"hotel10":"tongue restuarant","rate":"5-star"}]

        elif self.location=="medavakkam":
            self.nonveg=[{"hotel11":"sri slvaa chetinad hotel","rate":"3-star"},
                    {"hotel12":"naachiyar","rate":"4-star"},
                    {"hotel13":"AGS","rate":"5-star"},
                    {"hotel14":"the paradise","rate":"5-star"},
                    {"hotel15":"pandiyass","rate":"4-star"}]
            
            self.veg=[{"hotel16":"Fayaz","rate":"4-star"},
                    {"hotel17":"aruvi","rate":"3-star"},
                    {"hotel18":"ashwahty bhuvan","rate":"4-star"},
                    {"hotel19":"sumaatra","rate":"4-star"},
                    {"hotel20":"deepam","rate":"5-star"}]

            
        elif self.location=="santhospuram":
            self.nonveg=[{"hotel21":"Bismillah","rate":"3-star"},
                    {"hotel22":"RK.pandian","rate":"4-star"},
                    {"hotel23":"punjabi","rate":"3-star"},
                    {"hotel24":"palmshore","rate":"5-star"},
                    {"hotel25":"Grand biriyani","rate":"5-star"}]
            
            self.veg=[{"hotel26":"bhaavan","rate":"4-star"},
                    {"hotel27":"amigo","rate":"3-star"},
                    {"hotel28":"shree krishanu bhuvan","rate":"2-star"},
                    {"hotel29":"spicean","rate":"5-star"},
                    {"hotel30":"chennai bhavan","rate":"2-star"}]
        else:
            print("Out of your location")


        
    def diss_nv(self):        
        for i in self.nonveg:
            f={}
            f=i
            for k,v in f.items():
                print(k,"\t--- \t",v)

    def diss_v(self):
        for i in  self.veg:
            g={}
            g=i
        for j,u in g.items():
            print(j,"\t--- \t",u)
                 

class sellers(user_data):
    def _init_(self):
        self.uh = input("Enter hotel: ")
        self.hotel=["hotel1","hotel2","hotel3","hotel4","hotel5","hotel6","hotel7","hotel8","hotel9","hotel10",
                "hotel1","hotel12","hotel13","hotel14","hotel15","hotel15","hotel6","hotel17","hotel18","hotel9","hotel20",
                "hotel21","hotel22","hotel23","hotel24","hotel25","hotel26","hotel27","hotel28","hotel29","hotel30"]
       
        

    def di(self):
        for i in self.hotel:
            print("\n",i)
                
    def uh_val(self):
        for i in self.hotel:
            if (i != self.uh):
                raise ValueError("this hotel is not valid")
            
class dish(sellers):
    def _init_(self):
        self.f=["dish1","dish2","dish3","dish4","dish5"]
        self.diss()
        self.user_dis= input("Enter dish you want: ")

    def dish_val(self):
        for i in self.f:
            if (i != self.user_dis):
                raise ValueError ("you mentioned dish is not available")
            else:
                print("Packing....")
                break
            
    def diss(self):
        print("\n Available dish")
        
        for i in self.f:
            print(i)
class swiggy:
    def _init_(self,loaction,hotel,dish):
        self.area = loaction
        self.hotelname = hotel
        self.dishname = dish
        
    def beforeorder(self):
        print("order details",self.area,self.h,self.d)

    def display(self):
        print("order confirmed :",self.hotelname," \n @",self.hotelname," in ",self.dishname)

class user_dis(swiggy):
    def _init_(self):
        self.bill = 1500
        self.sgst = 5
        self.cgst = 10
        self.total = (self.bill+self.sgst+self.cgst)

    def delivery(self):
        self.addrres = input("Enter address: ")


    def addvalid(self):
        if isinstance (self.addr,str):
            if isinstance(len(self.addr) <= 25):
                raise ValueError ("enter valid address")
            elif self.addr != None:
                raise ValueError ("this is an invalid address")
                
        
    def display(self):
        print("Delivary address : ",self.addr)
        print("Total bill Rs.",self.total)
        ob1.display()


ob= user_data()
ob.h_dis(ob.location)
ob.diss_v()
ob.diss_nv()
d = dish()
d.dish_val()
ob1 = swiggy(ob.area,h.uh,d.user_dis)
ob1.beforeorder()
ob2 = user_dis()

ob2.delivery()
ob2.addvalid
ob2.display()
        

    
