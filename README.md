# Instagram-clone

## Build by [Kolem Edwin]

## Description

This is an Instagram clone where people share their images and videos for other users to view. Users can sign up, login, view and post photos, search and follow other users.

## Screenshot images

<img src="static/../instagram/static/images/Screenshot%20from%202021-10-17%2016-22-48.png">

<img src="static/../picts/static/img/home.png">
<img src="static/../picts/static/img/Screenshot%20from%202021-10-10%2022-16-50.png">

## Live page

https://github.com/edwinkipchumba/instagram-clone

## User stories

Users would like to:

1. Sign in to the application to start using.
2. Upload my pictures to the application.
3. See my profile with all my pictures.
4. Follow other users and see their pictures on my timeline.
5. Like a picture and leave a comment on it.

## Behaviour Driven Development (BDD)

| Behaviour | Input | Output |
| :-----------------| :-----------------: | ------------------: |
| Admin Authentication | On demand | Access Admin dashboard |
| User Authentication | On demand,Verify emails before proceeding | Access Admin dashboard |
| Display all images with comments and likes | Home page | Clickable links to open any images in a model |
| Display single images on model | On click | All details should be viewed |
| To add an image | Through Admin dashboard and homepage | Click on add and upload respectively |
| To edit image | Through Admin dashboard | Redirected to the image form details and editing happens |
| To delete an image | Through Admin dashboard | click on image object and confirm by delete button |
| To search | Enter text in search bar | Users can search by username |
| View other users profiles via story menu bar | Click username on stories navigation | Users can view all images posted by any user |
| Comment on images | Add comments below respectively image | Users can add comments on any image |
| Like images | Add likes to an image | Users can add likes to images they like |

## Setup | Installation Requirements

1. python3.8
2. virtualenv
3. requirements.txt
4. django3.2.8

## Cloning

* Open Terminal {Ctrl+Alt+T}

```
$git clone https://github.com/edwinkipchumba/instagram-clone

```
```
$cd instagram-clone
```

* open based on the text editor you have.

## Running the Application

* Creating the virtual environment

 ```
$ python3 -m venv --without-pip virtual
```

```
$ source virtual/bin/activate
```

$ curl https://bootstrap.pypa.io/get-pip.py | python

* Install Django Dependencies

```
$ pip install -r requirements.txt
```

## Setup Database

* setup your database User,Password, Host then make migrations

```
$ python manage.py makemigrations
```

## Now migrate

```
$python manage.py migrate
```

* To run the application, in your terminal:

$ python3 manage.py runserver

## Technology used

* django3.2.8 and postgresql
* HTML5
* CSS
* Bootsrap3
* python3.8

## Known Bugs

If you find a bug, kindly feel free to comment an issue here and inlcude their corresponding results.

## Contact  Information

 Feel free to contact me incase of any issue or questions, ideas and concern towards the same.

* Contact Number:+254728357619
  
* E-Mail: edwinkolem5@gmail.com.

## License

https://github.com/edwinkipchumba/instagram-clone/blob/master/LICENSE