#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
 * Copyright (C) 2018 FU Berlin
 *
 * This file is subject to the terms and conditions of the GNU Lesser
 * General Public License v2.1. See the file LICENSE in the top level
 * directory for more details.
"""

from __future__ import absolute_import, print_function, unicode_literals


class Browser(object):

    name = None

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_root_install_path(self, isMacOS):
        return None

    def get_user_install_path(self, home_dir, isMacOS):
        return None

    def get_extension_file_web(self):
        return None


class Firefox(Browser):

    name = 'firefox'

    def __init__(self):
        super(Firefox, self).__init__(self.name)

    def get_root_install_path(self, isMacOS):

        if isMacOS:
            return ['/Library/Application Support/Mozilla/NativeMessagingHosts/']

        else:
            return ['/usr/lib/mozilla/native-messaging-hosts/',
                    '/usr/lib64/mozilla/native-messaging-hosts/',
                    '/usr/share/mozilla/native-messaging-hosts/']

    def get_user_install_path(self, home_dir, isMacOS):

        if isMacOS:
            return ['%s/Library/Application Support/Mozilla/NativeMessagingHosts/' % home_dir]

        else:
            return ['%s/.mozilla/native-messaging-hosts' % home_dir]

    def get_extension_file_web(self):
        pass


class Chrome(Browser):

    name = 'chrome'

    def __init__(self):
        super(Chrome, self).__init__(self.name)

    def get_root_install_path(self, isMacOS):

        if isMacOS:
            return ['/Library/Google/Chrome/NativeMessagingHosts']

        else:
            return ['/etc/opt/chrome/native-messaging-hosts']

    def get_user_install_path(self, home_dir, isMacOS):

        if isMacOS:
            return ['%s/Library/Application Support/Google/Chrome/NativeMessagingHosts' % home_dir]

        else:
            return ['%s/.config/google-chrome/NativeMessagingHosts' % home_dir]

    def get_extension_file_web(self):
        pass


class Chromium(Browser):

    name = 'chromium'

    def __init__(self):
        super(Chromium, self).__init__(self.name)

    def get_root_install_path(self, isMacOS):

        if isMacOS:
            return ['/Library/Application Support/Chromium/NativeMessagingHosts']

        else:
            return ['/etc/chromium/native-messaging-hosts']

    def get_user_install_path(self, home_dir, isMacOS):

        if isMacOS:
            return ['%s/Library/Application Support/Chromium/NativeMessagingHosts' % home_dir]

        else:
            return ['%s/.config/chromium/NativeMessagingHosts' % home_dir]

    def get_extension_file_web(self):
        pass


class BrowserNotSupportedException(Exception):

    def __init__(self, browser_name):
        super(BrowserNotSupportedException, self).__init__('%s is not supported' % browser_name)


def get_browser(browser_name):

    if browser_name == 'chrome':
        return Chrome()

    elif browser_name == 'chromium':
        return Chromium()

    elif browser_name == 'firefox':
        return Firefox()

    raise BrowserNotSupportedException(browser_name)
