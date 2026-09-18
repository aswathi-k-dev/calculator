### DJANGO MODELS AND ORM QUERY

### DJANGO MODEL
---

- abstract of a database table
- a model is a python class that inherits from django.db.models.Model
- each attribute of class maps to databse column

EG: Employee[id,name,department,salary,location]

```

our_app > models.py

from django.db import models

class Employee(models.Model):
    
    name = models.CharField(max_length = 200)

    department = models.CharField(max_length = 200)

    salary = models.PositiveIntegerField()

    location = models.CharField(max_length = 200)

```

query_file =>

```

terminal > python manage.py makemigrations

```

query file execute =>

```
terminal > python manage.py migrate
```

#### ORM (OBJECT RELATIONAL MAPPING)

---

ORM stands for object relational mapping, a software technique that lets you talk to a database using your regular programming language instead of writing raw sql

*ORM QUERY FOR FETCHING ALL RECORDS FROM TABLE*

mysql :
```
mysql > select * from employee;
```

orm:
```
qs = Modelname.objects.all()

eg:

qs = Employee.objects.all()

*ORM QUERY FOR INSERTING A RECORD OR CREATING AN RESOURCE*

mysql:
```
mysql > insert into employee(name,department,salary,location)values(val1,...)
```
orm :
```
orm > Modelname.objects.create(field = value,field = value)

eg:

orm > Employee.objects.create(name = "hari",department = "hr",salary = 20000,location = "kochi")

```

*Orm query for fetching a specific record*

mysql:
```
mysql> select * from employee where id = 1;
```

orm :

```
orm > qs = Modelname.objects.get(condition)

eg:

orm >qs =  Employee.objects.get(id = 5)

or 

orm > qs = Modelname.objects.filter(condition)

orm > qs = Employee.objects.filter(id = 5)

```

*ORM QUERY FOR UPDATING RECORD*

mysql:
```
mysql> update employee set department = "hr",salary = 55000 where id = 5;
```

orm 

```

 orm > Models.objects.filter(condition).update(field = value,field = value)

 eg :

 orm > Employee.objects.filter(id = 5).update(department = "it",salary = 50000,location = "palakkad")

 ```

 *orm query for deleting record*

 mysql :
 ```
 mysql : delete from employee where id = 1;

 ```

 orm :
 ```
 
 orm > ModelName.objects.get(condition).delete()

 eg:

 Employee.objects.get(id = 5).delete()
 
 ```