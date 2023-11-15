# Command line for the win

## Background Context

[CMD CHALLENGE](https://cmdchallenge.com/) is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It’s a good training to improve your command line skills!

## Tasks

0. [0-first_9_tasks.png](0-first_9_tasks.png) The first 9 tasks.
1. [1-next_9_tasks.png](1-next_9_tasks.png) The next 9 tasks to complite 18 tasks.
2. [2-next_9_tasks.png](2-next_9_tasks.png) The last 9 tasks to attain the 27 tasks in total.

## Move the ``screenshots``

1. Connect to the sandbox, by using that `link` and `password` provided to you for the sandbox environment.

```bash
sftp user_name@your_server_ip_or_remote_hostname
```

2. Navigate to the directory where you want to upload the screenshots.

```bash
lcd ./Picture/Screenshots
```

3. Upload the screenshots.

```bash
put ./* /root/alx-system_engineering-devops/command_line_for_the_win/
```
