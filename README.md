# Django-Intern

Overview
A view is a “type” of Web page in your Django application that generally serves a specific function and has a specific template. For example, in a blog application, you might have the following views:

Blog homepage – displays the latest few entries.
Entry “detail” page – permalink page for a single entry.
Year-based archive page – displays all months with entries in the given year.
Month-based archive page – displays all days with entries in the given month.
Day-based archive page – displays all entries in the given day.
Comment action – handles posting comments to a given entry.
In our poll application, we’ll have the following four views:

Question “index” page – displays the latest few questions.
Question “detail” page – displays a question text, with no results but with a form to vote.
Question “results” page – displays results for a particular question.
Vote action – handles voting for a particular choice in a particular question.