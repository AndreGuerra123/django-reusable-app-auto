=============================
Django Reusable App Auto
=============================

.. image:: https://badge.fury.io/py/django-reusable-app-auto.svg
    :target: https://badge.fury.io/py/django-reusable-app-auto

.. image:: https://circleci.com/gh/AndreGuerra123/django-reusable-app-auto.svg?style=svg
    :target: https://circleci.com/gh/AndreGuerra123/django-reusable-app-auto

.. image:: https://codecov.io/gh/AndreGuerra123/django-reusable-app-auto/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/AndreGuerra123/django-reusable-app-auto

Your project description goes here

Documentation
-------------

The full documentation is at https://django-reusable-app-auto.readthedocs.io.

Quickstart
----------

Install Django Reusable App Auto::

    pip install django-reusable-app-auto

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_reusable_app_auto',
        ...
    )

Add Django Reusable App Auto's URL patterns:

.. code-block:: python

    import django_reusable_app_auto

    urlpatterns = [
        ...
        path('/django_reusable_app_auto', include(django_reusable_app_auto.urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?::
    $ cd django-reusable-app-auto
    $ poetry install
    $ poetry run runtests.py

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`django-reusable-app`: https://github.com/AndreGuerra123/django-reusable-app
