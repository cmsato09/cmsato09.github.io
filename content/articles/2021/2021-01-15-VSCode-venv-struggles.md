title: VSCode venv struggle
date: 2021-01-15
modified: 2021-01-17
category: VSCode
tags: VSCode, pelican,
slug: venv-struggle
author: cmsato09
status: published

## Post #12 Making a virtual environment in VSCode

I was attempting to get [Pelican static site generator](https://blog.getpelican.com/) to work on VSCode so I could move this blog to a static site that I put together (put together as in 'I set-up and didn't fork over from Github'). 

## Planning to move static sites
The Jekyll website this blog is currently on uses [Jekyll-Now](http://www.jekyllnow.com/). The advantage of using Jekyll-Now that drew me to it in the first place was the promise of 'eliminating up front set-up.' In the description of Jekyll-Now they say you don't need to use the command line or install/configure ruby and promised of having a blog in no time. You can also host Jekyll on Github pages and control most of your content and license compared to blogging website like Wordpress. Github pages is free to host so you don't have to worry about paying for a domain name. So from what I gathered from reading, it was good for a programming beginner to start a blog while learning and Github pages was free to use that didn't give away too many rights like for Wordpress. 

Although Jekyll-Now had been good for the eleven posts I have, I wanted to be able to customize this blog a bit more. Therefore, I'm building one from scratch. Since I'm still working with Python, I went with Pelican. Simple as that. From what I've read at this point, it looks like Jekyll and Pelican are equal with customizability and ease of use, but I just wanted to use a framework that uses my preferred language.

## venv problem
Back to the problem I pointed out in the title, I was having problems with using the venv file I made for the Pelican website folder. I would create my virtual environment in the folder I wanted using git bash using `py -m venv venv` and then opened the folder in VSCode. I then started the `pelican-quickstart` guide and got all the necessary files into the project folder. After looking through some of the python files that the pelican quickstart generated, I noticed that the task.py file needed the [invoke](http://www.pyinvoke.org/) library. I go ahead and try `pip install invoke` in the terminal in VSCode and it worked, but I notice the VSCode was still marking invoke as not imported. I didn't understand why it wasn't working until I realized the terminal wasn't using the virtual environment python.exe and running python from the global folder usually found in C:\Users\username\AppData\Local\Programs\Python\Python39 (this [youtube video](https://www.youtube.com/watch?v=CQDQWHnCqOE) also helped me realize the global folder problem). I had pip install invoke in the global folder and pelican wasn't even in the venv library! That took awhile to figure out and probably obvious to any vetran programmer who set-up a lot of virtual environments. Always read the terminal output message to figure out what is going on is the key take away message. 

### Activating the venv on VSCode
I read that you must 'activate' the environment using the terminal from [VSCode documentation](https://code.visualstudio.com/docs/python/environments) and it still didn't click with me. I did figure out how to select the python interpreter, but it still didn't work (I kept checking if the terminal used the virtual environment with `pip list` to see if it still pointed to the global python folder). I went and searched for a tutorial to see if there was a dumbed down version of VSCode documentation and found a [django tutorial](https://rasulkireev.com/django-venv/). This tutorial states to activate the venv, type `.\venv\scripts\activate.bat`. Lo and behold there is a activate.bat file in the directory, however, the terminal still spits out a error. 

>File C:/Users/username/ssg_pelican_blog/venv/Scripts/activate.ps1 cannot be loaded because running scripts is disabled on this system.

I found on [stackoverflow](https://stackoverflow.com/questions/56199111/visual-studio-code-cmd-error-cannot-be-loaded-because-running-scripts-is-disabl) via searching the error message, which cites this [github issue](https://github.com/Microsoft/vscode-python/issues/2559#issuecomment-478381840) on how to fix this VSCode problem. You have to edit the settings.json file to include the following line:
```
"terminal.integrated.shellArgs.windows": ["-ExecutionPolicy", "Bypass"]
```
At this point, I'm just ready for this problem to be solved and wasn't concerned about why this occurs. After adding the line in the setttings.json file and restarting VSCode, I was able to see a green (venv) in the terminal signalling that I was indeed using the virtual environment instead of the global python file. 

## To summarize
When you can't use your virtual environment in VSCode terminal, do the following

1. Double check if you are actually using your venv folder by typing `pip list` in the terminal. If you recently made your virtual environment, it shouldn't have many packages. If are a lot of packages installed, you are probably in the global python folder.

2. type in the terminal `.\venv\Scripts\activate` if on Windows to activate virtual environment. 

3. If message 'running scripts is disabled on this system' pops up, add `"terminal.integrated.shellArgs.windows": ["-ExecutionPolicy", "Bypass"]` into the settings.json file. Settings.json file can be accessed using the Command Palette located in the View tab (or Ctrl+Shift+p) and searching for 'settings json', then select 'Preferences: Open Settings (JSON)'. 

4. Close VSCode and restart the program. Run `.\venv\Scripts\activate` again in the terminal. A green '(venv)' should appear in the terminal.
