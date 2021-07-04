# SSH Configuration

To create a new ssh key :

```sh
ssh-keygen -t rsa -b 4096 -C "email@example.com"
```

Save in `~/.ssh/server.key`

And in `~/.ssh/config` :

```
##
## GIT REPO HOSTS
##

Host github.com
	IdentityFile ~/.ssh/github.key

Host gitlab.com
	IdentityFile ~/.ssh/gitlab.key
```
