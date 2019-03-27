=====
Usage
=====

To use Django Reusable App Auto in a project, add it to your `INSTALLED_APPS`:

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
        url(r'^', include(django_reusable_app_auto.urls)),
        ...
    ]
