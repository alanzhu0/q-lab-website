# Q Lab Website
This is the official website of the TJHSST Quantum Physics and Optics Lab. It can be found at https://activities.tjhsst.edu/q-lab.

The site is built in [Django](https://www.djangoproject.com/) and deployed using [TJ Director](https://director.tjhsst.edu). It was built by @Laur04 and is maintained by the TJ Sysadmins and Q-Lab members. All questions should be directed jointy to academic-services@tjhsst.edu and mshannum@fcps.edu.

## Contributing
Bug reports, feature suggestions and pull requests are welcome.

To configure a testing environment, ensure that you have Python and pipenv installed. Then:

1. Clone this repository
```
git clone git@github.com:Laur04/q-lab-website.git q-lab-website
```

2. Enter the project directory and start the virtual environment.
```
cd q-lab-website
pipenv install
pipenv shell
```

3. Copy `qlab/settings/secret.sample` to `qlab/settings/secret.py`. If you are a member of the TJ community and would like authentication to work properly, [create an Ion OAuth application](https://ion.tjhsst.edu/oauth/applications/) using the recommended settings and replace `SOCIAL_AUTH_ION_KEY` and `SOCIAL_AUTH_ION_SECRET` with the appropriate values.

4. Migrate the database
```
python manage.py migrate
```

5. Make yourself a superuser
```
python manage.py shell
from django.contrib.auth import get_user_model
user = get_user_model().objects.get_or_create(username="<YOUR_ION_USERNAME">)[0]
user.is_superuser = True
user.is_staff = True
user.save()
```

6. Start the server
```
python manage.py runserver
```

You can now access the app by navigating to [http://localhost:8000](http://localhost:8000) in a browser of you choice.

## Production
This site is deployed on Director. If you are a current TJ student and would like to become a part of maintaining it, please contact mshannum@fcps.edu
