from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import os
import sys


class MapItem(QGraphicsItem):
    HEIGHT = 100
    WIDTH = 200

    def __init__(self, x, y, desc, selected=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x = x
        self.y = y
        self.desc = desc
        self.rect = QRectF(x, y, self.WIDTH, self.HEIGHT)
        self.setZValue(10)
        self.selected = selected

    def paint(self, QPainter: QPainter, QStyleOptionGraphicsItem, widget=None):
        if self.selected:
            QPainter.setPen(QColor(255, 0, 0))
        QPainter.fillRect(self.rect, QBrush(Qt.white))
        QPainter.drawRect(self.rect)
        QPainter.drawText(self.rect, Qt.AlignCenter, self.desc)

    def boundingRect(self):
        return self.rect

    def __repr__(self):
        return '<MapItem: %s>' % self.desc


class MapScene(QGraphicsScene):

    def mousePressEvent(self, QGraphicsSceneMouseEvent):
        point: QPointF = QGraphicsSceneMouseEvent.scenePos()
        item = self.itemAt(point.x(), point.y(), QTransform())
        print(point)
        print(item)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        self.scene = MapScene()
        self.scene_view = QGraphicsView(self.scene)

        # self.path holds the path of the currently open file.
        # If none, we haven't got a file open yet (or creating new).
        self.path = None

        layout.addWidget(self.scene_view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        file_toolbar = QToolBar("File")
        file_toolbar.setIconSize(QSize(14, 14))
        self.addToolBar(file_toolbar)
        file_menu = self.menuBar().addMenu("&File")

        open_file_action = QAction(QIcon(os.path.join('images', 'blue-folder-open-document.png')), "Open file...", self)
        open_file_action.setStatusTip("Open file")
        open_file_action.triggered.connect(self.file_open)
        file_menu.addAction(open_file_action)
        file_toolbar.addAction(open_file_action)

        save_file_action = QAction(QIcon(os.path.join('images', 'disk.png')), "Save", self)
        save_file_action.setStatusTip("Save current page")
        save_file_action.triggered.connect(self.file_save)
        file_menu.addAction(save_file_action)
        file_toolbar.addAction(save_file_action)

        edit_toolbar = QToolBar("Edit")
        edit_toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(edit_toolbar)
        edit_menu = self.menuBar().addMenu("&Edit")

        undo_action = QAction(QIcon(os.path.join('images', 'arrow-curve-180-left.png')), "Undo", self)
        undo_action.setStatusTip("Undo last change")
        # undo_action.triggered.connect(self.editor.undo)
        edit_toolbar.addAction(undo_action)
        edit_menu.addAction(undo_action)

        redo_action = QAction(QIcon(os.path.join('images', 'arrow-curve.png')), "Redo", self)
        redo_action.setStatusTip("Redo last change")
        # redo_action.triggered.connect(self.editor.redo)
        edit_toolbar.addAction(redo_action)
        edit_menu.addAction(redo_action)

        edit_menu.addSeparator()

        cut_action = QAction(QIcon(os.path.join('images', 'scissors.png')), "Cut", self)
        cut_action.setStatusTip("Cut selected node")
        # cut_action.triggered.connect(self.editor.cut)
        edit_toolbar.addAction(cut_action)
        edit_menu.addAction(cut_action)

        copy_action = QAction(QIcon(os.path.join('images', 'document-copy.png')), "Copy", self)
        copy_action.setStatusTip("Copy selected node")
        # copy_action.triggered.connect(self.editor.copy)
        edit_toolbar.addAction(copy_action)
        edit_menu.addAction(copy_action)

        paste_action = QAction(QIcon(os.path.join('images', 'clipboard-paste-document-text.png')), "Paste", self)
        paste_action.setStatusTip("Paste from clipboard")
        # paste_action.triggered.connect(self.editor.paste)
        edit_toolbar.addAction(paste_action)
        edit_menu.addAction(paste_action)

        state_toolbar = QToolBar("State")
        state_toolbar.setIconSize(QSize(14, 14))
        self.addToolBar(state_toolbar)
        state_menu = self.menuBar().addMenu("&State")

        pointer_action = QAction(QIcon(os.path.join('images', 'pointer.png')), "pointer", self)
        pointer_action.setStatusTip("pointer State")
        # pointer_action.triggered.connect(self.editor.paste)
        state_toolbar.addAction(pointer_action)
        state_menu.addAction(pointer_action)
        # pointer_action.setEnabled(False)

        edit_action = QAction(QIcon(os.path.join('images', 'icon_edit.png')), "Edit a node", self)
        edit_action.setStatusTip("Edit a node")
        # edit_action.triggered.connect(self.insert_node_dialog)
        state_toolbar.addAction(edit_action)
        state_menu.addAction(edit_action)
        edit_action.setEnabled(False)

        delete_action = QAction(QIcon(os.path.join('images', 'deletion.png')), "Deletion", self)
        delete_action.setStatusTip("Deletion State")
        # delete_action.triggered.connect(self.input_dialog)
        state_toolbar.addAction(delete_action)
        state_menu.addAction(delete_action)
        delete_action.setEnabled(False)

        node_toolbar = QToolBar("State")
        node_toolbar.setIconSize(QSize(14, 14))
        self.addToolBar(node_toolbar)
        node_menu = self.menuBar().addMenu("&Node")

        sibling_action = QAction(QIcon(os.path.join('images', 'parent.png')), "Sibling", self)
        sibling_action.setStatusTip("Add Sibling Node")
        # sibling_action.triggered.connect(self.editor.paste)
        node_toolbar.addAction(sibling_action)
        node_menu.addAction(sibling_action)

        child_action = QAction(QIcon(os.path.join('images', 'child.png')), "Child", self)
        child_action.setStatusTip("Add Child Node")
        child_action.triggered.connect(self.insert_node_dialog)
        node_toolbar.addAction(child_action)
        node_menu.addAction(child_action)

        self.update_title()
        self.show()

        ### Just for demo
        root = MapItem(0, 0, 'Root <Root, ID:0>')
        self.scene.addItem(root)

        node = MapItem(300, 0, 'OS <Node, ID:1>', selected=True)
        self.scene.addItem(node)
        line1 = QGraphicsLineItem(50, 50, 350, 50)
        self.scene.addItem(line1)

        node2 = MapItem(300, 150, 'Network <Node, ID:2>')
        self.scene.addItem(node2)
        line2 = QGraphicsLineItem(200, 50, 300, 200)
        self.scene.addItem(line2)

        node3 = MapItem(600, 0, 'MacOS <Node, ID:3>')
        line3 = QGraphicsLineItem(350, 50, 600, 50)
        self.scene.addItem(node3)
        self.scene.addItem(line3)
        #
        ###

    def insert_node_dialog(self):
        node_desc, okPressed = QInputDialog.getText(self, "Edit a node", "New node description:", QLineEdit.Normal, "")
        print(node_desc)

    def dialog_critical(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    def file_open(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "*.ggm")

        try:
            with open(path, 'rU') as f:
                text = f.read()

        except Exception as e:
            self.dialog_critical(str(e))

        else:
            self.path = path
            self.update_title()

    def file_save(self):
        if self.path is None:
            # If we do not have a path, we need to use Save As.
            return self.file_saveas()

    def file_saveas(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "GogoMind documents (*.ggm);")

        if not path:
            # If dialog is cancelled, will return ''
            return

        else:
            self.path = path
            self.update_title()

    def update_title(self):
        self.setWindowTitle("%s - GogoMind" % (os.path.basename(self.path) if self.path else "Untitled"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("GogoMind")

    window = MainWindow()
    window.resize(900, 600)
    window.setWindowIcon(QIcon(os.path.join('images', 'icon.png')))
    app.exec_()
