C:\Users\neo\AppData\Local\Programs\Python\Python36\
C:\Users\neo\blogprojectril
---------- Windows OS -----------------
install python v3.6.5 - from the website msi installer
install django v2.0.6 - pip install Django==2.0.6
------------------------------------------------

============== Ubuntu 18.04 LTS ==============
--Setup Python 3 on Ubuntu 18.04 LTS--
-On my Ubuntu machine, there are two versions of python available, python2.7 as default python version and python3.
-In this step, we will change the default python version to python 3.
-Check the python version:
	$ python --version

-So the default python is 2.7 at the moment.
-Next, change the default python to python version 3 with the 'update-alternatives' command:
	$ update-alternatives --install /usr/bin/python python /usr/bin/python3 1

-Now check again the python version:
	$ python --version

-And you will get python 3.6 as a default python on the system.


--Install Django--
-Run command below to install pip for python 3.
	$sudo apt install python3-pip -y

-The installation will add a new binary file called 'pip3'. To make it easier to use pip, I will create a symlink for pip3 to pip:
	$ which pip3
	$ ln -s /usr/bin/pip3 /usr/bin/pip

-Now check the version :
	$pip --version	
	$ pip install Django

-After the installation is complete, check the Django version with the command below:
	$ python
	>>> import django
	>>> print(django.get_version())

=================================================

SETUP ECLIPSE FOR DJANGO PROJECT :
3. install pydev in eclipse oxygen
4. Preferences -> pydev -> interpreters -> python interpreters : give the location of the exe of python version 
5. import all libs in PYTHONPATH

------------------------------------------------

START SERVER :

1. cd C:\Users\neo\blogprojectril
2. python .\manage.py runserver

STARTING APPS IN DJANGO :
1. cd C:\Users\neo\blogprojectril
2. python .\manage.py startapp <appname>


How to create a superuser in Django ?
1. cd C:\Users\neo\blogprojectril
2. python manage.py createsuperuser (neo, kumarmitesh88215@gmail.com, 231513mitesh)
									(mitz, mtz@gmail.com, 88215mitesh)
									(tiger, kumarmitesh88215@gmail.com , 231513mitesh )

-----------------------------------------------------------------

Creating New Application :
1. python manage.py startapp <nameofapp>
	
-----------------------------------------------------

Creating Model for Database tables creation :
1. create classes in models.py for tables.
2.  python manage.py makemigrations rilblog -- Creates a migration file in the migrations folder in the app 
3.  python manage.py migrate <appname> -- making it available for all stuffs in the project.

Q) How table from models will show in admin pannel?
A) in the app , in the admin.py add: admin.site.register(<model classname>)

To access those tables from the database :

1. python manage.py shell  -- to access the project's shell terminal
2. >>> from <appname>.models import <tablename1, tablename2, ...>
3. <tablename>.objects.all() -- for getting the no. of objects in table

Either:
4. a = <tablename>(field= "value",field= "value",field= "value",field= "value") -- to insert a new row
5. a.save()  -- now in shells memory , to save from shells memory to the database
Or:
4. a = user()
5. a.user_name = "John Abrahim"

Q) How to add Foreign key in another table from shell ?
A) b.post_id = a(id=1)

Q) How to format Output which is not useful by default?:>>> user.objects.all()	>>> <QuerySet [<user: user object (1)>]>
1. def __str__ (self):
	return (self.<field_name>) -- in each class for a table in model u have to do this.

Q) How to filter the data from the table?
A) <tablename>.objects.filter(id = 1) -- for getting the no. of objects in table

Q) How to access tables from the admin page : 
A) from .models import <classname of table>
	admin.site.register(<classname>)

Q) How to Delete database tables ?
	A) For a quick resolve (if you don't care about losing your tables/data), correct your models.py file with the desired data types, delete the Migration folder and db.SQLite3 file, then re-run the following commands:
	python manage.py migrate
	python manage.py makemigrations <appname>
	python manage.py migrate
	python manage.py createsuperuser (to create an admin user/pswd to manage admin page)
	python manage.py runserver


Q) How to update a field in database ?
A) >>> from django.db.models import F     # F gives the Fieldvalue of any field we want and then i can perform operations on it
	>>> Comments.objects.filter(id = 4).update(user=F("user")+4)



------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------

Q) What is the PYTHONPATH environment variable?
A) The PYTHONPATH environment variable is the list of folders that the import statement will look through when attempting to resolve a module name.	

Q) How to set the PYTHONPATH environment variable on Windows XP, Vista, Windows 7, etc?
A) For Windows the PYTHONPATH is set in the windows registry.	
	-> Run regedit - First, open up �Run� from the start menu (Ctrl + R).
	-> Browse to the PythonPath folder - Browse to HKEY_LOCAL_MACHINE -> SOFTWARE -> Python -> PythonCore -> [ Version Number ] -> PythonPath.(Don't alter the pythonpath you see here.)
	-> Create new key - Right click the PythonPath folder and select New -> Key (Name it what you like.)
	-> Select the new folder and right click the one blank value sitting on the right side of the screen and select Modify.
For the value field, add your new paths separated by � ; �
	-> Run python and try an import.

Q) How does python find packages?
A) Python imports work by searching the directories listed in sys.path.
	I/P : 	> import sys
			> print ('\n'.join(sys.path))
	O/P	: 
			C:\Users\neo\AppData\Local\Programs\Python\Python36\Lib\idlelib
			C:\Users\neo\AppData\Local\Programs\Python\Python36\python36.zip
			C:\Users\neo\AppData\Local\Programs\Python\Python36\DLLs
			C:\Users\neo\AppData\Local\Programs\Python\Python36\lib
			C:\Users\neo\AppData\Local\Programs\Python\Python36
			C:\Users\neo\AppData\Local\Programs\Python\Python36\lib\site-packages	
			

PEP STANDARD: A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important.(Source-https://www.python.org/dev/peps/pep-0008/)


Q) What are Python Modules?
A) (Source - https://docs.python.org/3/tutorial/modules.html) If you quit from the Python interpreter and enter it again, the definitions you have made (functions and variables) are lost.

Q) Uses of IMPORT statement in Python- create a file called "fibo.py" in the current directory with the following contents:
	# Fibonacci numbers module
	def fib(n):    # write Fibonacci series up to n
	    a, b = 0, 1
	    while b < n:
	        print(b, end=' ')
	        a, b = b, a+b
	    print()
	def fib2(n):   # return Fibonacci series up to n
	    result = []
	    a, b = 0, 1
	    while b < n:
	        result.append(b)
	        a, b = b, a+b
	    return result
	--------
	>>> from fibo import *
	>>> fib(500)
	[This imports all names except those beginning with an underscore (_). In most cases Python programmers do not use this facility since it introduces an unknown set of names into the 
	interpreter, possibly hiding some things you have already defined.]
	--------
	>>> import fibo
	>>> fibo.fib(1000)
	1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
	--------
	>>> fib = fibo.fib
	>>> fib(500)
	1 1 2 3 5 8 13 21 34 55 89 144 233 377
	--------
	If the module name is followed by "as", then the name following "as" is bound directly to the imported module.
	>>> import fibo as fib
	>>> fib.fib(500)
	0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
		
	It can also be used when utilising "from" with similar effects:
	>>> from fibo import fib as fibonacci
	>>> fibonacci(500)
	0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

	
Q) More on Modules?
A)  1. A module can contain executable statements as well as function definitions.
	2. Modules can import other modules.	
	
	
	
	
        
        
        
        
	
	
	
	