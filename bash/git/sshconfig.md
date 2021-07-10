# SSH Configuration

To create a new ssh key :

```sh
ssh-keygen -t rsa -b 4096 -C "email@example.com" -f ~/.ssh/server.key
```

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

## HTTPS

If however, you are only cloning one repo from a new server for a temporary use, creating a SSH key can be useless. You can reuse SSH keys, or you can rely on a HTTPS link to clone this specific repo.

Using an HTTPS link requires to enter the credentials every time you push to the server, which can be bothersome. Some techniques rely on [Git Credential Storage](https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage) to store credential instead of entering them every time.

Otherwise, there is also a method that :warning: is not recommended :warning: as it stores the credentials directly into the remote url :

```
https://username:password@gitlab.example.com/group/repo.git
```

