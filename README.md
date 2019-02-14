# training-servers

Tools for administering training servers, and dockerfiles defining training servers.


## usermaker.py

This is a script to create a script to create a set of guest users. Usage is

```
python3 usermaker.py myworkshop 40
```

This will create a script `myworkshop_create.sh` to create 40 users, `myworkshop_destroy.sh` to destroy them and `myworkshop.html` containing account names and passwords that can be printed out. One thing the creation script doesn't do is create symbolic links to course material in the user's directory. Need to use Kirill's script to do this:

```
sudo bash myworkshop_create.sh
sudo /home-local/kirill/bio-ansible/scripts/bash/link_R_data.bash
# ... run workshop ...
sudo bash myworkshop_destroy.sh
```

Note at the end of `myworkshop_create.sh` there is `rstudio-server restart`. This is because RStudio can become confused if a user is destroyed and then a new user with the same name created.

Another thing to remember: If for some reason someone has logged into RStudio in a way that is broken and with no way to sign out and try a different account, get them to go to

https://.../rstudio/auth-sign-in


## R workshop Docker image

Directory "docker" contains files for creating a Docker image for running an R workshop.

The built image is currently available on Docker Hub as [paulfharrison/rworkshop](https://cloud.docker.com/u/paulfharrison/repository/docker/paulfharrison/rworkshop).

Set environment variable PASSWORD to a suitable password. Expose port 8787. Connect to http://[IP-address]:8787 with a web browser, and log in as "rstudio" with the password you specified. You will then see a list of freshly generated guest accounts available as CSV and HTML files.

Within the instance, you can symlink a file or directory into all user's home directory with `sudo ./share <filename>`. For example you could do:

```
git clone https://github.com/MonashDataFluency/r-intro-2.git
sudo ./share r-intro-2/r-intro-2-files
```

R packages installed as the `rstudio` user are available to all users.