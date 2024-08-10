# DEPLOYMENT

## Clone repository
* To make a local copy of this project, you can clone the repository by typing the following command into your IDE terminal:

`git clone https://github.com/nhamidi90/unnie_style.git`

* Alternatively, to open the workspace in Gitpod, you can [click here](https://gitpod.io/#https://github.com/nhamidi90/unnie_style)

## Create database and Heroku app
* Create a database
* Go to the Heroku dashboard an select 'Create new app'
* Enter a unique name and select your region. Click 'Create App'.

## Connect to database and load fictures
* Inside your project, go to the settings tab and select the 'Reveal config vars' button and add the DATABASE_URL config var and paste in your database url 
* In your workspace install dj_database_url and psycopg2: 
pip3 install dj_database_url==0.5.0 psycopg2
* Freeze requirements:
pip freeze > requirements.txt
* In settings.py, add this line under import os:
* Scroll to databases and update the code:
import dj_database_url
```# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': dj_database_url.parse('your-database-url-here')
}
```

* To check you are connected you can run:
python3 manage.py showmigrations
* Migrate your database to the new database:
python3 manage.py migrate
* Load the fixtures. You will have to add the extra images manually through the admin:
python3 manage.py loaddata categories
python3 manage.py loaddata products
* Create a superuser. The email can be left blank:
python3 manage.py createsuperuser
* You need to delete your database again to prevent it form being exposed to GitHub and uncomment out the original database code. You will also need to add an if statement for when the app os runnin gp Heroku:
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

## Connect to Heroku

* Install gunicorn:
pip3 install gunicorn
* Create a Procfile with the following line. There should be no space after the line:
web: gunicorn unnie_style.wsgi:application
* Freeze requirements again
pip freeze > requirements.txt
* In the terminal, log into Heroku:
    Log in to your Heroku account and go to Account Settings in the menu under your avatar.
    Scroll down to the API Key and click Reveal
    Copy the key
    In the Gitpod terminal, run heroku login -i
    Paste in your API key when asked
* Temporarily disable collect static:
heroku config:set DISABLE_COLLECTSTATIC=1 --app unnie-style
* Update the hostname of your Heroku app to ALLOWED_HOSTS in settings.py
* Commit and push to GitHub
* Go back to you pp on Heroku and from the deply tab select connect to GitHub. Select your repository
* In the setting tab, add a new config var: SECRET_KEY. Generate a secret key and paste it in
* In your project setting.py, replace the secret key variable:
SECRET_KEY = os.environ.get('SECRET_KEY', '')

## Connect to AWS

### Create S3 bucket
* Create an AWS account and go to S3
* Create a new bucket. Uncheck 'block all public access' and make sure under Object Ownership that 'ACLS enabled' is selected. 
* On the Properties tab, scroll down to 'static web hosting'. Set the home/default page to 'index.html' and error link as 'error.html', then save.
* On the Permissions tab, paste the following into the Cross-origin resource sharing (CORS) section
```
[
    {
        "AllowedHeaders": [
        "Authorization"
        ],
        "AllowedMethods": [
        "GET"
        ],
        "AllowedOrigins": [
        "*"
        ],
        "ExposeHeaders": []
    }
]
```
* On the Bucket Policy tab, copy the ARN and select 'policy generator'. Add these settings:
policy type: 'S3 bucket policy'
principal: *
Actions: GetObject
Paste in the ARN into the ARN Field
* Click add statement then generate policy, and copy this policy into the Bucket policy editor.
* Before you save, add /* in Resource to allow access to all resources in this bucket. Click save
* Go to the Access control list (ACL) tab, click edit and enable List for Everyone under the public access section.

### Creat IAM
* Open up IAM on your AWS account, click 'User Groups' and create a new group 
* Go to 'Policies' then 'Create Policy'. Open the JSON tab then select 'Import managed policy'
* Seach S3 then import S3 full access policy
* Get the ARN from your S3 bucket policy page and paste it under 'Resource' so it looks similar to this:
```
"RESOURCE": [
   "arn:aws:S3....",
   "arn:aws:S3..../*",
]
```
* Click review policy. Give it a name and description. Create policy
* Attach the policy to the group:
* Click 'User Groups and go to the permissions tab. Open 'Attach permissions' dropdown, search for your policy name and click 'Attach policies'
* On the users page click 'Add user'. Enter a name and give them progrmamatic access. Select Next.
* Add the user to the group by clicking through to the end.
* Now you need to create a CSV file. Select the user for whom you wish to create a CSV file.
* Select the 'Security Credentials' tab and scroll to 'Access Keys' and click 'Create access key'
* Select 'Application running outside AWS', and click next
* On the next screen, you can leave the 'Description tag value' blank. Click 'Create Access Key' then click the 'Download .csv file' button

## Connect Django to S3

* In your workspace, install boto3 and django-storages:
`pip3 install boto3`
`pip3 install django-storages`
* Freeze requirements.txt
`pip freeze > requirements.txt`
* In settings.py under INSTALLED_APPS, add 'storages',
* Update AWS_STORAGE_BUCKET_NAME and AWS_S3_REGION_NAME to match your own
* Go to heroku and add config vars for 
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
USE_AWS and set it to True
You can find these in the csv file you downloaded
* Also remove the DISABLE_COLLECTSTATIC variable
* Commit and push to GitHub. You should see a static folder in your S3 bucket, and your static files being rendered on the live site.

## Add media files, and connect to Stripe

* Go to S3 and create a new folder called 'media'. Add your media files
* Click next then under 'manage public permissions', grant public read access to these objects. Upload.
* In Heroku config vars add the variables for:
STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY
STRIPE_WH_SECRET
You can get these from Your Stripe account under 'Developers' > 'API Key'
* In Stripe, create a new webhook endpoint by going to the webhooks tab, 'Add endpoint'
* Add your Heroku URL followed by /checkout/wh/
* Select receive all eevents, add endpoint
* Copy the Signing secret and add to Heroku variable STRIPE_WH_SECRET

## Sending emails using gmail

* Create a gmail account and turn on 2 step verification
* Scroll down and tou will see the App passwords section.
* Type a name for your app and copy the password
* In Heroku add the variables for EMAIL_HOST_PASS, pasting in the password and EMAIL_HOST_USER, adding in your email address 