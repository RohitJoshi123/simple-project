simple-project
****************

What???
=============
Vanilla Django project that can be used as a "skeleton" to build more complex projects. 
I use is mainly to prove that the ``project-buildout`` works as needed.

Database Evolutions

Django South
-------------
Uses ``Django-South`` to handle database evolutions/modifications.

Django extensions
-------------------
Uses ``django-extensions``. Among other tools, this gives us the ``shell_plus`` which is accessible by::

	bin/manage shell_plus

This is a great tool for testing and fooling around with the project.


Static file serving
----------------------

This Django project, comes ready to serve static files. The static files are picked up from the ``static/`` folder of the application, and are copied under the ``STATIC_ROOT``. The whole procedure is handled by the application ``django.contrib.staticfiles``. The ``deploy`` script calls management command ``bin/manage collectfiles`` which does all the job for us.

So in case you have css/js or other static files, simply place them in the folder ``static/``. Subsequently, a template for example, can access the static css files by using::

	href="<static_url>/path/to/file/relative/to/static_root"
	
The apache configuration then maps the ``STATIC_URL`` to the ``STATIC_ROOT``, and the files are able to be served.

Subdomains
-----------
In the case of this app, the main application listens to ``www.<domain>``, and the static content comes from ``assets.<domain>``. All these parameters are handled by the buildout scripts.


How to create applications under the project
============================================
*	::

		bin/manage startapp <appname>

*	Add the app in INSTALLED_APPS list in settings.py, in the form::

		<projectegg>.<appname>

*	Create the database models of the app in file ``models.py``

*	Include the app under South's monitoring::

		bin/manage schemamigration <appname> --initial

*	Run the deploy script to apply the migrations::

		bin/deploy

*	Alternatively, we could just apply the migrations using::		

		bin/manage migrate	<appname>



