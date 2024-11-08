STEP : 1 ==> pip instal flask (For Flask)  
STEP : 2 ==> pip install psycopg2 (For Postgres)  
STEP : 3 ==> pip install sqlalchemy (For SQL toolkit)  
STEP : 4 ==> app = Flask(\_\_name\_\_) (For Instance creation for flask)  
STEP : 5 ==> For Configure PostgreSQL URI:  
                             app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5433/postgres'  
                             app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
STEP : 5 ==> db = SQLAlchemy(app) (For Database Initialization)  
STEP : 6 ==> Model Creation  
STEP : 7 ==> Table Creation in Database  
STEP : 8 ==> REST Methods Creation ['POST','PUT','GET','DELETE']  
STEP : 9 ==> Run the App  
if \_\_name\_\_ == '\_\_main\_\_':  
app.run(debug=True)  
STEP : 10 ==> Test it With POSTMAN Tool
