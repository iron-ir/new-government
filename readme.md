نحوه استارت کردن پروژه
===================================

* ابتدا آخرین نسخه [پایتون](https://www.python.org/downloads/) را دانلود و نصب کنید.
* سپس از نصب پایتون در سیستم خود مطمئن شوید.
در ترمینال خود دستور زیر را بزنید درصورتی که پایتون نصب شده باشد ورژن پایتون نصب شده را برایتان نمایش می دهد.
        
        (base)[root@root ~]$ python -V
        Python 3.9.3
        (base)[root@root ~]$
            
* پروژه را کلون کرده
* در ترمینال در یک دایرکتوری مورد نظر خود رفته و یک ماشین مجازی بسازید 
با دستور زیر یک ماشین مجازی بسازید

		(base)[root@root ~]$ cd my/path/venvs/
		(base)[root@root venvs]$ python -m venv venv_name
		(base)[root@root venvs]$

* حال شما بایستی به دایرکتوری مربط به ماشین های مجازیتان رفته و ماشین مجازی خود را با دستور زیر فعال کنید.

        (base)[root@root venvs]$ cd venv_name/Script
        (base)[root@root Script]$ activate
        (venv_name)[root@root Script]$

* حالا شما ماشین مجازی خود را ساخته اید در گام بعدی بایستی به دایرکتوری پروژه ی کلون شده ی خود بروید .

        (venv_name)[root@root ~]$ cd my/project/path/
        (venv_name)[root@root my_project]$ 
       
* برای اینکه کتابخانه های نصب شده در پروژه را نصب کنید دستور زیر را وارد کنید.

        (venv_name)[root@root my_project]$ pip install -r requirements.txt        
        
* سپس برای ساخت دیتابیس دستور زیر را وارد کنید.

        (venv_name)[root@root my_project]$ python manage.py migrate
        
* حال برای دسترسی به پنل ادمین سایت بایستی یک سوپرادمین بسازید.
برای این کار دستور زیر را وارد می کنید.

        (venv_name)[root@root my_project]$ python manage.py createsuperuser
        username: nvd
        email address: nvd@nvd.com
        password: ********
        password (again): ********
        By password validation and create user anyway? [y/N]: y
        Superuser created successfully.
        (venv_name)[root@root my_project]$ 

* در ادامه شما بایستی سرور پایتونی خود را ران کنید.

        (venv_name)[root@root my_project]$ python manage.py runserver
        Watching for file changes with StatReloader
        Performing system checks...
        
        System check identified no issues (0 silenced).
        April 27, 2021 - 07:09:39
        Django version 3.2, using settings 'new_government.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CONTROL-C.


حال کافی است به آدرس نمایش داده شده بروید و از دیدن جنگو لذت ببرید.


در صورتی که تمایل داشتید دستورات دیگر جنگو را ببینید دستور زیر را وارد کنید.

        (venv_name)[root@root my_project]$ python manage.py help
        
        Type 'manage.py help <subcommand>' for help on a specific subcommand.

            Available subcommands:

        [auth]
            changepassword
            createsuperuser
            
        [contenttypes]
            remove_stale_contenttypes
            
        [debug_toolbar]
            debugsqlshell

        [django]
            check
            compilemessages
            createcachetable
            dbshell
            diffsettings
            dumpdata
            flush
            inspectdb
            loaddata
            makemessages
            makemigrations
            migrate
            sendtestemail
            shell
            showmigrations
            sqlflush
            sqlmigrate
            sqlsequencereset
            squashmigrations
            startapp
            startproject
            test
            testserver
        
        [sessions]
            clearsessions
        
        [staticfiles]
            collectstatic
            findstatic
            runserver

