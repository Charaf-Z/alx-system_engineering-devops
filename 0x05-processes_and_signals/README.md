# 0x05 Processes and signals

## Tasks

0. Script that displays its own PID.
1. Script that displays a list of currently running processes.
2. Script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process.
3. Script that displays the PID, along with the process name, of processes whose name contain the word `bash`.
4. Script that displays `To infinity and beyond` indefinitely.
5. Script that kills `4-to_infinity_and_beyond process`.
6. Script that that kills `4-to_infinity_and_beyond process`. v2
7. Script that displays `To infinity and beyond` indefinitely with a `sleep 2` in between each iteration `I am invincible!!!` when receiving a `SIGTERM` signal.
8. Script that kills the process `7-highlander`.
9. Script that creates the file `/var/run/holbertonscript.pid` containing its PID and:
   * Displays `To infinity and beyond` indefinitely.
   * Displays `I hate the kill command` when receiving a `SIGTERM` signal.
   * Displays `Y U no love me?!` when receiving a SIGINT signal.
   * Deletes the file `/var/run/myscript.pid` and terminates itself when receiving a `SIGQUIT or SIGTERM` signal.
10. Script that indefinitely writes `I am alive!` to the file `/tmp/my_process`.
11. C program that creates 5 zombie processes.
