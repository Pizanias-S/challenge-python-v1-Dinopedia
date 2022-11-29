# GlobalWebIndex Python Challenge - v1 | Exercise: DinosaursAficionado

### Deployment
The application has been deployed in AWS Elastic Beanstalk with the static files been handled from Elastic Beanstalk,
because unfortunately my free tier account was not able to handle the AWS S3 storage without charging me.

The database that was used is PostgreSQL deployed in AWS RDS. 

[Click me to see the site!](http://djangodinopediablog-env.eba-umebnduf.eu-south-1.elasticbeanstalk.com/)

### Problems
I had some issues with Docker and because I have very limited time I was not able to solve them so Docker was not used
for the project, moreover for the same reasons the testing is not as extensive as it should be.


### Admin
As an admin you can add a kind of dino with his attributes (Name, Eating Class, Period, 
Size, Color, Author and up to 2 images for each dino)

![Dino Admin](dino_admin.jpg)

I created some test dinosaurs feel free to fidle with everything you want.

### Dinopedia

I added a Comments section for each kind of dinosaur with some test comments.

Each dino has a unique slug that is autogenerated from its name and used for identification and the url.

### Database Diagram

![Diagram for the dino Database](dino_db.jpg)

### Contact
If you have any questions don't hesitate to contact me at <s.pizanius@gmail.com>

---

Create a Python application for Dinosaurs Aficionados which is going to be used to maintain and provide various information about all kinds of Dinosaurs.

As an application administrator you’d like to have the ability to :
* Add a kind of dinosaur 
  * Name
  * Eating classification e.g [herbivores, omnivores, and carnivores]
  * Typical Colour
  * Period they lived e.g [triassic , jurassic, cretaceous, paleogene, neogene]
  * Average Size e.g [tiny, very small, small, medium, large, very large etc]).
* Remove a kind(s) of dinosaur(s)
* Associate up to 2 images with each dinosaur
* Remove image(s) 

As a developer you’d like to Integrate with the application and have the ability to : 
* Find all the available kinds of dinosaurs
* Search for a particular kind and get their images
* Like your favourite (Optional)
* See your favourites (Optional)

We would like you to try and present a well written solution that will cover the above criteria. Utilising the following points
* Python 3.*
* Django (_Current repo uses a django template. Feel free to restructure if your solution is based on anything else like flask/fast api etc_)
* Database integration (Postgres or any equivalent)
* Docker
* Testing suite
* README

Get creative as much as you want, we WILL appreciate it. You will not be evaluated based on how well you follow these instructions, but based on how sensible your solution will be. In case you are not able to implement something you would normally implement for time reasons, make it clear with a comment.

# Submission
Just create a private repo out of this and send invites to collaborate/review on the following emails <cbekos@gwi.com> / <tvesela@gwi.com> / <zmaxa@gwi.com> / <ecechal@gwi.com>
