I am Pharaoh
============

**I am Pharaoh** is scaffold create to Django users which are starting
with `Pyramid`_.

Install:
~~~~~~~~

::

    pip install iampharaoh

After, verify your scaffold’s:

::

    pcreate -l

Result:

::

    Available scaffolds:
        alchemy:                 Pyramid SQLAlchemy project using url dispatch
        pharaohapps:             Create an 'app' in project. - Like startapp Django
        pharaohproject:          Scaffold created for Django users initiate with Pyramid more comfortably
        starter:                 Pyramid starter project
        zodb:                    Pyramid ZODB project using traversal

Only **pharaohapps** and **pharaohproject** are created by **I am
Pharaoh**, others are default in Pyramid

How to:
~~~~~~~

After install **I am Pharaoh**, start a new project

::

    pcreate -s pharaohproject nameOfProject

The result in nameOfProeject folder is:

::

    ├── LICENSE
    ├── MANIFEST.in
    ├── README
    ├── nameOfProject
    │   ├── __init__.py
    │   ├── nameOfProject
    │   │   ├── __init__.py
    │   │   ├── base_model.py
    │   │   └── urls.py
    │   ├── scripts
    │   │   ├── __init__.py
    │   │   ├── destroydb.py
    │   │   └── initializedb.py
    │   └── static
    ├── development.ini
    ├── production.ini
    ├── setup.cfg
    └── setup.py

So, run in you project:

::

    python setup.py develop

This command will download some packages, but the most significant for
Django users are:

-  `SQLAlchemy`_: The Python SQL Toolkit and Object Relational Mapper.
-  `Alembic`_: Migrations.
-  `WTForms-Alchemy`_: Forms and ModelForm.
-  `pyramid\_jinja2`_: Template Engine.

Create App
~~~~~~~~~~

Whitin your project (Like Django):

::

    pcreate -s pharaohapps nameOfApp

The result in nameOfProeject folder now is:

::

    ├── LICENSE
    ├── MANIFEST.in
    ├── README
    ├── nameOfProject
    │   ├── __init__.py
    │   ├── nameOfProject
    │   │   ├── __init__.py
    │   │   ├── base_model.py
    │   │   └── urls.py
    │   ├── nameOfApp -> add after run last command
    │   │   ├── __init__.py
    │   │   ├── models.py
    │   │   ├── templates
    │   │   │   └── index.html
    │   │   ├── urls.py
    │   │   └── views.py
    │   ├── scripts
    │   │   ├── __init__.py
    │   │   ├── destroydb.py
    │   │   └── initializedb.py
    │   └── static
    ├── development.ini
    ├── production.ini
    ├── setup.cfg
    └── setup.py

To connect app in project:

::

        # nameOfProject/urls.py
        config.include("nameOfProject.nameOfApp.urls")

.. _Pyramid: http://docs.pylonsproject.org/en/latest/
.. _SQLAlchemy: http://www.sqlalchemy.org
.. _Alembic: http://alembic.readthedocs.org/en/latest/
.. _WTForms-Alchemy: https://wtforms-alchemy.readthedocs.org/en/latest/
.. _pyramid\_jinja2: https://github.com/Pylons/pyramid_jinja2
