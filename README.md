# Gitbup
Docker Container to backup private git repositories

## Use
An example docker-compose file and an example config.yaml file can be found in this repository and below.

You have to define the baseurl of the used git service (e.g. ```gitlab.com```). The credential can be a repository token.

```yaml
version: '3.3'
services:
	gitbup:
		image: ghcr.io/lucasmchoi/gitbup:latest
		container_name: gitbup
		restart: always
		volumes:
			- /Docker/config:/gitbup/config
			- /Docker/repos:/gitbup/repos
```

```yaml
repo-1:
	service: gitlab
	baseurl: gitlab.com
	repourl: username/example-1
	reponame: example-1
	username: username
	credential: example-credential-1
	schedule: "5 * * * *"
```

## Caveats

- Supports currently only gitlab

## Requirements
- [Python](https://www.python.org)
- [Pip](https://pypi.org/)
- [PyYAML](https://github.com/yaml/pyyaml)
- [Git](https://git-scm.com)

## License
Copyright © 2023 [Luca Choi](https://www.github.com/lucasmchoi)
This work is licensed under [AGPL v3](/LICENSE)