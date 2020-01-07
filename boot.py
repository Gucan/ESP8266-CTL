import os,gc,machine,network,socket,hashlib,ucryptolib
gc.collect()
gc.enable()
PIN=[16,5,4,0,2,14,12,13,15]
KEY=hashlib.sha256("Gucan").digest()
server=socket.socket()
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('',37521))
server.listen(10)
while True:
    con,add=server.accept()
    DATA=ucryptolib.aes(KEY,2,KEY[8:24]).decrypt(con.recv(1024)).decode()
    if DATA[0:1].isdigit() and int(DATA[0:1])>=1 and int(DATA[0:1])<=8:
        if DATA[1:3]=="ON":
            machine.Pin(PIN[int(DATA[0:1])],1).on()
        elif DATA[1:3]=="OF":
            machine.Pin(PIN[int(DATA[0:1])],1).off()
        elif DATA[1:3]=="ST":
            if machine.Pin(PIN[int(DATA[0:1])],1).value():
                con.send("ON")
            else:
                con.send("OF")
        else:
            con.send("指令不合法")
    else:
        con.send("引脚不可用")
    con.close()
