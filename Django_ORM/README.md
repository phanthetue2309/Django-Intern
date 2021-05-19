# Django ORM 
## Model One To One 
- First we code build a model one to one : it mean every customer owns only one vehicle. Thus, a one-to-one relationship exists.
![One-To-One](image/OneToOne_Code.PNG)
- This is how model mean :
![One-To-One-RealtionShip](image/one-to-one-relationship.png)
- Database : 
![One-To-One-RealtionShip](image/OneToOne.PNG)

## Model One To Many 
- Model : 
![One-To-Many](image/OneToMany_Code.PNG)
- This is how model mean : A one to many relationships is where one object from table1 can have multiple relations with entities in table2. Although, table2 objects will have only one relation to the object of table1.
![One-To-Many-RealtionShip](image/one-to-many-relationship.png)
- Database : 
![One-To-Many-RealtionShip](image/OneToMany.PNG)

## Model Many To Many 
- Model : 
![Many-To-Many](image/ManyToMany_Code.PNG)
- Here we have multiple workers for multiple machines. A worker can be assigned to operate more than one machine. Also, a machine can be operated by multiple workers one at a time.
![Many-To-Many-RealtionShip](image/many-to-many-relationship.png)
- This is a special case of relationships. Many to Many Relationship requires a separate table. There they store objects related to other objects.
- Database : 
![Many-To-Many-RealtionShip](image/ManyToMany.PNG)

## Full in Admin 
![admin](image/admin_view.PNG)
