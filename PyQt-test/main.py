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
button_style_red = '''
QPushButton{
    background: #F76677;
    border-radius: 5px;
}
QpushButton: hover{
    background: red;
}
'''
button_style_yellow = '''
QPushButton{
    background: #F7D674;
    border-radius: 5px;
}
QpushButton: hover{
    background: yellow;
}
'''
button_style_green = '''
QPushButton{
    background: #6DDF6D;
    border-radius: 5px;
}
QpushButton: hover{
    background: green;
}
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
        # 在推荐音乐模块中，有一个推荐的标题，和一个横向排列的音乐封面列表，在这里：
        # 推荐标题使用QLable()来实现；
        # 音乐封面列表由多个QToolButton()组成，其继续由一个布局为QGridLayout()的QWidget()部件所包含。
        self.right_recommend_label = QtWidgets.QLabel('recommend')
        self.right_recommend_label.setObjectName('right_label')

        self.right_recommend_widget = QtWidgets.QWidget()
        self.right_recommend_layout = QtWidgets.QGridLayout()
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.recommend_button_1 = QtWidgets.QToolButton()
        self.recommend_button_1.setText('可馨HANM')
        self.recommend_button_1.setIcon(QtGui.QIcon('cover/r1.jpg'))
        self.recommend_button_1.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文

        self.recommend_button_2 = QtWidgets.QToolButton()
        self.recommend_button_2.setText('那首歌')
        self.recommend_button_2.setIcon(QtGui.QIcon('cover/r2.jpg'))
        self.recommend_button_2.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文
        
        self.recommend_button_3 = QtWidgets.QToolButton()
        self.recommend_button_3.setText('伟大的渺小')
        self.recommend_button_3.setIcon(QtGui.QIcon('cover/r3.jpg'))
        self.recommend_button_3.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文
        
        self.recommend_button_4 = QtWidgets.QToolButton()
        self.recommend_button_4.setText('荣耀征战')
        self.recommend_button_4.setIcon(QtGui.QIcon('cover/r4.jpg'))
        self.recommend_button_4.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文

        self.recommend_button_5 = QtWidgets.QToolButton()
        self.recommend_button_5.setText('猎场合辑')
        self.recommend_button_5.setIcon(QtGui.QIcon('cover/r5.jpg'))
        self.recommend_button_5.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文

        self.right_recommend_layout.addWidget(self.recommend_button_1, 0, 0)
        self.right_recommend_layout.addWidget(self.recommend_button_2, 0, 1)
        self.right_recommend_layout.addWidget(self.recommend_button_3, 0, 2)
        self.right_recommend_layout.addWidget(self.recommend_button_4, 0, 3)
        self.right_recommend_layout.addWidget(self.recommend_button_5, 0, 4)

        self.right_layout.addWidget(self.right_recommend_label, 1, 0 ,1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 2, 0, 2, 9)

        # 歌曲列表  /tab    热门歌单
        # 音乐列表模块和音乐歌单模块都有一个标题和一个小部件来容纳具体的内容
        # 其中标题我们都使用QLabel()部件来实现，而音乐列表我们使用网格布局的QWidget()部件下包裹着数个QPushButton()按钮部件来实现
        # 音乐歌单列表则使用网格布局的QWidget()部件下包裹着数个QToolButton()工具按钮部件来实现
        self.right_newsong_label = QtWidgets.QLabel('new www_www')
        self.right_newsong_label.setObjectName('right_label')

        self.right_newsong_widget = QtWidgets.QWidget()
        self.right_newsong_layout = QtWidgets.QGridLayout()
        self.right_newsong_widget.setLayout(self.right_newsong_layout)

        self.newsong_button_1 = QtWidgets.QPushButton('BBButtton1')
        self.newsong_button_2 = QtWidgets.QPushButton('BBButtton2')
        self.newsong_button_3 = QtWidgets.QPushButton('BBButtton3')
        self.newsong_button_4 = QtWidgets.QPushButton('BBButtton4')
        self.newsong_button_5 = QtWidgets.QPushButton('BBButtton5')
        self.newsong_button_6 = QtWidgets.QPushButton('BBButtton6')
        
        self.right_newsong_layout.addWidget(self.newsong_button_1, 0, 1)
        self.right_newsong_layout.addWidget(self.newsong_button_2, 1, 1)
        self.right_newsong_layout.addWidget(self.newsong_button_3, 2, 1)
        self.right_newsong_layout.addWidget(self.newsong_button_4, 3, 1)
        self.right_newsong_layout.addWidget(self.newsong_button_5, 4, 1)
        self.right_newsong_layout.addWidget(self.newsong_button_6, 5, 1)

        self.right_playlist_label = QtWidgets.QLabel('MMMM_MMMM')
        self.right_playlist_label.setObjectName('right_label')

        self.right_playlist_widget = QtWidgets.QWidget()
        self.right_playlist_layout = QtWidgets.QGridLayout()
        self.right_playlist_widget.setLayout(self.right_playlist_layout)

        self.playlist_button_1 = QtWidgets.QToolButton()
        self.playlist_button_1.setText('name1')
        self.playlist_button_1.setIcon(QtGui.QIcon('cover/p1.jpg'))
        self.playlist_button_1.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.playlist_button_2 = QtWidgets.QToolButton()
        self.playlist_button_2.setText('name2')
        self.playlist_button_2.setIcon(QtGui.QIcon('cover/p2.jpg'))
        self.playlist_button_2.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.playlist_button_3 = QtWidgets.QToolButton()
        self.playlist_button_3.setText('name3')
        self.playlist_button_3.setIcon(QtGui.QIcon('cover/p3.jpg'))
        self.playlist_button_3.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.playlist_button_4 = QtWidgets.QToolButton()
        self.playlist_button_4.setText('name4')
        self.playlist_button_4.setIcon(QtGui.QIcon('cover/p4.jpg'))
        self.playlist_button_4.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.right_playlist_layout.addWidget(self.playlist_button_1, 0, 0)
        self.right_playlist_layout.addWidget(self.playlist_button_2, 0, 1)
        self.right_playlist_layout.addWidget(self.playlist_button_3, 1, 0)
        self.right_playlist_layout.addWidget(self.playlist_button_4, 1, 1)

        # 上面两部分添加到右侧布局中
        self.right_layout.addWidget(self.right_newsong_label, 4, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_label, 4, 5, 1, 4)
        self.right_layout.addWidget(self.right_newsong_widget, 5, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_widget, 5, 5, 1, 4)

        # 播放条
        # 音乐播放进度条我们使用QProgressBar()进度条部件来实现
        self.right_process_bar = QtWidgets.QProgressBar()  # 播放进度
        self.right_process_bar.setValue(49)
        self.right_process_bar.setFixedHeight(3)
        self.right_process_bar.setTextVisible(False)  # 不显示文字

        # 音乐播放控制按钮组则使用一个QWidget()部件下包裹着三个QPushButton()按钮部件来实现
        self.right_playconsole_widget = QtWidgets.QWidget()
        self.right_playconsole_layout = QtWidgets.QGridLayout()
        self.right_playconsole_widget.setLayout(self.right_playconsole_layout)

        self.console_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.backward', color = '#F76677'), '')
        self.console_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.forward', color = '#F76677'), '')
        self.console_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.pause', color = '#F76677'), '')
        self.console_button_3.setIconSize(QtCore.QSize(30, 30))

        self.right_playconsole_layout.addWidget(self.console_button_1, 0, 0)
        self.right_playconsole_layout.addWidget(self.console_button_2, 0, 2)
        self.right_playconsole_layout.addWidget(self.console_button_3, 0, 1)
        self.right_playconsole_layout.setAlignment(QtCore.Qt.AlignCenter)  # 设置布局内部件居中显示
        
        self.right_layout.addWidget(self.right_process_bar, 9, 0, 1, 9)
        self.right_layout.addWidget(self.right_playconsole_widget, 10, 0, 1, 9)


        self.fun_QSS()
        self.fun_QT5()
    
    # 美化
    def fun_QSS(self):
        # 左上 三个按钮
        self.left_close.setFixedSize(15, 15)
        self.left_visit.setFixedSize(15, 15)
        self.left_mini.setFixedSize(15, 15)

        self.left_close.setStyleSheet(button_style_red)
        self.left_visit.setStyleSheet(button_style_yellow)
        self.left_mini.setStyleSheet(button_style_green)


        # 将左侧菜单中的按钮和文字颜色设置为白色，并将按钮的边框去掉
        self.left_widget.setStyleSheet('''
            QWidget#left_widget{
                background:darkGray;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        # 右侧搜索框 圆角
        self.right_bar_widget_search_input.setStyleSheet('''
            QLineEdit{
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
            }
        ''')

        # 右侧部件 右上角和右下角圆角 背景设置为白色
        # 字体放大
        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }

            QLabel#right_label{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        # 推荐模块和歌单模块 QToolButton
        self.right_recommend_widget.setStyleSheet('''
            QToolButton{border:none;}
            QToolButton:hover{border-bottom:2px solid #F76677;}
        ''')
        self.right_playlist_widget.setStyleSheet('''
            QToolButton{border:none;}
            QToolButton:hover{border-bottom:2px solid #F76677;}
        ''')
        
        # 音乐列表使用的是QPushButton()按钮部件，我们需要对其去除边框，修改字体和颜色等
        self.right_newsong_widget.setStyleSheet('''
            QPushButton{
                border:none;
                color:gray;
                font-size:12px;
                height:40px;
                padding-left:5px;
                padding-right:10px;
                text-align:left;
            }
            QPushButton:hover{
                color:black;
                border:1px solid #F3F3F5;
                border-radius:10px;
                background:LightGray;
            }
        ''')

        # 将播放进度条的样色设置为浅红色，然后去除播放控制按钮的边框
        self.right_process_bar.setStyleSheet('''
            QProgressBar::chunk{background-color: #F76677;}
        ''')
        self.right_playconsole_widget.setStyleSheet('''
            QPushButton{border:none;}
        ''')

    def fun_QT5(self):
        self.setWindowOpacity(0.9)  # 透明度
        
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 窗口背景透明

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        self.main_layout.setSpacing(0)  # 无缝
#    def init_ui(self):

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUI()
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()