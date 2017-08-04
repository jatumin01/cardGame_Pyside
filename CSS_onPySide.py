from PySide import QtGui,QtCore

from PySide.QtCore import QObject, Signal, Slot
import sys
import random
if not "%userprofile%/Desktop/Yggdrazil_python/week09" in sys.path:
    sys.path.append("%userprofile%/Desktop/Yggdrazil_python/week09")

import pipelineGameCard.CG_masterCompiled as GameFuc
reload(GameFuc)

class TestEvent(QtGui.QDialog):
    def __init__(self):
        super(TestEvent,self).__init__()
        print 
        self.setFixedSize(QtCore.QSize(1000,800))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowTitle('eieiei')
        self.cardGame = GameFuc.c
        self.virable()
        self.widget()
        self.layout()
        self.connect()
        self.timer()
        self.check = 0

    def virable(self):
        self.cha = ["charHero.png","charMons.png","charBoss.png"]
        self.w = 1000
        self.h = 800
        self.heroCard = ["aHero.png","dHero.png","bHero.png","heal.png"]
        self.monsCard = ["aMons.png","dMons.png","bMons.png","heal.png"]
        self.bossCard = ["aBoss.png","dMons.png","bMons.png","heal.png"]
        self.backCard = "card.png"
        self.c1_count = 0
        self.c2_count = 0
        self.c3_count = 0
        self.heroCard_count = 0

        self.c1_switch = 0
        self.c2_switch = 0
        self.c3_switch = 0
        self.heroCard_switch = 0

    def widget(self):
        # set shadows
        self.shadow = QtGui.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setOffset(5)
        self.shadow.setColor(QtGui.QColor(0,0,0))
        self.shadow1 = QtGui.QGraphicsDropShadowEffect(self)
        self.shadow1.setBlurRadius(20)
        self.shadow1.setOffset(5)
        self.shadow1.setColor(QtGui.QColor(0,0,0))
        self.shadow2 = QtGui.QGraphicsDropShadowEffect(self)
        self.shadow2.setBlurRadius(20)
        self.shadow2.setOffset(5)
        self.shadow2.setColor(QtGui.QColor(0,0,0))
        self.shadow3 = QtGui.QGraphicsDropShadowEffect(self)
        self.shadow3.setBlurRadius(20)
        self.shadow3.setOffset(5)
        self.shadow3.setColor(QtGui.QColor(0,0,0))
        self.shadow4 = QtGui.QGraphicsDropShadowEffect(self)
        self.shadow4.setBlurRadius(20)
        self.shadow4.setOffset(5)
        self.shadow4.setColor(QtGui.QColor(0,0,0))
        self.shadow5 = QtGui.QGraphicsDropShadowEffect(self)
        self.shadow5.setBlurRadius(20)
        self.shadow5.setOffset(5)
        self.shadow5.setColor(QtGui.QColor(0,0,0))
        self.shadow6 = QtGui.QGraphicsDropShadowEffect(self)
        self.shadow6.setBlurRadius(20)
        self.shadow6.setOffset(5)
        self.shadow6.setColor(QtGui.QColor(0,0,0))
        self.shadow7 = QtGui.QGraphicsDropShadowEffect(self)
        self.shadow7.setBlurRadius(20)
        self.shadow7.setOffset(5)
        self.shadow7.setColor(QtGui.QColor(0,0,0))


        ################
        #              #
        #    title     #
        #              #
        ################
        self.clear_btn = QtGui.QPushButton("x")
        self.clear_btn.setFixedSize(QtCore.QSize(30,30))
        self.hide_btn = QtGui.QPushButton("_")
        self.hide_btn.setFixedSize(QtCore.QSize(30,30))
        self.restrat_btn = QtGui.QPushButton("Restrat")
        self.restrat_btn.setFixedSize(QtCore.QSize(70,25))
        self.restrat_btn.setStyleSheet("""QPushButton{ background:white; border-radius:12px;}""")
        self.clear_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.titlelabel = QtGui.QLabel("CARD GAME |")
        self.titlelabel.setStyleSheet("""QLabel{ color:white;}""")


        #####################
        #                   #
        #    procress bar   #
        #                   #
        #####################
        self.turn = QtGui.QLabel("00")
        self.turn.setFixedSize(QtCore.QSize(40,40))
        self.turn.setAlignment(QtCore.Qt.AlignCenter)
        self.turn.setStyleSheet("""QLabel{ background:white;  border-radius:20px;}""")
        self.heroName = QtGui.QLabel("HERO")
        self.monsterName = QtGui.QLabel("MONSTER")
        self.processBar1 = QtGui.QProgressBar()
        self.processBar1.setMaximum(300)
        self.processBar1.setMinimum(0)
        self.processBar1.setValue(self.cardGame.hero.hp)
        #self.processBar1.setTextVisible(False)
        self.processBar2 = QtGui.QProgressBar()
        self.processBar2.setMaximum(150)
        self.processBar2.setMinimum(0)
        self.processBar2.setValue(self.cardGame.monsterType.hp)
        self.processBar2.setInvertedAppearance(True)
        #self.processBar2.setTextVisible(False)
 
        self.herostatus  = QtGui.QLabel("")
        self.herostatus.setAlignment(QtCore.Qt.AlignCenter)
        self.herostatus.setFixedSize(QtCore.QSize(200,30))
        self.herostatus.setStyleSheet("""QLabel{ background:white;  border-radius:15px;}""")
        self.monsterstatus  = QtGui.QLabel("")
        self.monsterstatus.setFixedSize(QtCore.QSize(200,30))
        self.monsterstatus.setAlignment(QtCore.Qt.AlignCenter)
        self.monsterstatus.setStyleSheet("""QLabel{ background:white;  border-radius:15px;}""")


        self.heropic = QtGui.QLabel(" Hero Pic")
        self.heropic.setPixmap(QtGui.QPixmap(self.cha[0]))
        self.heropic.setGraphicsEffect(self.shadow1)
        self.herochoose = QtGui.QLabel("Hero Choose")
        self.herochoose.setPixmap(QtGui.QPixmap("backCard.png"))
        self.herochoose.setGraphicsEffect(self.shadow2)
        self.vs = QtGui.QLabel("VS")
        self.vs.setPixmap(QtGui.QPixmap("vs.png"))
        self.monsterpic = QtGui.QLabel("Monster pic")
        self.monsterpic.setPixmap(QtGui.QPixmap(self.cha[1]))
        self.monsterpic.setGraphicsEffect(self.shadow3)
        self.monsterchoose = QtGui.QLabel("Monster Choose")
        self.monsterchoose.setPixmap(QtGui.QPixmap("backCard.png"))
        self.monsterchoose.setGraphicsEffect(self.shadow4)

        self.heroName = QtGui.QLabel("HERO")
        self.heroName.setAlignment(QtCore.Qt.AlignCenter)
        self.heroName.setFixedSize(QtCore.QSize(250,30))
        self.heroName.setStyleSheet("""QLabel{ background:rgb(210, 156, 179);  border-radius:15px;}""")
        self.battle  = QtGui.QPushButton("BATTLE")
        self.battle.setFixedSize(QtCore.QSize(300,25))
        self.battle.setStyleSheet("""QPushButton{ background:white; border-radius:12px;}""")
        self.monsterName = QtGui.QLabel("MONSTER")
        self.monsterName.setAlignment(QtCore.Qt.AlignCenter)
        self.monsterName .setFixedSize(QtCore.QSize(250,30))
        self.monsterName.setStyleSheet("""QLabel{ background:rgb(210, 156, 179);  border-radius:15px;}""")



        self.cardslot1  = QtGui.QLabel("slot 1")
        self.cardslot1.setPixmap(QtGui.QPixmap("backCard.png"))
        self.cardslot1.setFixedSize(QtCore.QSize(220,230))
        self.cardslot1.setGraphicsEffect(self.shadow5)
        self.cardslot2  = QtGui.QLabel("slot 2")
        self.cardslot2.setPixmap(QtGui.QPixmap("backCard.png"))
        self.cardslot2.setFixedSize(QtCore.QSize(220,230))
        self.cardslot2.setGraphicsEffect(self.shadow6)
        self.cardslot3  = QtGui.QLabel("slot 3")
        self.cardslot3.setPixmap(QtGui.QPixmap("backCard.png"))
        self.cardslot3.setFixedSize(QtCore.QSize(220,230))
        self.cardslot3.setGraphicsEffect(self.shadow7)
        self.deck  = QtGui.QLabel("DECK")
        self.deck.setPixmap(QtGui.QPixmap("deck.png"))
        self.deck.setGraphicsEffect(self.shadow)

        self.arrow = QtGui.QLabel("arrow")
        self.arrow.setFixedSize(QtCore.QSize(30,20))
        self.arrow.setPixmap(QtGui.QPixmap("arrow.png"))



    def layout(self):
        self.main_layout = QtGui.QVBoxLayout()
        self.row_title = QtGui.QHBoxLayout()
        self.row_layout  = QtGui.QHBoxLayout()
        self.row_status = QtGui.QHBoxLayout()
        self.row_picUser = QtGui.QHBoxLayout()
        self.row_battle = QtGui.QHBoxLayout()
        self.row_cardplay = QtGui.QHBoxLayout()
        self.arrow_layout = QtGui.QVBoxLayout()
        dialog = QtGui.QDialog()
        self.panel = QtGui.QVBoxLayout()
        self.panel.addWidget(dialog)
        self.row_layout.addWidget(self.processBar1)
        self.row_layout.addWidget(self.turn)
        self.row_layout.addWidget(self.processBar2)

        dialog.setLayout(self.main_layout)
        dialog.setStyleSheet("""QDialog{ background:rgba(156, 179, 210, 200);  border-radius:15px;}""")

        
        self.main_layout.addLayout(self.row_title)
        self.main_layout.addLayout(self.row_layout)
        self.main_layout.addLayout(self.row_status)
        self.main_layout.addLayout(self.row_picUser)
        self.main_layout.addLayout(self.row_battle)
        self.main_layout.addLayout(self.row_cardplay)
        self.main_layout.addLayout(self.arrow_layout)
        self.main_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.main_layout.setAlignment(self.restrat_btn,QtCore.Qt.AlignLeft)
        self.row_title.addWidget(self.titlelabel)
        self.row_title.addWidget(self.restrat_btn)
        self.row_title.addWidget(self.hide_btn)
        self.row_title.addWidget(self.clear_btn)

        self.row_status.addWidget(self.herostatus)
        self.row_status.addWidget(self.monsterstatus)

        self.row_picUser.addWidget(self.heropic)
        self.row_picUser.addWidget(self.herochoose)
        self.row_picUser.addWidget(self.vs)
        self.row_picUser.addWidget(self.monsterchoose)
        self.row_picUser.addWidget(self.monsterpic)
        self.row_picUser.setAlignment(QtCore.Qt.AlignCenter)

        self.row_battle.addWidget(self.heroName)
        self.row_battle.addWidget(self.battle)
        self.row_battle.addWidget(self.monsterName)
        
        self.row_cardplay.addWidget(self.cardslot1)
        self.row_cardplay.addWidget(self.cardslot2)
        self.row_cardplay.addWidget(self.cardslot3)
        self.row_cardplay.addWidget(self.deck)
        self.row_cardplay.setAlignment(QtCore.Qt.AlignCenter)

        self.arrow_layout.addWidget(self.arrow)
        self.arrow_layout.setAlignment(QtCore.Qt.AlignRight)

        self.setLayout(self.panel)

    def connect(self):
        self.hide_btn.clicked.connect(self.hide_fucn)
        self.restrat_btn.clicked.connect(self.restart)
        self.clear_btn.clicked.connect(self.clearFunc)
        self.battle.clicked.connect(self.battleCard)
        self.deck.mouseMoveEvent = self.dragMoveEvent
        self.cardslot1.setAcceptDrops(True)
        self.cardslot2.setAcceptDrops(True)
        self.cardslot3.setAcceptDrops(True)
        self.herochoose.setAcceptDrops(True)

        self.cardslot1.dragEnterEvent = self.dragEvent_c1
        self.cardslot2.dragEnterEvent = self.dragEvent_c2
        self.cardslot3.dragEnterEvent = self.dragEvent_c3
        self.herochoose.dragEnterEvent = self.dragEvent_heroCard

        self.cardslot1.dropEvent = self.dropEvent_c1
        self.cardslot2.dropEvent = self.dropEvent_c2
        self.cardslot3.dropEvent = self.dropEvent_c3
        self.herochoose.dropEvent = self.dropEvent_heroCard

        self.cardslot1.mouseMoveEvent = self.dragMoveEvent_c1
        self.cardslot2.mouseMoveEvent = self.dragMoveEvent_c2
        self.cardslot3.mouseMoveEvent = self.dragMoveEvent_c3
        self.herochoose.mouseMoveEvent = self.dragMoveEvent_heroCard

        self.arrow.mouseMoveEvent = self.scaleF
        self.arrow.enterEvent = self.mouseEnterEvent
        self.arrow.leaveEvent = self.mouseLeaveEvent

    def barhp(self):
        if self.valueH != self.cardGame.hero.hp :
            self.processBar1.setValue(self.valueH)
            if self.valueH >= self.cardGame.hero.hp :
                self.valueH-=1
            elif self.valueH <= self.cardGame.hero.hp :
                self.valueH+=1

        if self.cardGame.bossburn == 0 :
            if self.valueM != self.cardGame.monsterType.hp :
                self.processBar2.setValue(self.valueM)
            if self.valueM >= self.cardGame.monsterType.hp :
                self.valueM-=1
            elif self.valueM <= self.cardGame.monsterType.hp :
                self.valueM+=1
        else :
            if self.check == 0 :
                self.monsterpic.setPixmap(QtGui.QPixmap(self.cha[2]))
                self.processBar2.setMaximum(300)
                self.processBar2.setValue(self.valueB)
                self.herostatus.setText("HERO WIN !! BUT!")
                self.monsterstatus.setText("BOSS APPEAR !!!!") 
                self.herochoose.setPixmap("backCard.png")
                self.heroCard_count = 0
                self.timer.stop()
                self.check = 1
            if self.valueB != self.cardGame.monsterType.hp :
                self.processBar2.setValue(self.valueB)
                if self.valueB >= self.cardGame.monsterType.hp :
                    self.valueB-=1
                elif self.valueB <= self.cardGame.monsterType.hp :
                    self.valueB+=1

        if self.valueH == self.cardGame.hero.hp and self.valueM == self.cardGame.monsterType.hp :
            self.herochoose.setPixmap("backCard.png")
            self.heroCard_count = 0
            self.timer.stop()


    def battleCard(self):
        if self.heroCard_count != 0 :
            self.turn.setText(str(self.cardGame.turn))
            self.cardGame.randomCard(self.cardGame.monsterType)
            self.monsterchoose.setPixmap(QtGui.QPixmap(self.monsCard[self.cardGame.monsterType.selectCard]))
            self.cardGame.hero.selectCard = self.heroCard_count-1
            self.cardGame.start()
            self.herostatus.setText(self.cardGame.statusHero)
            self.monsterstatus.setText(self.cardGame.statusMons) 
            self.timer.start()


    def timer(self):
        self.valueH = 300
        self.valueM = 150
        self.valueB = 300
        self.timer = QtCore.QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.barhp)

    def clearFunc(self):
        self.close()


    def dropEvent(self,event):
        if event.mimeData().hasUrls() :
            event.accept()
            urls = event.mimeData().urls()

        elif event.mimeData().hasText() :
            event.accept()

        else :
            event.ignore()
    def keyPressEvent(self,event):
        key = event.key()
        if key == 16777216 :
            self.close()
    def mousePressEvent(self,event):
        self.moving = True 
        self.mouseClick = event.pos()
    def mouseMoveEvent(self,event):
        if self.moving :
            self.move(event.globalPos()-self.mouseClick)

            
    def mouseEnterEvent(self,event):
        self.setCursor(QtCore.Qt.SizeFDiagCursor)
    def mouseLeaveEvent(self,event):
        self.setCursor(QtCore.Qt.ArrowCursor)



    def dragMoveEvent(self,event):
        mimeData = QtCore.QMimeData()
        mimeData.setText(self.backCard)

        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(event.pos()-self.deck.rect().topLeft())

        pixmap = QtGui.QPixmap(self.backCard)

        drag.setPixmap(pixmap)
        drag.start(QtCore.Qt.MoveAction)
    def dragEvent_c1(self,event):
        if self.c1_count == 0:
            event.accept()
    def dragEvent_c2(self,event):
        if self.c2_count == 0:
            event.accept()
    def dragEvent_c3(self,event):
        if self.c3_count == 0:
            event.accept()
    def dragEvent_heroCard(self,event):
        if self.heroCard_count == 0:
            event.accept()

    def dropEvent_c1(self,event):
        text = event.mimeData().text()
        if text == "card.png":
            if event.mimeData().hasText():
                event.accept()
                ran = random.randint(1,4)
                if ran == 1 :
                    text = self.heroCard[0]
                elif ran == 2 :
                    text = self.heroCard[1]
                elif ran == 3 :
                    text = self.heroCard[2]
                elif ran == 4 :
                    text = self.heroCard[3]
  
                self.cardslot1.setPixmap(text)
                self.c1_count = ran

            else:
                event.ignore()

        elif text != "card.png":
            if event.mimeData().hasText():
                event.accept()
                #text = event.mimeData().text()

                self.cardslot1.setPixmap(text)
                if text == self.heroCard[0]:
                    self.c1_count = 1
                elif text == self.heroCard[1]:
                    self.c1_count = 2
                elif text == self.heroCard[2]:
                    self.c1_count = 3
                elif text == self.heroCard[3]:
                    self.c1_count = 4

                if self.c2_switch == 1 :
                    self.cardslot2.setPixmap("backCard.png")
                    self.c2_switch = 0
                    self.c2_count = 0
                elif self.c3_switch == 1 :
                    self.cardslot3.setPixmap("backCard.png")
                    self.c3_switch = 0
                    self.c3_count = 0
                elif self.heroCard_switch == 1 :
                    self.herochoose.setPixmap("backCard.png")
                    self.heroCard_switch = 0
                    self.heroCard_count = 0
        else:
            event.ignore()
    def dropEvent_c2(self,event):
        text = event.mimeData().text()
        if text == "card.png":
            if event.mimeData().hasText():
                event.accept()
                ran = random.randint(1,4)
                #text = event.mimeData().text()
                if ran == 1 :
                    text = self.heroCard[0]
                elif ran == 2 :
                    text = self.heroCard[1]
                elif ran == 3 :
                    text = self.heroCard[2]
                elif ran == 4 :
                    text = self.heroCard[3]

                self.cardslot2.setPixmap(text)
                self.c2_count = ran

            else:
                event.ignore()

        elif text != "card.png":
            if event.mimeData().hasText():
                event.accept()
                #text = event.mimeData().text()

                self.cardslot2.setPixmap(text)
                if text == self.heroCard[0]:
                    self.c2_count = 1
                elif text == self.heroCard[1]:
                    self.c2_count = 2
                elif text == self.heroCard[2]:
                    self.c2_count = 3
                elif text == self.heroCard[3]:
                    self.c2_count = 4

                if self.c1_switch == 1 :
                    self.cardslot1.setPixmap("backCard.png")
                    self.c1_switch = 0
                    self.c1_count = 0
                elif self.c3_switch == 1 :
                    self.cardslot3.setPixmap("backCard.png")
                    self.c3_switch = 0
                    self.c3_count = 0
                elif self.heroCard_switch == 1 :
                    self.herochoose.setPixmap("backCard.png")
                    self.heroCard_switch = 0
                    self.heroCard_count = 0
        else:
            event.ignore()
    def dropEvent_c3(self,event):
        text = event.mimeData().text()
        if text == "card.png":
            if event.mimeData().hasText():
                event.accept()
                ran = random.randint(1,4)
                #text = event.mimeData().text()
                if ran == 1 :
                    text = self.heroCard[0]
                elif ran == 2 :
                    text = self.heroCard[1]
                elif ran == 3 :
                    text = self.heroCard[2]
                elif ran == 4 :
                    text = self.heroCard[3]

                self.cardslot3.setPixmap(text)
                self.c3_count = ran

            else:
                event.ignore()

        elif text != "card.png":
            if event.mimeData().hasText():
                event.accept()
                #text = event.mimeData().text()

                self.cardslot3.setPixmap(text)
                if text == self.heroCard[0]:
                    self.c3_count = 1
                elif text == self.heroCard[1]:
                    self.c3_count = 2
                elif text == self.heroCard[2]:
                    self.c3_count = 3
                elif text == self.heroCard[3]:
                    self.c3_count = 4

                if self.c2_switch == 1 :
                    self.cardslot2.setPixmap("backCard.png")
                    self.c2_switch = 0
                    self.c2_count = 0
                elif self.c1_switch == 1 :
                    self.cardslot1.setPixmap("backCard.png")
                    self.c1_switch = 0
                    self.c1_count = 0
                elif self.heroCard_switch == 1 :
                    self.herochoose.setPixmap("backCard.png")
                    self.heroCard_switch = 0
                    self.heroCard_count = 0
        else:
            event.ignore()
    def dropEvent_heroCard(self,event):
        text = event.mimeData().text()
        if text != "card.png":
            if event.mimeData().hasText():
                event.accept()
                #text = event.mimeData().text()

                self.herochoose.setPixmap(text)
                if text == self.heroCard[0]:
                    self.heroCard_count = 1
                elif text == self.heroCard[1]:
                    self.heroCard_count = 2
                elif text == self.heroCard[2]:
                    self.heroCard_count = 3
                elif text == self.heroCard[3]:
                    self.heroCard_count = 4

                if self.c2_switch == 1 :
                    self.cardslot2.setPixmap("backCard.png")
                    self.c2_switch = 0
                    self.c2_count = 0
                elif self.c3_switch == 1 :
                    self.cardslot3.setPixmap("backCard.png")
                    self.c3_switch = 0
                    self.c3_count = 0
                elif self.c1_switch == 1 :
                    self.cardslot1.setPixmap("backCard.png")
                    self.c1_switch = 0
                    self.c1_count = 0
                print self.heroCard_count 

            else:
                event.ignore()


    def dragMoveEvent_c1(self,event):
        if self.c1_count != 0 :
            self.c1_switch=1
            self.c2_switch=0
            self.c3_switch=0
            self.heroCard_switch=0

            if self.c1_count == 1:
                pic = self.heroCard[0]
            elif self.c1_count == 2:
                pic = self.heroCard[1]
            elif self.c1_count == 3:
                pic = self.heroCard[2]
            elif self.c1_count == 4:
                pic = self.heroCard[3]

            mimeData = QtCore.QMimeData()
            mimeData.setText(pic)
            #self.cardslot1.setPixmap("backCard.png")
            drag = QtGui.QDrag(self)
            drag.setMimeData(mimeData)
            drag.setHotSpot(event.pos()-self.deck.rect().topLeft())

            pixmap = QtGui.QPixmap(pic)

            drag.setPixmap(pixmap)
            drag.start(QtCore.Qt.MoveAction)


        else :
            event.ignore()
    def dragMoveEvent_c2(self,event):

        if self.c2_count != 0 :
            self.c1_switch=0
            self.c2_switch=1
            self.c3_switch=0
            self.heroCard_switch=0
            if self.c2_count == 1:
                pic = self.heroCard[0]
            elif self.c2_count == 2:
                pic = self.heroCard[1]
            elif self.c2_count == 3:
                pic = self.heroCard[2]
            elif self.c2_count == 4:
                pic = self.heroCard[3]
            mimeData = QtCore.QMimeData()
            mimeData.setText(pic)

            drag = QtGui.QDrag(self)
            drag.setMimeData(mimeData)
            drag.setHotSpot(event.pos()-self.deck.rect().topLeft())

            pixmap = QtGui.QPixmap(pic)

            drag.setPixmap(pixmap)
            drag.start(QtCore.Qt.MoveAction)
                
        else :
            event.ignore()            
    def dragMoveEvent_c3(self,event):

        if self.c3_count != 0 :
            self.c1_switch=0
            self.c2_switch=0
            self.c3_switch=1
            self.heroCard_switch=0
            if self.c3_count == 1:
                pic = self.heroCard[0]
            elif self.c3_count == 2:
                pic = self.heroCard[1]
            elif self.c3_count == 3:
                pic = self.heroCard[2]
            elif self.c3_count == 4:
                pic = self.heroCard[3]
            mimeData = QtCore.QMimeData()
            mimeData.setText(pic)

            drag = QtGui.QDrag(self)
            drag.setMimeData(mimeData)
            drag.setHotSpot(event.pos()-self.deck.rect().topLeft())

            pixmap = QtGui.QPixmap(pic)

            drag.setPixmap(pixmap)
            drag.start(QtCore.Qt.MoveAction)
                
        else :
            event.ignore()
    def dragMoveEvent_heroCard(self,event):
        
        if self.heroCard_count != 0 :
            self.c1_switch=0
            self.c2_switch=0
            self.c3_switch=0
            self.heroCard_switch=1
            if self.heroCard_count == 1:
                pic = self.heroCard[0]
            elif self.heroCard_count == 2:
                pic = self.heroCard[0]
            elif self.heroCard_count == 3:
                pic = self.heroCard[2]
            elif self.heroCard_count == 4:
                pic = self.heroCard[3]

            #self.setCursor(QtCore.Qt.DragCopyCursor)
            #self.setCursor(self.blank)
            #event.setDragCursor(self.blank)
            mimeData = QtCore.QMimeData()
            mimeData.setText(pic)

            drag = QtGui.QDrag(self)
            drag.setMimeData(mimeData)
            drag.setHotSpot(event.pos()-self.deck.rect().topLeft())

            pixmap = QtGui.QPixmap(pic)
            #pixmap = pixmap.scaled(100,100 , aspectMode=QtCore.Qt.IgnoreAspectRatio , mode=QtCore.Qt.FastTrbansformation )

            drag.setPixmap(pixmap)
            drag.start(QtCore.Qt.MoveAction)

        else :
            event.ignore()



    def scaleF(self,event):

        x = event.x()
        y = event.y()
        self.w += x
        self.h += y
        print x
        print y
        self.setFixedSize(QtCore.QSize(self.w,self.h))
    def hide_fucn(self):
        self.showMinimized()
    def restart(self):
        reload(GameFuc)
        self.close()
        c = TestEvent()
        c.show()


app = QtGui.QApplication(sys.argv)
window = TestEvent()


window.show()
app.exec_()

