import messages as msg

msg.hello()
msg.bye()

from messages import hello, bye  # * to import all, not recommended

hello()
bye()
