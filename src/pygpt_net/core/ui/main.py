#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2023.12.17 22:00:00                  #
# ================================================== #
import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QSplitter, QWidget

from .output import Output
from .toolbox import Toolbox
from .menu import Menu
from .dialogs import Dialogs
from .contexts import Contexts
from .attachments import Attachments
from .attachments_uploaded import AttachmentsUploaded


class UI:
    def __init__(self, window=None):
        """
        UI (main)

        :param window: Window instance
        """
        self.window = window
        self.nodes = {}
        self.splitters = {}
        self.tabs = {}
        self.menu = {}
        self.models = {}
        self.groups = {}
        self.paths = {}
        self.config_option = {}
        self.plugin_data = {}
        self.plugin_option = {}
        self.plugin_addon = {}

        self.chat = Output(window)
        self.toolbox = Toolbox(window)
        self.contexts = Contexts(window)
        self.attachments = Attachments(window)
        self.attachments_uploaded = AttachmentsUploaded(window)
        self.menus = Menu(window)
        self.dialogs = Dialogs(window)

    def setup(self):
        """Setup UI"""
        # load font
        self.setup_font()

        # chat and toolbox
        self.window.chat = self.chat.setup()
        self.window.toolbox = self.toolbox.setup()

        # ctx
        self.window.ctx = QWidget()
        self.window.ctx.setLayout(self.contexts.setup())

        # set width
        self.window.ctx.setMinimumWidth(200)

        # horizontal splitter
        self.window.ui.splitters['main'] = QSplitter(Qt.Horizontal)
        self.window.ui.splitters['main'].addWidget(self.window.ctx)  # contexts
        self.window.ui.splitters['main'].addWidget(self.window.chat)  # chat box
        self.window.ui.splitters['main'].addWidget(self.window.toolbox)  # toolbox
        self.window.ui.splitters['main'].setSizes([1, 8, 1])

        # menu
        self.menus.setup()

        # dialogs
        self.dialogs.setup()

        # set central widget
        self.window.setCentralWidget(self.window.ui.splitters['main'])

    def setup_font(self):
        """Setup UI font"""
        path = os.path.join(self.window.config.get_root_path(), 'data', 'fonts', 'Lato', 'Lato-Regular.ttf')
        font_id = QFontDatabase.addApplicationFont(path)
        if font_id == -1:
            print("Error loading font file {}".format(path))
        else:
            family = QFontDatabase.applicationFontFamilies(font_id)[0]
