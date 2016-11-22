from fabric.api import *

# add SSH Config at Local Host File
env.use_ssh_config = True
env.activate = 'source venv/bin/activate && source .env'


def install():
    run('rm -rf YongsanDist')
    run('git clone https://github.com/DanielTimLee/YongsanDist')
    with cd('~/YongsanDist/'):
        run('virtualenv --python=python3 venv')
        with prefix(env.activate):
            run('pip install -r requirements.txt')
            run('bower install --allow-root')
            run('python server.py')


def deploy():
    with cd('~/YongsanDist/'):
        run('git checkout master')
        run('git pull origin master')
        with prefix(env.activate):
            run('pip install -r requirements.txt')
            run('bower install --allow-root')


def register_upstart():
    sudo('rm -f /etc/init/yongsandist.service')
    sudo('ln -s /home/ubuntu/yongsandist/yongsandist.upstart.service /etc/init/yongsandist.upstart')
    sudo('initctl reload-configuration')


def start():
    sudo('initctl start yongsandist.upstart')


def stop():
    sudo('initctl stop yongsandist.upstart')


def status():
    sudo('initctl status yongsandist.upstart')


def proxy_start():
    sudo('service nginx start')


def proxy_stop():
    sudo('service nginx stop')
