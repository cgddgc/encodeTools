#!python 3
#coding=utf-8
import base64,urllib.parse,hashlib

class coder:
    def __init__(self):
        self.func_list=[('base64编码','b64enc'),('base64解码','b64dec'),('URL编码','urlenc'),('URL解码','urldec'),('ip转换长整数','ip2int'),('长整数转换ip','int2ip'),('md5转换','md5enc')]
        pass

    def ip2int(self,ip):                        #IP地址转换为长整数
        ips=ip.split('.')
        res=0
        try:
            for i in range(4):
                res=res+int(ips[i])*256**(3-i)
        except Exception as e:
            res='Please input correct ip address!'
        return res

    def int2ip(self,li):                        #长整数转换为ip地址
        try:
            li=int(li)
            if li < 4294967296 and li > 16777215:
                res=[]
                ip=li
                for j in range(4):
                    buf=divmod(ip,256**(3-j))
                    ip=buf[1]
                    res.append(buf[0])
                restr=str(res[0])+'.'+str(res[1])+'.'+str(res[2])+'.'+str(res[3])
            else:
                restr='Data too big or too small!'
        except Exception as e:
            restr='Input not a valid ip int value!'
        return restr


    def b64dec(self,string):                #base64解码函数
        string=str(string)
        if string[-2]!='=':
            string+='=='
        elif string[-1]!='=':
            string+='='
        try:
            res=base64.b64decode(string).decode('utf-8')
        except Exception as e:
            res='Input not a valid base64 encode string'
        return res

    def b64enc(self,string):                #base64编码函数
        string=str(string)
        return base64.b64encode(string.encode('utf-8')).decode('utf-8')

    def urlenc(self,string):                #urlencode函数
        string=str(string)
        res=urllib.parse.quote(string)
        while res[-3:]=='%0A':
            res=res[:-3]
        return res


    def urldec(self,string):                #urldecode函数
        string=str(string)
        res=urllib.parse.unquote(string)
        while res[-3:]=='%0A':
            res=res[:-3]
        return res


    def md5enc(self,string):                #计算md5值，32位小写字母
        string=str(string).encode('utf-8')
        m=hashlib.md5()
        m.update(string)
        return m.hexdigest()




if __name__ == '__main__':  
    c=coder()
    out=c.md5enc(0)
    print(out)