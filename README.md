# Django-Intern

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