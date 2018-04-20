#!/usr/bin/env python
# -*- coding: utf-8 -*-

from weibo import APIClient

global tag_url
tag_url = ""#你的安全域名

def get_access_token(app_key, app_secret, callback_url):
    client = APIClient(app_key=app_key, app_secret=app_secret, redirect_uri=callback_url)
    # 获取授权页面网址
    auth_url = client.get_authorize_url()
    print auth_url
    # 在浏览器中访问这个URL，会跳转到回调地址，回调地址后面跟着code，输入code
    code =raw_input("Input code:")
    r = client.request_access_token(code)
    access_token = r.access_token
    # token过期的UNIX时间
    expires_in = r.expires_in
    print 'access_token:', access_token
    print 'expires_in:', expires_in

    return access_token, expires_in
def init_login():
    app_key = '' #你的API KEY
    app_secret = '' #你的API SEC
    access_token = '' #你的TOKEN
    expires_in = '' #TOKEN的过期时间
    callback_url = ''#回调网址
    if access_token=='':
        access_token, expires_in = get_access_token(app_key, app_secret, callback_url)
    # 上面的语句运行一次后，请保存得到的access token
    client = APIClient(app_key=app_key, app_secret=app_secret, redirect_uri=callback_url)
    client.set_access_token(access_token, expires_in)
    return client

def send_message(client,message):
    utext = unicode(message+tag_url,"UTF-8")
    client.post.statuses__share(status=utext)

def send_pic(client,message,picpath):
    f = open(picpath, 'rb')
    utext = unicode(message+tag_url,"UTF-8")
    client.statuses.share.post(status=utext, pic=f).text
    f.close()


if __name__ == '__main__':
     client = init_login()
