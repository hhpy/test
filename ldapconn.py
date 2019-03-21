#!usr/bin/env python
#coding: utf-8
import traceback
import os
import sys
import ldap

def login_ldap(username, password):
    try:
        conn = ldap.initialize("ldaps://ldap.staff.test.com:636")
        conn.protocol_version = ldap.VERSION3
        conn.simple_bind_s(username, password)
        print('ldap connect successfully')
    except:
        traceback.print_exc()
        print("ldap connect failure")

def login_ldap_test(username, password):
    try:
        conn = ldap.initialize("ldaps://172.0.0.1:636")
        conn.protocol_version = ldap.VERSION3
        conn.simple_bind_s(username, password)
        print('ldap connect successfully')
    except:
        traceback.print_exc()
        print("ldap connect failure")
if __name__ == "__main__":
    login_ldap("staff\test", "xxxx")
    login_ldap_test("ekin\dddd", "xxxx")







