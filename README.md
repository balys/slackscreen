# slackscreen
A tool to tail output of your iTerm2 session to slack channel.


This works with Iterm2 https://www.iterm2.com
This was only tested on MacOS Siera.

You need to enable iTerm2 session logging in:
iTerm->Profiles->Open Profiles->Default->[Edit Profiles]->[Session Tab]-> "Automatically log session input files in:"

Then in one iterm session launch the slackscreen tool. This will generate an echo command you need to paste into the session you want to broadcast.
You can paste it to any existing session (in screen, remote SSH'ed, etc.)

````
~/dev/slackscreen$ ./slackscreen.py


Paste the command below in the terminal you would like to attach to, then wait for confirmation:
-----------------------------
  echo 6FFC7BA1E7E2464DA2815B9301540E
-----------------------------


[ OK  ] Terminal 6FFC7BA1E7E2464DA2815B9301540E found and attached, its broadcasting to Slack now!
[ RUNNING ] Sent updated screen no.0 to #verycool channel. Press [CTRL+C] to Stop.
[ RUNNING ] Sent updated screen no.1 to #verycool channel. Press [CTRL+C] to Stop.
^C[ QUIT ] CTRL+C Pressed, cleaning up!
````

As you see it will broadcast the output until your press CTRL+C, then it will also delete the message in slack completely.


![Running in Slack gif](https://github.com/balys/slackscreen/raw/master/readmefiles/slackscreen_example.gif)