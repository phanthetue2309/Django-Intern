# Django-Intern

Overview
A view is a “type” of Web page in your Django application that generally serves a specific function and has a specific template. For example, in a blog application, you might have the following views:

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