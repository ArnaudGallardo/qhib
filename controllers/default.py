# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

import urllib2
import json
import dateutil.parser
import hitbox


def get_key(url):
    authKey = hitbox.get_auth()
    hitbox.reset_streamKey(authKey)
    streamKey = hitbox.get_streamKey(authKey)
    return 0


def index():
    #get_key("")
    form=FORM(INPUT(_type='submit', _class='loginBtn', _value=XML('&#xf090;')),
              INPUT(_name='email', requires=IS_NOT_EMPTY(), _class='login', _placeholder=XML("&#xf0e0;")),
              INPUT(_name='password', _type='password', requires=IS_NOT_EMPTY(), _class='login', _placeholder=XML("&#xf084;")))
    form['_style']='width:200px'
    connected = False
    email, password = request.post_vars['email'], request.post_vars['password']
    if request.post_vars:
        print "posted"
        user = auth.login_bare(email, password)
        if user != False:
            connected = True
            print user
    dico = {"form": form, "connected": connected}
    return dict(dico=dico)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


