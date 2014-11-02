#I am Pharaoh

**I am Pharaoh** is scaffold create to Django users which are starting with [Pyramid](http://docs.pylonsproject.org/en/latest/).


### Install:

	pip install iampharaoh

After, verify your scaffold's:

	pcreate -l

Result:

	Available scaffolds:
  		alchemy:                 Pyramid SQLAlchemy project using url dispatch
  		pharaohapps:             Create an 'app' in project. - Like startapp Django
  		pharaohproject:          Scaffold created for Django users initiate with Pyramid more comfortably
  		starter:                 Pyramid starter project
  		zodb:                    Pyramid ZODB project using traversal

Only **pharaohapps** and **pharaohproject** are created by **I am Pharaoh**, others are default in Pyramid

### How to:

After install **I am Pharaoh**, start a new project

	pcreate -s pharaohproject nameOfProject


The result in nameOfProeject folder is:


	├── LICENSE
	├── MANIFEST.in
	├── README
	├── nameOfProject
	│   ├── __init__.py
	│   ├── nameOfProject
	│   │   ├── __init__.py
	│   │   ├── base_model.py
	│   │   └── urls.py
	│   ├── scripts
	│   │   ├── __init__.py
	│   │   ├── destroydb.py
	│   │   └── initializedb.py
	│   └── static
	├── development.ini
	├── production.ini
	├── setup.cfg
	└── setup.py

So, run in you project:

	python setup.py develop

This command will download some packages, but the most significant for Django users are:

[SQLAlchemy](http://www.sqlalchemy.org): The Python SQL Toolkit and Object Relational Mapper.
[Alembic](http://alembic.readthedocs.org/en/latest/): Migrations.
[WTForms-Alchemy](https://wtforms-alchemy.readthedocs.org/en/latest/): Forms and ModelForm.
[pyramid_jinja2](https://github.com/Pylons/pyramid_jinja2): Template Engine.
