# Deployment

Code Institute provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser. This is to improve the accessibiltiy of the project to others.

The live deployed application can be found at [Snakes andLadders](https://snakes-and-ladders-sw.herokuapp.com/).

[Return to README.md](README.md)

## Local Deployment
*Gitpod* IDE was used to write the code for this project.

To make a local copy of this repository, you can clone the project by typing the follow into your IDE terminal:
- `git clone https://github.com/StevenWeir038/Snakes-and-Ladders.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/StevenWeir038/Snakes-and-Ladders)

## Heroku
It is recommended to deploy as soon as practicible to faciliate regular testing.

This project uses [*Heroku*](https://www.heroku.com/about), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment to the platform can feel complex for a first time user so do as follows after account setup:

Within your personal area select *New* in the top right corner and select *Create new app* from the drop down menu.

![Create-new-app](docs/readme/heroku-deployment/heroku-create-new-app.png "Create new app")

Give your app a name, set where you reside and then select *Create app*. For example:

![Create-new-app-name](docs/readme/heroku-deployment/heroku-create-new-app-name.png "Create new app name")

In the menu of your newly created project select *Settings*.

![Personal-menu](docs/readme/heroku-deployment/heroku-personal-menu.png "Personal menu")




Select *Reveal Config Vars*.

![Reveal-config-vars](docs/readme/heroku-deployment/heroku-personal-reveal-config-vars.png "Reveal config vars")

In the *Config Vars* section of the *Settings* page, expose the necessary port by setting the value of KEY to `PORT` and the value to `8000`.  

![Config vars](docs/readme/heroku-deployment/heroku-config-vars.png "Config vars")

To install/support dependancies select *Add buildpack*.
The order of the buildpacks is important, select `Python` first then `Node.js` second. If they are not in this order, you can click and drag them in the buildpacks section to rearrange.

Make sure to save your changes once each pack is selected.

![Buildpack-2](docs/readme/heroku-deployment/heroku-buildpack-2.png "Buildpack-2")
![Buildpack-1](docs/readme/heroku-deployment/heroku-buildpack-1.png "Buildpack-1")



To deploy, scroll to the top menu and select *Deploy*.

In the *Deployment method* section of the *Deploy* page look for the *GitHub* icon and select *Connect to GitHub*.

![Deployment-method](docs/readme/heroku-deployment/heroku-deployment-method-github.png "Deployment method")

In the *Connect to GitHub* section of the *Deploy* page type a unique repository name.  For example the name is `snakes-and-ladders-sw` as set in the Create app page.

Select *Search*.  If the repository is found select *Connect*.

![Deployment-method](docs/readme/heroku-deployment/heroku-deployment-method-github-name.png "Deployment method")

![Confirm-deployment](docs/readme/heroku-deployment/heroku-deployment-github-confirm.png "Confirm deployment")
