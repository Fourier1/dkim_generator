#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-

import os


# TODO comment ajouter la commande su zimbra avant execution.
# TODO les caracteres a suprimer dans le DKIM gener : " ,

def generate_dkim(_domaine):
    """ Generate DKIM"""
    cmd_dkim = "/opt/zimbra/libexec/zmdkimkeyutil -a -d " + _domaine
    try:
        dkim_ = os.system(cmd_dkim)
        print(dkim_)
        print("\n[ok] Create DKIM\n")
    except os.error as e:
        print(e)


def delete_dkim(_domaine):
    """ Generate DKIM"""
    cmd_dkim = "/opt/zimbra/libexec/zmdkimkeyutil -r -d " + _domaine
    try:
        print(os.system(cmd_dkim))
        print("\n[ok] Delete DKIM\n")
    except os.error as e:
        print(e)


def print_dkim(_domaine):
    """ Generate DKIM"""
    cmd_dkim = "/opt/zimbra/libexec/zmdkimkeyutil -u -d " + _domaine
    try:
        print(os.system(cmd_dkim))
        print("\n[ok] Print DKIM\n")
    except os.error as e:
        print(e)

# if __name__ == '__main__':
#     generate_dkim("domainna.ci")
    # print_dkim("domainna.ci")
    # delete_dkim("domainna.ci")
