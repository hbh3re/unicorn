import os
from invoke import task

HERE = os.path.dirname(os.path.abspath(__file__))
API = os.path.join(HERE, 'mysite')


@task
def test_all(ctx):
    pep8(ctx)
    test_api(ctx)
    # TODO: add more as they become available

# PYTHON
@task(aliases=['flake8'])
def pep8(ctx, echo=True):
    ctx.run('pep8 {} {}'.format(API, "--ignore=E402,E501"), echo=echo)


@task
def api_server(ctx):
    ctx.run('python {}/manage.py runserver'.format(API), echo=True)


@task
def test_api(ctx):
    ctx.run('python {}/manage.py test {}'.format(API, API), echo=True, pty=True)


@task(aliases=['req'])
def requirements(ctx):
    ctx.run('pip install -r requirements.txt', echo=True)