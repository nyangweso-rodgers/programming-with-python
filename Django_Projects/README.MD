# Django - Python
__Django__ is a web development framework that assists in building and maintaining quality web applications. It helps eliminate repetitive tasks making the development process an easy and time-saving experience. __Django__ is a high-level Python web framework that encourages rapid developmnt and clean, progmatic design. It makes it easier to build better web apps quickly and with less code.

# Advantages of Django
* __Object-Retaional Mapping (ORM) Support__ : Django provides a bridge between the data model and the database engine, and supports a large set of databases including MySQL, Oracle, Postgres. It also supports NoSQL databases through __Django-nonrel fork__. For now, the only NoSQL databases supported are __MongoDB__ and __google app engine__.
* __Multilingual Support__: Django supports multilingual websites through its built-in internalization system. So you can develop your websites, which would support multiple languages.
* __Framework Support:__ Django has built-in support for __Ajax__, __RSS__, __Caching__ and various other frameworks.
* __Development Environment:__ Django comes with a lightweight web server to facilitate end-to-end application developmnt and testing.

# Features of Django
1. __Django's Admin Interface:__
So many clients need to have a view into their application so they can manage users, data, or content on pages. Usually, the client will not be technical or have time enough to dive into the actual code and make changes.

__Django's admin interface__ is a great solution. Without any extra configuration, you get a powerful, fully-customizable, login-protected admin area that displays all of your application's data.

2. __Django has Built-in Auth:__
Django comes with built-in authentication via sessions. What if you want to use tokens? Just install the __Django REST Framework__ (DRF) library which comes with token auth.
Any authentication system you use in a Django project will also use the ORM.

3. __ORM:__
Have you ever tried to manually set up an ORM to connect your database to your application? For example, SQLAlchemy, TypeORM, or Sequelize. Even with good documentation, it's not easy. You have to get different types of queries to work, as well as migrations, seeding, and so much more.

Django provides all of that for you out of the box. Just plug in the credentials of your favorite database - Postgres, MySQL, Mongo, and so on - and Django handles the rest. You create models and interact with them via the same Python interface no matter what database you choose.

__REMARK:__ _All of the features listed so far are not exclusive to Python's Django alone. The difference is that most frameworks let you set up your own ORM, Authentication, and so on. Django does all of this with very little effort. This means that you can ship features, MVPs, and applications more quickly._
# References
1. https://www.freecodecamp.org/news/10-reasons-to-try-django-for-client-projects/