#!/usr/bin/python
# Developed by Shantanu Goel. http://tech.shantanugoel.com/

import socket
import argparse
import time

#Defaults
port        = 52235
receiver_no = "1234567890"
sender_no   = "1234567890"
receiver    = "Receiver"
sender      = "Sender"
epochtime   = time.mktime(time.localtime())

def buildMessage(args):
  body = "<?xml version=\"1.0\" encoding=\"utf-8\"?>" + "<s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\">" + "<s:Body>" + "      <u:AddMessage xmlns:u=\"urn:samsung.com:service:MessageBoxService:1\">" + "         <MessageType>text/xml</MessageType>" + "         <MessageID>MessageId</MessageID>" + "<Message>" + "&lt;Category&gt;SMS&lt;/Category&gt;" + "&lt;DisplayType&gt;Maximum&lt;/DisplayType&gt;" + "&lt;ReceiveTime&gt;" + "&lt;Date&gt;" + time.strftime('%Y-%m-%d', time.localtime(args.time)) + "&lt;/Date&gt;" + "&lt;Time&gt;" + time.strftime('%H:%M:%S', time.localtime(args.time)) + "&lt;/Time&gt;" + "&lt;/ReceiveTime&gt;" + "&lt;Receiver&gt;" + "&lt;Number&gt;" + args.receiver_no + "&lt;/Number&gt;" + "&lt;Name&gt;" + args.receiver + "&lt;/Name&gt;" + "&lt;/Receiver&gt;" + "&lt;Sender&gt;" + "&lt;Number&gt;" + args.sender_no + "&lt;/Number&gt;" + "&lt;Name&gt;" + args.sender + "&lt;/Name&gt;" + "&lt;/Sender&gt;" + "&lt;Body&gt;" + args.msg + "&lt;/Body&gt;" + "</Message>" + "      </u:AddMessage>" + "   </s:Body>" + "</s:Envelope>";

  host = socket.gethostname()
  length = len(body)
  header = "POST /PMR/control/MessageBoxService HTTP/1.0\r\n" + "Content-Type: text/xml; charset=\"utf-8\"\r\n" + "HOST: " + host + "\r\n" + "Content-Length: " + str(length) + "\r\n" + "SOAPACTION: \"uuid:samsung.com:service:MessageBoxService:1#AddMessage\"\r\n" + "Connection: close\r\n" + "\r\n"
  message = header + body
  print message

  return message

def sendMessage(args, message):
  s    = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
  s.connect((args.ip, args.port))
  sent = s.send(message)
  if (sent <= 0):
    print("Error Sending Message")
    s.close()
    return
  recv = s.recv(100000)
  print recv
  s.close()

def main():
  parser = argparse.ArgumentParser(description='Send an arbitrary text message to Samsung TVs which is displayed onscreen. Developed by Shantanu Goel (http://tech.shantanugoel.com/) version 1.0', add_help = False)
  flags = parser.add_argument_group('Arguments')
  flags.add_argument('-i', '--ip', dest = 'ip', default = None, help = 'Required. IP Address of the TV', required = True)
  flags.add_argument('-m', '--msg', dest = 'msg', default = None, help = 'Required. Message body text to be sent to TV', required = True)
  flags.add_argument('-p', '--port', dest = 'port', default = port, type = int, help = 'Optional. Port on which message should be sent')
  flags.add_argument('-t', '--time', dest = 'time', default = epochtime, type = float, help = 'Optional. Receive date and time in epoch/unix format')
  flags.add_argument('-r', '--receiver', dest = 'receiver', default = receiver, help = 'Optional. Receiver Name')
  flags.add_argument('-x', '--receiverno', dest = 'receiver_no', default = receiver_no, help = 'Optional. Receiver Number')
  flags.add_argument('-s', '--sender', dest = 'sender', default = sender, help = 'Optional. Sender Name')
  flags.add_argument('-y', '--senderno', dest = 'sender_no', default = sender_no, help = 'Optional. Sender Number')
  flags.add_argument('-h', '--help', action='help')
  args = parser.parse_args()

  message = buildMessage(args)

  sendMessage(args, message)


main()
