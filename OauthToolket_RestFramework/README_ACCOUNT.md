# Create Account From HRM Project

## Create model User 

- Model User using with Role : 
    - Class Role : 
    
            class Role(models.Model):
                name = models.CharField(max_length=255)
                permissions_role = models.TextField(null=True)
                description = models.TextField()
            
                def __str__(self):
                    return self.name
    
    
## Create model Base User 

- Class UserManager : 
      
            class UserManager(BaseUserManager):
                def create_user(self, email, password=None):
                    """
                    Creates and saves a User with the given email and password.
                    """
                    if not email:
                        raise ValueError('Users must have an email address')
            
                    user = self.model(
                        email=self.normalize_email(email),
                    )
            
                    user.set_password(password)
                    user.save(using=self._db)
                    return user
            
                def create_staffuser(self, email, password):
                    """
                    Creates and saves a staff user with the given email and password.
                    """
                    user = self.create_user(
                        email,
                        password=password,
                    )
                    user.staff = True
                    user.save(using=self._db)
                    return user
            
                def create_superuser(self, email, password):
                    """
                    Creates and saves a superuser with the given email and password.
                    """
                    user = self.create_user(
                        email,
                        password=password,
                    )
                    user.staff = True
                    user.admin = True
                    user.save(using=self._db)
                    return user

## Add Role merge with model User



# Test Generate Access Token  

## Test Register with Model User and get access token

![img_8.png](image/img_8.png)

## Test  Login with access token

![img_9.png](image/img_9.png)

