from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome
'''
在PyQt5中，有多种布局的方式供我们选择，比较常用的布局有以下几种：
    表单布局：QFormLayout
    网格布局：QGridLayout
    水平排列布局：QHBoxLayout
    垂直排列布局：QVBoxLayout
每种布局都有自己对布局内小部件的控制方式和特点，在此我们选择网格布局
'''


class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 网格布局
        self.main_widget.setLayout(self.main_layout)  # 窗口主部件布局

        self.left_widget = QtWidgets.QWidget()
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()
        self.left_widget.setLayout(self.left_layout)

        self.right_widget = QtWidgets.QWidget()
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)

        # addWidget 参数为 控件名，行，列，占用行数，占用列数
        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        # 三个按钮
        self.left_close = QtWidgets.QPushButton('')
        self.left_visit = QtWidgets.QPushButton('')
        self.left_mini = QtWidgets.QPushButton('')

        self.left_label_1 = QtWidgets.QPushButton('每日推荐1')
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton('每日推荐2')
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton('每日推荐3')
        self.left_label_3.setObjectName('left_label')

        # 使用 qtawesome 中的图标
        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.music', color='white'), 'button_1')
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.sellsy', color='white'), 'button_2')
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.film', color='white'), 'button_3')
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.home', color='white'), 'button_4')
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.download', color='white'), 'button_5')
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.heart', color='white'), 'button_6')
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), 'button_7')
        self.left_button_7.setObjectName('left_button')
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), 'button_8')
        self.left_button_8.setObjectName('left_button')
        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='white'), 'button_9')
        self.left_button_9.setObjectName('left_button')

        # 将按钮添加到左侧的网格布局中
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)

        # 右侧

        # 搜索模块
        # 分为一个文本框（QLable）和一个搜索框（QLineEdit）
        self.right_bar_widget = QtWidgets.QWidget()
        self.right_bar_layout = QtWidgets.QGridLayout()  # 网格布局
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' Search:  ')
        self.search_icon.setFont(qtawesome.font('fa', 16))  # 字体，字号
        self.right_bar_widget_search_input = QtWidgets.QLineEdit()
        self.right_bar_widget_search_input.setPlaceholderText('You can input anything')

        self.right_bar_layout.addWidget(self.search_icon, 0, 0, 1, 1)
        self.right_bar_layout.addWidget(self.right_bar_widget_search_input, 0, 1, 1, 1)

        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)

        # 今日推荐

        # 最新歌曲  /tab    热门歌单
        # 播放条
#        self.init_ui()

#    def init_ui(self):

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUI()
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()