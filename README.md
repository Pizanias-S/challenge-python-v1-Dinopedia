# GlobalWebIndex Python Challenge - v1 | Exercise: DinosaursAficionado

### Acknowledgments 
The Dino project first started as a technical assignment for an interview with GWI so base idea of the project came
from GWI. Everything after the base idea was created by me (except the poetry file).

### Deployment
The application has been deployed in AWS Elastic Beanstalk with the static files been handled from Elastic Beanstalk,
because unfortunately my free tier account was not able to handle the AWS S3 storage without charging me.

The database that was used is PostgreSQL deployed in AWS RDS. 

[Click me to see the site!](http://djangodinopediablog-env.eba-umebnduf.eu-south-1.elasticbeanstalk.com/)

### Admin
As an admin you can add a kind of dino with his attributes (Name, Eating Class, Period, 
Size, Color, Author and up to 2 images for each dino)

![Dino Admin](dino_admin.jpg)

You have the ability to review, adjust and delete all the existing dinos their attributes
and the comments made by users.

![Dino Admin 2](dino_admin_2.jpg)

I created some test dinosaurs feel free to fidle with everything you want.

### Dinopedia

There is a main page with a Favorites, All Posts and a search bar function.

![Dino View Main](dino_view_main.jpg)

In the All Posts page you can see all the dinos and click on them

![Dino View All](dino_view_posts.jpg)

Each dino has a unique slug that is autogenerated from its name and used for identification and the url.
You can see the imformation for each dino.

![Dino View Post](dino_view_post.jpg)

There is a Comments section for each dino with some test comments, every user can comment on a post.

![Dino View Post Comment](dino_view_post_comment.jpg)

Each user can add some dinos to his favorites and view them as a list.

![Dino View Favorites](dino_view_favorites.jpg)

There is a search bar to search for different kinds of dinos.

![Dino View Search](dino_view_search.jpg)

### Database Diagram

![Diagram for the dino Database](dino_db.jpg)

### Contact
If you have any questions don't hesitate to contact me at <s.pizanius@gmail.com>

