title: Wrestling with Pelican part 1
date: 2021-01-22
modified: 2021-01-23
category: pelican
tags: pelican,
slug: pelican-struggle
author: cmsato09
status: published

## Post #13 Setting up Pelican
After finallly understanding what was wrong with how I was using the virtual environment, I thought it wouldn't be too difficult getting this pelican blog up and running. I was wrong.

### Pelican quickstart with v4.5.4
Installing pelican wasn't too difficult and the [pelican documentation](https://docs.getpelican.com/en/4.5.4/index.html) is pretty straight-forward. There are many websites that show how to quickly get a basic pelican static page up and running like this [step-by-step guide](https://medium.com/@acalamea/step-by-step-guide-to-setup-a-web-site-using-pelican-and-gitpages-5de976ae44cb) and [getting started guide](https://opensource.com/article/19/1/getting-started-pelican). More resource list at [Full Stack Python's pelican blog post](https://www.fullstackpython.com/pelican.html).

This blog post mainly covers some of the problems I encountered and how the start-up went. I will link sources to show what directions I followed. 

Typing `pelican-quickstart` in the terminal after installing pelican starts the project creation which asks some questions and sets up the initial skeleton files in the project folder. 
> Welcome to pelican-quickstart v4.5.4.
>
> This script will help you create a new Pelican-based website.
>
> Please answer the following questions so this script can generate the files needed by Pelican.
>
> Where do you want to create your new web site? [.]<br>
> What will be the title of this web site? Novice Programmer Journey from Zero<br>
> Who will be the author of this web site? cmsato09<br>
> What will be the default language of this web site? [English]<br>
> Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) n<br>
> Do you want to enable article pagination? (Y/n) Y<br>
> How many articles per page do you want? [10] 10<br>
> What is your time zone? \[Europe/Paris\] US/Pacific<br>
> Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) Y<br>
> Do you want to upload your website using FTP? (y/N) N<br>
> Do you want to upload your website using SSH? (y/N) N<br>
> Do you want to upload your website using Dropbox? (y/N) N<br>
> Do you want to upload your website using S3? (y/N) N<br>
> Do you want to upload your website using Rackspace Cloud Files? (y/N) N<br>
> Do you want to upload your website using GitHub Pages? (y/N) y<br>
> Is this your personal page (username.github.io)? (y/N) y<br>
> Done. Your new project is available at C:\filepathway<br>

I didn't understand most of these questions, but this blog post from [Archer Imagine](http://archerimagine.com/articles/pelican/helloworld-pelican-quickstart.html) covers what the questions mean. There are some descrepancies with the article due to being a different version of pelican. 
Once you answer the questions, the following files and folders are generated. Folder hierarchy copied from [here](https://docs.getpelican.com/en/latest/install.html#kickstart-your-site) in the documentation.

> project_folder/<br>
> |-- content<br>
> |-- output<br>
> |-- tasks.py<br>
> |-- Makefile<br>
> |-- pelicanconf.py<br>
> |-- publishconf.py<br>

The content folder is where you save your markdown or reStructuredText files.<br>
The output folder is where the html files are generated, which are then used to publish your website. pelicanconf.py is an important file that configures how your website looks.<br>
I'm actually not sure what the tasks.py, Makefile, and publishconf.py files do since I have't touched them. At the moment, pelicanconf.py is the really important file. You will have to generate your own .gitignore, readme.mk, requirement.txt, etc. 

This blog post gets quite long so I've divided it. Continue to part 2