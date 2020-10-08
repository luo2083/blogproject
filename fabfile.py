from fabric import task
from invoke import Responder
from _credentials import github_username, github_password

def _get_github_auth_responders():
    username_responder = Responder(
        pattern="Username for 'https://github.com':",
        response='{}\n'.format(github_username)
    )
    password_responder = Responder(
        pattern="Password for 'https://{}@github.com':".format(github_username),
        response='{}\n'.format(github_password)
    )
    return [username_responder, password_responder]

@task()
def deploy(c):
    supervisor_conf_path = '/home/luo/etc/'
    supervisor_program_name = 'blogproject'

    project_root_path = '/home/luo/apps/blogproject/'

    with c.cd(supervisor_conf_path):
        cmd = 'supervisorctl -c /home/luo/etc/supervisord.conf stop {}'.format(supervisor_program_name)
        c.run(cmd)

        with c.cd(project_root_path):
            cmd = 'git pull'
            responders = _get_github_auth_responders()
            c.run(cmd, watchers = responders)

        with c.cd(project_root_path):
            c.run('/home/luo/Envspy3.6/blogprojectenv/bin/pip3 install -r requirements.txt')
            c.run('/home/luo/Envspy3.6/blogprojectenv/bin/python3 manage.py migrate')
            c.run('/home/luo/Envspy3.6/blogprojectenv/bin/python3 manage.py collectstatic --noinput')

        with c.cd(supervisor_conf_path):
            cmd = 'supervisorctl -c /home/luo/etc/supervisord.conf start {}'.format(supervisor_program_name)
            c.run(cmd)

