# Personal Website

Pretty self explanatory. Making it in Django was overkill, since for now the entire thing is statically built with `django-bakery` ¯\\_(ツ)_/¯

Requires python and npm to be installed.

## init
- copy `.env.template` into a new `.env` and update the variables. Set debug to `True` for local dev.
- `make init`

## run it
- django server: `make runserver` OR static build server: `make bakeserver`
- tailwind watch: `make tailwindwatch`
- formatting: `make format` and lint check: `make lint`

## build it
- add views to be statically baked to `settings.py` >> `BAKERY_VIEWS` (they must be class-based views which inherit from `django-bakery` views, separate from your django class-based views)
- update `BUILD_DIR` in your `.env`. Defaults to `<PROJECT_ROOT>/build` in `settings.py`. This will also collect all of your static files in the build folder.
- to bake into static html, run `make bake`.
