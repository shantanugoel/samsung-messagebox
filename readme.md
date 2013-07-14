A simply python script to send messages to Samsung TVs that can be displayed onscreen.
Developed by Shantanu Goel http://tech.shantanugoel.com/
Currently tested with Samsung 2010 C series TVs. Should work with most others as well that support this service.
Run "python samsung-msgbox.py -h" for usage instructions

usage: samsung-msgbox.py -i IP -m MSG [-p PORT] [-t TIME] [-r RECEIVER]
                         [-x RECEIVER_NO] [-s SENDER] [-y SENDER_NO] [-h]

Send an arbitrary text message to Samsung TVs which is displayed onscreen.
Developed by Shantanu Goel (http://tech.shantanugoel.com/) version 1.0

Arguments:
  -i IP, --ip IP        Required. IP Address of the TV
  -m MSG, --msg MSG     Required. Message body text to be sent to TV
  -p PORT, --port PORT  Optional. Port on which message should be sent
  -t TIME, --time TIME  Optional. Receive date and time in epoch/unix format
  -r RECEIVER, --receiver RECEIVER
                        Optional. Receiver Name
  -x RECEIVER_NO, --receiverno RECEIVER_NO
                        Optional. Receiver Number
  -s SENDER, --sender SENDER
                        Optional. Sender Name
  -y SENDER_NO, --senderno SENDER_NO
                        Optional. Sender Number
  -h, --help

![Demo 1](https://raw.github.com/shantanugoel/samsung-messagebox/master/samsung-messagebox-demo-1.jpg)
![Demo 2](https://raw.github.com/shantanugoel/samsung-messagebox/master/samsung-messagebox-demo-2.jpg)
