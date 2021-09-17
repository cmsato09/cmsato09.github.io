---
title: Learning Django
date: 2021-09-17
modified: 2021-09-17
category: Django
tags: django
slug: 
author: cmsato09
status: published
---

<h2>Post #18 Django website building</h2>
<p>I've been building a personal Django website for the past couple of months 
or so without too much progress. The reason I started learning Django was 
because the database my workplace uses is a Django website hosted on a internal
server. I joined this project more than halfway through so I had little idea on
how the database connected to the html page and how the data was displayed, 
etc. I was tasked with creating a small application and learning how the Django
website was built. Considering the project had little organization (it should 
honestly be refactored into separate apps), I went ahead and started my own 
Django project from scratch. While building my own application and reading the 
code of the Django project workplace has been
a good exercise for me.</p>

<h3>Django tutorials</h3>
<p>I first started reading <a href="https://djangoforbeginners.com/">Django for
Beginners</a> by William S. Vincent and found that most of the things he was 
discussing was not what I wanted to do (although great to learn). This book 
covers the initial set-up, how to create an app, class-based views and 
templates, and a lot about user accounts and authorization. It didn't really 
cover the structure of Django and how the different apps connect with each 
other. It is a "follow the tutorial" style book and some of the topics seen 
here I think I would use later when I understand Django a bit more.</p>

<p>Additional resources I've used that have helped me is 
<a href="https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p">
Corey Schafer's Django tutorial series</a>, 
<a href="https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django">
Mozilla's Django tutorial</a> and <a href="https://www.djangoproject.com/">
Django's own documentation website</a>. The first two tutorials were a little 
more easier to understand and discussed how Django works. Django is an 
incredibly powerful framework and I started to think Django was basically too 
much to make something simple such as a videogame information database that I 
was planning. </p>

<h3>Dragon Warrior Monsters Database</h3>
<p>A lot of lesson videos and tutorial sites note that a personal project is 
often better at helping you learn compared to following a tutorial website 
build. I don't think making a (insert website name here) clone or a generic 
e-commerce site is bad and it's great for understanding how the websites you 
use are built, but I've read tutorial builds from coding bootcamps are viewed 
differently (sometimes unfavorably) from a job interviewer. Tutorial builds 
showcase you can follow a recipe, but it doesn't necessarily show that you know
how to use the tools. </p>

<p>I started making videogame tutorial database on 
<a href="https://en.wikipedia.org/wiki/Dragon_Warrior_Monsters" 
title="Wikipedia page">Dragon Warrior Monsters</a> (also known as Dragon Quest 
Monsters), a Gameboy game based on the famous JRPG series, Dragon Quest. The 
Dragon Quest series is an RPG where typically a party of 4 characters travel 
around the map battling monsters they encounter. Dragon Quest Monsters flips 
the script by recruiting, leveling, and breeding monsters to fight other 
monsters. Many will point out that sounds like Pokemon. The only similarity 
between the two games are recruiting and leveling up monsters. The battling 
system and leveling/breeding system are completely different. The breeding 
system is complicated and great to have a database. That is my primary 
reason of building this website -- create a database for a 23 year old game 
that no one will play or create a updated database for it. The perfect project 
for me, myself, and I.</p>
<img src="https://livedoor.sp.blogimg.jp/sylphwatch/imgs/5/a/5ae04322.jpg" alt="DQMonsters 1">

<h4>Monster database</h4>
<p>I created a monster model that shows the names (old names used in the 
original game and updated names used in later games), monster family, skills/
abilities learned, and description. I also created a breeding table model which 
shows which two monsters need to mate to get the target monster. The breeding 
table model is connected to the monster model by foreign key and I created a 
HTML page that displays both sets of information per monster.
So far, I've created a MonsterList and MonsterDetail view with 
<a href="https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-display/">
ListView and DetailView</a> to display monster model and breeding table model, 
but it looks quite ugly with basic HTML5.</p>
<img src="/images/2021_09_17_dqmscreen.png" alt="screenshot of current HTML page">

<h4>HTML5 and CSS</h4>
<p>As you can see above, I found that my lack of HTML5 and CSS knowledge is a 
bit of a problem. I started freeCodeCamp's 
<a href="https://www.freecodecamp.org/learn/responsive-web-design/">Responsive 
Web Design course</a> to learn the basics of HTML5 and CSS. That'sa post for 
another time.</p>