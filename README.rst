Setup
=====

The setup::

    git clone https://github.com/toastdriven/bobbyblog.git
    cd bobbyblog

    virtualenv env
    . env/bin/activate
    pip install -r requirements.txt

    ./manage.py syncdb

    ./manage.py loaddata blog.json

    ./manage.py runserver


From there, hit::

* http://127.0.0.1:8000/api/v1/category/?format=json (should be two results)
* http://127.0.0.1:8000/api/v1/category/?format=json&title=Foo (should be just one)
