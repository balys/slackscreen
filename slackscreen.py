#!/usr/local/bin/python
from slackclient import SlackClient
import os
import time
import sys
import uuid


# Tested on MacOS Siera + iTerm2
# Set iTerm session logging location in
# iTerm->Profiles->Open Profiles->Default->[Edit Profiles]->[Session Tab]-> "Automatically log session input files in:"


######################################
sc = SlackClient('xoxp-XXXXXXXXXX-XXXXXXXXXX-XXXXXXXXXX-XXXXXXXXXX')    # Generate it from https://api.slack.com/tokens
mychannel="@yourusername"                                               # The terminal window will pop up in this channel, @user or #channel
logdir="/Users/MyUsername/iTermLogs/"                                         # Location for Iterm Logs as you set in Iterm2 Profile
bot_username="slackscreen"                                                      # User which submits the message
icon_emoji=":desktop_computer:"       
console_height=25                                                         # Amount of lines to broadcast
######################################



# We use this to identify the screen
print ""
print ""
print "Paste the command below in the terminal you would like to attach to, then wait for confirmation:"
rand_string=str(uuid.uuid4().get_hex().upper()[0:30])
print "-----------------------------"
print "  echo "+rand_string
print "-----------------------------"
print ""
print ""

not_attached=True
while not_attached == True:
  logfile=os.popen("for file in `ls -rt "+logdir+"`; do A=$(tail -2 "+logdir+"$file); if echo $A | grep -q ^"+rand_string+"; then echo $file;fi;done").read()
  log_location=(logdir+logfile).strip()
  time.sleep(1)
  if os.path.isfile(log_location):
      not_attached = False
      print "[ OK  ] Terminal "+rand_string+ " found and attached, its broadcasting to Slack now!"


updateable_message=sc.api_call(
        "chat.postMessage", channel=mychannel, text="```[Attached to terminal "+rand_string+"]```",
        username=bot_username, icon_emoji=icon_emoji
    )

message_ts=updateable_message['ts']
message_channel=updateable_message['channel']

i=0
while message_ts != "":
  try:
    message_newtext=os.popen("tail -"+str(console_height)+" " + log_location + '| sed "s,\x1B\[[0-9;]*[a-zA-Z],,g"' ).read()    
    updateable_message=sc.api_call(
        "chat.update", ts=message_ts, channel=message_channel, text="```"+message_newtext+"````")
    time.sleep(2)    
    print "[ RUNNING ] Sent updated screen no."+str(i)+" to " + mychannel + " channel. Press [CTRL+C] to Stop."
    i=i+1

  except KeyboardInterrupt:
      print "[ QUIT ] CTRL+C Pressed, deleting the slack output, exiting!"
      intial_message=sc.api_call(
      "chat.delete", channel=message_channel, ts=message_ts
      )
      sys.exit(0)
  
