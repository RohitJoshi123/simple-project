simple-djangoproject
-------------------------
Vanilla Django project that can be used as a "skeleton" to build more complex projects. 
I use is mainly to prove that the ``project-buildout`` works as needed.

Uses ``Django-South`` for database evolutions.

Uses ``django-extensions``. Among other tools, this gives us the ``shell_plus`` which is accessible by::

	bin/manage shell_plus

How to create applications under the project
--------------------------------------------
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



