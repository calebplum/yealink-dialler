# yealink-dialler
Yealink-dialler is a Python interface to send commands to Yealink IP phones. It was written in early 2016 and is is untested on firmware released since then. It performs the following functions:

1. Dial telephone numbers
2. Answer incoming calls
3. Hang up in-progress calls
4. Mute/Unmute in-progress calls


## Compatibility
This script was written for the Yealink SIP-T22P but should work without modification with the following models:

- T20 / T20P
- T21P
- T22 / T22P
- T23 / T23P / T23G
- T26 / T26P
- T27P
- T28P
- T29G
- T32G
- T38G
- T40P
- T42G

It should also work after minor modification with most other Yealink IP phones which support Action URI's. See [this Yealink article](http://support.yealink.com/faq/faqInfo?id=565) for info about Action URI's.

If you find that it works with any other models please let me know.


## Usage
Setup is simple. Fill in the phone's details in the variables at the top of the script. The Internal Parameters section does not need to be modified. Make sure your phone is configured to allow Action URI calls from your computer, this can be done in the phone's web interface in Features > Remote Control.
