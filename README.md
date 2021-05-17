# Django-Intern

## Tutorial 3
Overview
A view is a “type” of Web page in your Django application that generally serves a specific function and has a specific template. The following views of this project is :

Blog homepage – displays the latest few entries. <br>
Entry “detail” page – permalink page for a single entry. <br>
Year-based archive page – displays all months with entries in the given year.<br>
Month-based archive page – displays all days with entries in the given month.<br>
Day-based archive page – displays all entries in the given day.<br>
Comment action – handles posting comments to a given entry.<br>
In our poll application, we’ll have the following four views:<br>

Question “index” page – displays the latest few questions.<br>
Question “detail” page – displays a question text, with no results but with a form to vote.<br>
Question “results” page – displays results for a particular question.<br>
Vote action – handles voting for a particular choice in a particular question.<br>

## Tutorial 4 : 

Write a minima form : 
![Image-minimalForm](image/minimal_form.PNG)

Working with POST method : 
![Image-def_vote_tutorial4](image/def_vote_tutorial4.PNG)

request.POST is a dictionary-like object that lets you access submitted data by key name. <br>
In this case, request.POST['choice'] returns the ID of the selected choice, as a string. <br>
request.POST values are always strings. <br>


request.POST['choice'] will raise KeyError if choice wasn’t provided in POST data. <br>
The above code checks for KeyError and redisplays the question form with an error message if choice isn’t given. <br>

After incrementing the choice count, the code returns an HttpResponseRedirect rather than a normal HttpResponse. HttpResponseRedirect takes a single argument: the URL to which the user will be redirected (see the following point for how we construct the URL in this case). 


We are using the reverse() function in the HttpResponseRedirect constructor in this example. <br>
This function helps avoid having to hardcode a URL in the view function. It is given the name of the view that we want to pass control to and the variable portion of the URL pattern that points to that view. In this case, using the URLconf we set up in Tutorial 3, this reverse() call will return a string like

We can change for better code by using Generic View : <br> 
![Image-generic_view](image/generic_view_code.PNG) <br> 
By using Generic view we can save time and energy and it more efficient about your code. 

This is end Tutorial 4 

## Tutorial 5
Now we change to Part 5 : Automated Testing  <br>
We all know why we have to use Test so now we have some information about way to test :<br>
https://en.wikipedia.org/wiki/Test-driven_development <br>

## First Test is about Identify Bug
First , we got some problem about day publish : 
![Image-bug_time](image/bug_time_Tutorial_5.PNG) <br> 

Something wrong Right ? <br>
So we create a auto test like this : 
![Image-create_test](image/create_test.PNG) <br> 
And The bug here : 
![Image-bug_show](image/bug_show.PNG) <br> 
And now we have to solve this bug : <br>
![Image-fix_bug_test](image/fix_bug_test.PNG) <br> 
Now the bug has been fixed : <br>
![Image-solve_bug_show](image/solve_bug_show.PNG) <br> 

So what all Django have done : 
    manage.py test polls looked for tests in the polls application <br>
    it found a subclass of the django.test.TestCase class <br>
    it created a special database for the purpose of testing <br>
    it looked for test methods - ones whose names begin with test <br>
    in test_was_published_recently_with_future_question it created a Question instance whose pub_date field is 30 days in the future <br>
    … and using the assertIs() method, it discovered that its was_published_recently() returns True, though we wanted it to return False <br>

After this we have some bug have to fix in : <br>
    Client Action <br>
    URL pattern <br>