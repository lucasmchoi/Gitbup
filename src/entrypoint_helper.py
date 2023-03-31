import os
import yaml
import subprocess

# load and parse config.yaml
with open('/gitbup/config/config.yaml') as configf:
    configl = yaml.load(configf, Loader=yaml.SafeLoader)

# iterate over all repos in config.yaml
for repo in configl.keys():
    if configl[repo]['service'] == 'gitlab':
        gitserviceurl = configl[repo]['baseurl']
        gitrepourl = configl[repo]['repourl']
        gitreponame = configl[repo]['reponame']
        gitusername = configl[repo]['username']
        gitcredential = configl[repo]['credential']
        cronschedule = configl[repo]['schedule']
        healthcheckurl = configl[repo]['hcheckurl']
        # set url for gitlab
        gitcloneurl = 'https://gitbup:{}@{}/{}.git'.format(gitcredential,gitserviceurl,gitrepourl)

        # check if repo already exists
        if not os.path.isdir(os.path.join('/gitbup/repos', gitreponame)):
            subprocess.run(['cd /gitbup/repos && git clone {}'.format(gitcloneurl)], shell=True)
            print('Repo {} added to /gitbup/repos/{}'.format(gitreponame, gitreponame))
        else:
            print('Repo {} already existing in /gitbup/repos/{}'.format(gitreponame, gitreponame))

        # load cronfile
        with open('/var/spool/cron/crontabs/root') as cronf:
            cronc = cronf.read()
        
        # check if cron for regular pulling exists alreay in cronfile
        if '/gitbup/repos/{}'.format(gitreponame) in cronc:
            print('Repo {} git pull --all already in cronfile'.format(gitreponame))
        else:
            subprocess.run(['''echo "{} sh -c 'cd /gitbup/repos/{} && git pull --all'" >> /var/spool/cron/crontabs/root && curl -fsS -m 10 --retry 5 -o /dev/null {}'''.format(cronschedule, gitreponame, healthcheckurl)], shell=True) # 
            print('Repo {} git pull --all added in cronfile'.format(gitreponame))
    else:
        print('{} not yet supported'.format(configl[repo]['service']))
