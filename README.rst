Uploading Files Securely with Flask
===================================

A practical demonstration of how to securely store file uploads on the filesystem with `Flask`_.


Install
-------

**Clone files**

.. code-block:: text

    $ git clone https://github.com/henriquesgabriel/flask-upload-secure.git
    $ cd flask-upload-secure

**Install and setup** `virtualenv`_

.. code-block:: text

    $ pip3 install virtualenv

**Create a virtual environment with virtualenv**

.. code-block:: text

    $ virtualenv venv

**You can also create a virtual environment using Python3**

.. code-block:: text

    $ python3 -m venv venv

**Activate the virtual environment**

.. code-block:: text

    $ source venv/bin/activate


**Install project dependencies**

.. code-block:: text

    $ pip install -r requirements.txt


Run
---

.. code-block:: text

    $ export FLASK_APP=app.py
    $ export FLASK_ENV=development
    $ flask run


.. _Flask: http://flask.pocoo.org

.. _virtualenv: https://pypi.org/project/virtualenv/
