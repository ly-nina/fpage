import base64
import json
import time
import OpenSSL.crypto as ct
from OpenSSL.crypto import FILETYPE_PEM

# config 官方demo是字典
config_list = {
    'app_id':  '2016091300499397',                                                           # 应用id
    'merchant_private_key':  'MIIEowIBAAKCAQEAoCOlauccWH0OLiJEbCBdKKayNPHGQF7vW2jx025xykzVijNB8APSPaFxuZ/CU+71a1XlFOtHz5jJqQwf0PZw5dDAfwUcbcVbiy+v3r/maY1OcgQew5CY+43sslVSDKt2PpuSQ9FBcAlZOe2ptB48V0aQy7lHr3Y1n/LS0eJzLNcEhnc1h9Ny49vbG2siadGHZBjRJskMQh/jOHfP+KmcmmkaHlzpE/HxUYJuOXJqrMqt6/Qf2l5oMitMHL3Rllro4MCqr2IjCe9xjV2K6/1KdF4NS+9Nm9GshDEYSC/MJuQCrr58sNhqemaIcaCCNc8HdPwEWUAUWTzpsBIHD8D4XQIDAQABAoIBADBsNvPJaIfVYLlQgVIUwzasmUxrI2CJlGUWqbEeP2hFrXh5oWGbNjKOo93WUiOhKTLIqVmW/4Lll2z3jpNYQbEsW1jNSdhjihffVpXLfzfBk8vkNQ07pxbBxqXyKLpOCpZJ4oOBPgFLwmBC3kLptaNKYjRIFUYYP4TbHyZ6DAutilExKQiPXnJRmqfUHnn3eY9Uc0vvxqIwoO1dhvNbZgYIXV/AHxpwFue7iTOWHQv3JihjmN//plQbpjquTOLJhDVLvqW3h7v72egANbIQd1XzH+T0FLqE5ZC8zHiwk2buI3YV3nj++A6+Src7tU5BS1pxbSWjx0mZWVeY+kDkMqECgYEA0yLGlRO1AenTrC9CtmKplnpKOMMqO2xIiW5ZADC6DZX3boy0lqzEN/eZOEL8flsM75Dmk7gqOQJhqb1AYCrArRpwprJ49vZCh/xPWZd3amWRr/lW8dbGmttku8gplkBOiH6tq/5kPpHkbrPkuRyw5nejo9uGLj8uYAlmoAF+RwkCgYEAwirKweO2zGpuvcDihIUOtHwHKzz+d7nbZIL/8iu2IeD6gegCYGYucWl8ENWRG5YC5/IBWWVpFIOCwrqVE3cRkmgTK+zP/SAe+0Q3aylSiHrds+mOvQ/U4EPP31RO9vTqhpLLlFG0JEpLYtNXGBfoloXXf1Am1saiv72BOf+rh7UCgYB0MCH57dNhTyz2Bzf+KENNFNT9caEu/ELapkgCC86HJWz5gCLs+/wrFG1UAcDzQ+XVe/b3eZR6tO3Lu+LOSRio6fDuOy7IMPKh5N5B3lGP0n8eyOboxRmcJHnFwLvp/E97W8L08FR3/k8oAIUwvTI4UcRSqr6neotpvCKmkMvOCQKBgAhgJizk8L6ynKJMzriesLqyWvDPib6KYt9cE0RUBGBDvyqZYnjcD4bO4Q4s2DyTZP6yXsKHcFf1ME/MEqArU7O4D5OmfHZTy2JVV/qkZq4CdsvK+GBJbYpbAn2Eun9Go1M4w9VbDOU/2y6hJTGh3mOX1GrmfzZmjSCuQQPKdpC9AoGBANG34mxLNbXD4j9AJatX+CtVd7FRO9v4QVFw5brLaAZw918H2TwDaPGyVPm3kGZ65sdfm+C70W4G3Abq3DcZnuOqYdx8sNIcNBN0HglB457L+6PztYbZSGc2IHslrlNiOKCqGU7v3D3smkH/zvQDdCy+zthA7ikOtFoY0yQEjLPe',                                            # 商户私钥
    'notify_url':  'http://182.254.209.84/alipay.trade.page.pay-PHP-UTF-8/notify_url.php',                                                       # 异步通知地址
    'return_url':  'http://182.254.209.84/alipay.trade.page.pay-PHP-UTF-8/return_url.php',                                                      # 同步跳转地址
    'charset': 'UTF-8',
    'sign_type': 'RSA2',
    'alipay_public_key': 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2ktbldc9rB2NjUdcZ+CcWcIiQXEB9pcYGNQFwAepVQVdWO3zAvsY9yfmptWqXxrRzhyVl1BZCsXjjduMDLO5cSe00n78TEcAg11Cgx5pzlcQibXGMYHi1iEbAwR9XgWzWNSMEN+gWkCpE/BbvEdAc+Nyfkr3hmFf8xVHuakIVJ0T+tSsM+FezX7AJGjNM8Uzae9pOSb8xunkmXP6caUvrbyxs4g5Nw3JCzEatX3a24UuQmUyrUsQBMLWF+dxPDioos58KQgZP1f5eQRhbIalrxkd1dVpEFFCmXagcsO16iY6liyl+7t4+O/oH/G2mmF0a/EnrhUP3SKx3pQnaRm0VwIDAQAB',                                            # 对应appid的支付宝公钥
    'gatewayUrl': 'https://openapi.alipaydev.com/gateway.do',       # 支付宝网关/沙盒网关
}

data = {
    'out_trade_no': '',          # 订单号
    'subject': '',              # 订单名称
    'total_amount': '',         # 付款金额
    'body': ''                 # 商品描述
}




# /buildermodel/AlipayTradePagePayContentBuilder.php
# 用builder中的set...方法设置上面几个变量

class AlipayTradePagePayContentBuilder:
    bizContentarr = {'product_code': "FAST_INSTANT_TRADE_PAY"}      # 共有变量，放在class内。每个实例私有变量用__init__初始化

    def __init__(self):
        self.body = ''
        self.subject = ''
        self.outTradeNo = ''
        self.totalAmount = ''
        # 产品标识码
        self.productCode = ''
        self.bizContent = None

    def set_body(self, body):  # 私有变量
        self.body = body
        self.bizContentarr['body'] = body

    def set_subject(self, subject):
        self.subject = subject
        self.bizContentarr['subject'] = subject

    def set_out_trade_no(self, outTradeNo):
        self.outTradeNo = outTradeNo
        self.bizContentarr['out_trade_no'] = outTradeNo

    def set_total_amount(self, totalAmount):
        self.totalAmount = totalAmount
        self.bizContentarr['total_amount'] = totalAmount

    def getBizContent(self):
        if self.bizContentarr is not None:
            self.bizContent = json.dumps(self.bizContentarr, ensure_ascii=False)

        return self.bizContent

# /service/AlipayTradeService.php
# 用该文件中的pagePay方法，输出订单，且配置同步/异步回调地址（公网可以访问的地址）

class AlipayTradeService:

    def __init__(self, config):
        self.format = "json"
        self.app_id = config['app_id']
        self.charset = config['charset']
        self.sign_type = config['sign_type']
        self.gateway_url = config['gatewayUrl']
        self.alipay_public_key = config['alipay_public_key']
        self.merchant_private_key = config['merchant_private_key']

        # if not self.app_id or not self.app_id.strip():
        #     raise Exception('app_id Error!')
        # if not self.charset or not self.app_id.strip():
        #     raise Exception('charset Error!')
        # if not self.sign_type or not self.sign_type.strip():
        #     raise Exception('sign_type Error!')
        # if not self.gateway_url or not self.gateway_url.strip():
        #     raise Exception('gateway_url Error!')
        # if not self.alipay_public_key or not self.alipay_public_key.strip():
        #     raise Exception('alipay_public_key Error!')
        # if not self.merchant_private_key or not self.merchant_private_key.strip():
        #     raise Exception('merchant_private_key Error!')

        assert self.app_id and self.app_id.strip(), 'app_id Error!'
        assert self.charset and self.charset.strip(), 'charset Error!'
        assert self.sign_type and self.sign_type.strip(), 'sign_type Error!'
        assert self.gateway_url and self.gateway_url.strip(), 'gateway_url Error!'
        assert self.alipay_public_key and self.alipay_public_key.strip(), 'alipay_public_key Error!'
        assert self.merchant_private_key and self.merchant_private_key.strip(), 'merchant_private_key Error!'

    def pagePay(self, builder, return_url, notify_url):
        biz_content = builder.getBizContent()
        # write biz_content to log
        # write_log(biz_content)
        req = PagePayRequest()
        req.set_notify_url(notify_url)
        req.set_return_url(return_url)
        req.set_bizContent(biz_content)
        # 调用支付API
        res = self.aopclientrequestExecute(req, True)
        return res

    def aopclientrequestExecute(self, req, isPage=False):  # 这里变量名字变了
        aop = AopClient()
        aop.apiVersion = '1.0'
        aop.appId = self.app_id
        aop.format = self.format
        aop.signType = self.sign_type
        aop.postCharset = self.charset
        aop.gatewayUrl = self.gateway_url
        aop.alipayrsaPublicKey = self.alipay_public_key
        aop.rsaPrivateKey = self.merchant_private_key
        aop.debug = True  # 开启页面信息输出

        if isPage:
            result = aop.PageExecute(req, 'post')
            # print(result)
        else:
            result = None
            # result = aop.Execute(req)
            # 未用到，先不考虑

        # 写入日志
        # write_log('response: result....')
        return result


class PagePayRequest:
    terminalType = ''
    terminalInfo = ''
    prodCode = ''
    apiVersion = "1.0"
    notify_url = ''
    return_url = ''
    apiParas = {}

    def set_notify_url(self, notify_url):
        self.notify_url = notify_url

    def set_return_url(self, retuen_url):
        self.return_url = retuen_url

    def set_bizContent(self, bizcontent):  # 在这里把表单塞到另一个字典中
        self.apiParas['biz_content'] = bizcontent

    def getApiMethodName(self):
        return "alipay.trade.page.pay"

    def getTerminalType(self):
        return self.terminalType

    def getTerminalInfo(self):
        return self.terminalInfo

    def getProdCode(self):
        return self.prodCode

    def getNotifyUrl(self):
        return self.notify_url

    def getReturnUrl(self):
        return self.return_url

    def getApiParas(self):
        return self.apiParas

class AopClient:
    apiVersion = '1.0'
    appId = ''
    format = 'json'
    # sign = ''
    postCharset = 'UTF-8'
    gatewayUrl = ''
    alipayrsaPublicKey = ''
    rsaPrivateKey = ''
    debugInfo = False
    signType = 'RSA'
    alipaySdkVersion = "alipay-sdk-php-20161101"
    rsaPrivateKeyFilePath = r'F:\work\LanS\LED\pay\Alipay_for_python'
    fileCharset = "UTF-8"

    def PageExecute(self, req, method="POST"):
        # 官方有编码检测 ---- 本地文件字符集编码 和 表单提交编码  是否一致
        # setupCharsets(rea)
        # if xxxxxx

        # 判断api_version
        # if xxx

        # 组装参数
        sysParams = {
            "app_id": self.appId,
            "version": self.apiVersion,  # 上面api_version 判断完后的
            "format": self.format,
            "sign_type": self.signType,
            "method": req.getApiMethodName(),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),  # 时间， php中是  date("Y-m-d H:i:s")
            "alipay_sdk": self.alipaySdkVersion,
            "terminal_type":  req.getTerminalType(),
            "terminal_info": req.getTerminalInfo(),
            "prod_code": req.getProdCode(),
            "notify_url": req.getNotifyUrl(),
            "return_url": req.getReturnUrl(),
            "charset": self.postCharset
        }

        apiParas = req.getApiParas()
        # 判断是否需要加密，付款默认是false
        # if xxx

        totalParams = {**apiParas, **sysParams}
        # 待签名字符串
        preSignStr = self.getSignContent(totalParams) # 没有用到该变量

        # 签名
        totalParams['sign'] = self.generateSign(totalParams, self.signType)

        if method.upper() == 'GET':  # 目前只有POST，先不考虑其他业务
            pass
        else:
            return self.buildRequestForm(totalParams)

    # 转换成目标字符集
    # 字典->字符串
    def getSignContent(self, params):
        temp = {}
        # temp = {i: a[i] for i in sorted(a.keys())}  # 一样的方法
        for i in sorted(params.keys()):
            temp[i] = params[i]

        params = temp
        stringToSigned = ""
        i = 0
        for k, v in params.items():
            if not self.checkEmpty(v) and '@' != v[:1]:
                # v = self.characet(v, self.postCharset) 编码一样，没做变换。先不处理
                if i == 0:
                    stringToSigned += k + "=" + v
                else:
                    stringToSigned += "&" + k + "=" + v
                i += 1

        return stringToSigned

    # 转换字符集编码
    def characet(self, value, targetCharaset):
        if not value:
            fileType = self.fileCharset
            if fileType.lower() != targetCharaset.lower():  # 对比两种编码是否一样，直接两种编码转换而不是str和bytes
                # py2 可以直接 str.decode(from_encoding).encode(to_encoding)
                pass

        return value


    def generateSign(self, params, signType='RSA'):
        return self.sign(self.getSignContent(params), signType)

    # data 是待签名字符串
    def sign(self, data, signType='RSA'):
        if self.checkEmpty(self.rsaPrivateKeyFilePath):
            prikey = self.rsaPrivateKey
            res = '-----BEGIN RSA PRIVATE KEY-----\n' + self.wordwrap(prikey, 64) + '\n-----END RSA PRIVATE KEY-----'
            
            with open(r'%s\key.pem' % self.rsaPrivateKeyFilePath, 'w') as f:
                f.write(res)
            
        
        else:  # 不作路径设置，直接传入私钥值，所以先不管下面的读取私钥文件操作
            with open(r'F:\work\LanS\LED\pay\Alipay_for_python\key.pem', 'r') as f:
                res = f.read()
            
        load_key = ct.load_privatekey(FILETYPE_PEM, res)
        
        if not res:
            raise Exception('RSA Error!')
        """
        File "D:\python3\lib\site-packages\OpenSSL\crypto.py", line 2867, in sign
            digest_obj = _lib.EVP_get_digestbyname(_byte_string(digest))
          File "D:\python3\lib\site-packages\OpenSSL\_util.py", line 112, in byte_string
            return s.encode("charmap")
        AttributeError: 'bytes' object has no attribute 'encode'
        https://pyopenssl.readthedocs.io/en/latest/api/crypto.html#OpenSSL.crypto.PKey
        """
        # res 应该要是PKey 类型。
        if 'RSA2' == signType:
            sign_data = ct.sign(load_key, data, 'sha256')
            # ct.load_privatekey()
            
        else:
            sign_data = ct.sign(load_key, data, 'sha1')

        # python 没有free操作
        # if not self.checkEmpty(self.rsaPrivateKeyFilePath):
        #     openssl_free_key

        sign_data = base64.b64encode(sign_data)
        return sign_data

    def wordwrap(self, input_data, length):
        data_len = len(input_data)
        count = int(data_len / length)
        d = input_data[:length]

        for i in range(count):
            d += '\n' + input_data[length * (i + 1):length * (i + 2)]

        return d

    def buildRequestForm(self, param_temp):
        sHtml = "<form id='alipaysubmit' name='alipaysubmit' action='" + self.gatewayUrl + "?charset=" + self.postCharset.strip() + "' method='POST'>"
        
        for k, v in param_temp.items():
            if not self.checkEmpty(v):
                # print(v)
                # v = v.replace("'", "&apos")
                if k == 'sign':
                    v = v.decode()
                sHtml += "<input type='hidden' name='" + k + "' value='" + v + "'/>"

        # submit按钮控件请不要含有name属性
        sHtml += "<input type='submit' value='ok' style='display:none;'></form>"
        sHtml += "<script>document.forms['alipaysubmit'].submit();</script>"
        return sHtml

    def checkEmpty(self, value):
        if '%s' % value in locals().keys():
            return True

        if not value:
            return True

        if value.strip() == '':
            return True

        return False

'''
if __name__ == '__main__':
    
    testClass = AlipayTradePagePayContentBuilder()
    testClass.set_body('123')
    testClass.set_out_trade_no('a')
    # print(testClass.bizContentarr)
    aop = AlipayTradeService(config_list)
    response = aop.pagePay(testClass, config_list['return_url'], config_list['notify_url'])
    
'''
    
