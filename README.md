
** Steps

 * urls.py inside app (named routes)
 * urls.py inside project (include function)
 * Database config: (project settings.py)
 * Create models
 * Add app to installed apps
 * Create migration: $ python manage.py makemigrations gallery
 * View generated code: $ python manage.py sqlmigrate gallery 0002
 * Apply migration: $ python manage.py migrate
 * Check tables created by additional apps
 * Create user for admin: $ python manage.py createsuperuser
 * Login to admin site
 * Make app models modifiable by admin (View admin.py in app root)
 * Check ORM API to query all
 * Check templates system (Names specification, )
 
run: pip install -r requirements.txt