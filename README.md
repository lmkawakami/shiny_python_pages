# My shiny python pages ✨🐍📑

This is my [shiny for python][shiny] playground hosted on [github pages][github] as static stand alone pages using [py-shinylive][py-shinylive]

## Available pages:
1. [myapp][myapp] - A simple shiny app demo

## How to run locally:
1. `cd` into the chosen app directory
2. Run the following command:
```shiny run app.py```
3. Open your browser and go to [localhost:8000](http://localhost:8000/)

## How to build the app for github pages:
1. from the root directory run the following command:
```shinylive export <APP_NAME> site --subdir <APP_NAME>```
2. add a link to the app in the [README.md](README.md) file with a description
3. commit and push the changes to the repository

<!-- External Links -->
[shiny]: https://shiny.posit.co/py/
[github]: https://pages.github.com/
[py-shinylive]: https://github.com/posit-dev/py-shinylive

<!-- Local Links -->
[myapp]: https://lmkawakami.github.io/shiny_python_pages/site/myapp/index.html