# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainrvpJdh.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt,)
from PySide2.QtGui import ( QFont, QIcon, QPixmap, )
from PySide2.QtWidgets import *

from upload_file_region import UploadFileRegion

from image_uploader import ImageUploader

appVersion = "0.6"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        # Main Window stylesheet path
        self.main_styles_path = "./styles/main_styles.css"

        MainWindow.resize(1150, 840)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: #EAEAEA;")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        # self.Top_Bar = QFrame(self.centralwidget)
        # self.Top_Bar.setObjectName(u"Top_Bar")
        # self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        # self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        # self.Top_Bar.setFrameShape(QFrame.NoFrame)
        # self.Top_Bar.setFrameShadow(QFrame.Raised)

        # self.horizontalLayout = QHBoxLayout(self.centralwidget)
        # self.horizontalLayout.setObjectName(u"horizontalLayout")
        # self.horizontalLayout.setSpacing(0)
        # self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        #self.verticalLayout.addWidget(self.Top_Bar)


        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)

        self.mainWindowHLayout = QHBoxLayout( self.Content )
        self.mainWindowHLayout.setObjectName(u"mainWindowHLayout")
        self.mainWindowHLayout.setSpacing(0)
        self.mainWindowHLayout.setContentsMargins(0, 0, 0, 0)


        # Sidebar menu layout setup
        self.sidebarMenuFrame = QFrame( self.Content )
        self.sidebarMenuFrame.setObjectName(u"sidebarMenuFrame")
        # self.sidebarMenuFrame.setMinimumSize(QSize(220, 0))
        # self.sidebarMenuFrame.setMaximumSize(QSize(250, 4000))
        self.sidebarMenuFrame.setStyleSheet(u"background-color: #A5A5A5;")
        # self.sidebarMenuFrame.setFrameShape(QFrame.StyledPanel)
        # self.sidebarMenuFrame.setFrameShadow(QFrame.Raised)

        self.sidebarMenuVLayout = QVBoxLayout( self.sidebarMenuFrame )
        self.sidebarMenuVLayout.setObjectName( "sidebarMenuVLayout" )
        self.sidebarMenuVLayout.setSpacing( 8 )
        self.sidebarMenuVLayout.setContentsMargins( 2, 2, 2, 2 )



        # ---------------------------------------------------------------------------------------
        # Setting up page-routing buttons in menu sidebar

        # Page 1 (Welcome landing page, isActive on app launch)
        self.btn_page_1 = QPushButton( self.sidebarMenuFrame )
        self.btn_page_1.setObjectName( "btn_page_1" )
        self.btn_page_1.setProperty( "isActivePage", True )
        self.btn_page_1.setMinimumSize( QSize( 0, 48 ) )

        # Page 2 (Upload LDR images)
        self.btn_page_2 = QPushButton( self.sidebarMenuFrame )
        self.btn_page_2.setObjectName( "btn_page_2" )
        self.btn_page_2.setProperty( "isActivePage", False )
        self.btn_page_2.setMinimumSize( QSize( 0, 48 ) )

        # Page 3 (Adjust camera settings)
        self.btn_page_3 = QPushButton( self.sidebarMenuFrame )
        self.btn_page_3.setObjectName( "btn_page_3" )
        self.btn_page_2.setProperty( "isActivePage", False )
        self.btn_page_3.setMinimumSize( QSize( 0, 48 ) )

        # Page 4 (Adjust calibration settings)
        self.btn_page_4 = QPushButton( self.sidebarMenuFrame )
        self.btn_page_4.setObjectName( "btn_page_4" )
        self.btn_page_4.setProperty( "isActivePage", False )
        self.btn_page_4.setMinimumSize( QSize( 0, 48 ) )

        # Go button - Starts Radiance pipeline process
        self.btn_start_pipeline = QPushButton( self.sidebarMenuFrame )
        self.btn_start_pipeline.setObjectName( "btn_start_pipeline" )
        self.btn_start_pipeline.setProperty( "isActivePage", False )
        self.btn_start_pipeline.setMinimumSize( QSize( 0, 64 ) )
        
        # TODO
        # Add spacer here after GO btn
        # Then add button for Settings page
        # Then add Help Button
        # Then add QLabel for where we put version number

        
        self.btn_help = QPushButton(self.sidebarMenuFrame)
        self.btn_help.setObjectName(u"btn_help")
        self.btn_help.move(0,1000)
        self.btn_help.setStyleSheet("background-color: #2E8BC0")
        self.btn_help.setMinimumSize(QSize(0, 40))
        self.btn_help.setIcon( QIcon("./assets/icons/help-icon.png") )
        
        
        

        # Default active page
        self.activePage = self.btn_page_1

        self.btn_page_1.clicked.connect( lambda: self.setActivePage( self.btn_page_1 ) )
        self.btn_page_2.clicked.connect( lambda: self.setActivePage( self.btn_page_2 ) )
        self.btn_page_3.clicked.connect( lambda: self.setActivePage( self.btn_page_3 ) )
        self.btn_page_4.clicked.connect( lambda: self.setActivePage( self.btn_page_4 ) )
        
        self.btn_start_pipeline.clicked.connect( lambda: self.setActivePage( self.btn_start_pipeline ) )
        self.btn_help.clicked.connect( lambda: self.setActivePage( self.btn_help ) )
        # Add page-routing buttons to sidebar
        self.sidebarMenuVLayout.addWidget( self.btn_page_1, stretch=1 )
        self.sidebarMenuVLayout.addWidget( self.btn_page_2, stretch=1 )
        self.sidebarMenuVLayout.addWidget( self.btn_page_3, stretch=1 )
        self.sidebarMenuVLayout.addWidget( self.btn_page_4, stretch=1 )
        self.sidebarMenuVLayout.addWidget( self.btn_start_pipeline, stretch=1 )
        self.sidebarMenuVLayout.addWidget( self.btn_help, stretch=1 )

        settingsBtn = QPushButton( "Settings", self.sidebarMenuFrame)
        settingsBtn.setMinimumSize( QSize( 0, 52 ) )
        settingsBtn.setGeometry(0,0, 200, 30)
        settingsBtn.setStyleSheet( "background-color: #D9D9D9;" )
        settingsBtn.setIcon( QIcon("./assets/icons/settings-icon.png") )

        self.sidebarMenuVLayout.addWidget( settingsBtn, stretch=2 )

        appVersionLabel = "Version: {}".format( appVersion )
        self.versionLabel = QLabel( appVersionLabel )
        self.sidebarMenuVLayout.addWidget( self.versionLabel, stretch=1, alignment=Qt.AlignBottom )

        # Set style of sidebar menu buttons
        self.setButtonStyling()

        # ---------------------------------------------------------------------------------------

        

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")


        self.mainWindowHLayout.addWidget( self.sidebarMenuFrame, stretch=2 )
        self.mainWindowHLayout.addWidget( self.frame_pages, stretch=9 )

        self.Content.setLayout( self.mainWindowHLayout )


        # -------------------------------------------------------------------------------------------------
        # Page 1 Setup
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_1 = QLabel(self.page_1)
        self.label_1.setObjectName(u"label_1")
        font = QFont()
        font.setPointSize(40)
        labelfont = QFont()
        labelfont.setPointSize(20)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet(u"color: #000;")
        self.label_1.setAlignment(Qt.AlignCenter)
        self.verticalLayout_7.addWidget(self.label_1)
        


        self.label_p1 = QLabel(self.page_1)
        self.welcomeImagePixmap = QPixmap('./assets/images/officeteamstock.jpg')

        self.label_p1.setPixmap(self.welcomeImagePixmap)
        self.label_p1.setAlignment(Qt.AlignCenter)
        self.label_p1.resize(self.welcomeImagePixmap.width(), self.welcomeImagePixmap.height())

        self.label_p1.move(130,300)
        
        self.label_p1_title = QLabel(self.page_1)
        self.label_p1_title.setText("Meet The Team!")
        self.label_p1_title.setStyleSheet("font: 16pt \".AppleSystemUIFont\";")
        self.label_p1_title.adjustSize()
        self.label_p1_title.move(350,720)
        
        self.label_p1.show()

        self.intro_para = QLabel(self.page_1)
        self.intro_para.setAlignment(Qt.AlignHCenter)
        self.intro_para.setText("The HDRI Lighting Calibration Tool is a free, open-source \n application developed by a small team of students \n from Oregon State Univeristy.")
        self.intro_para.setFont(labelfont)
        self.intro_para.adjustSize()
        self.intro_para.setStyleSheet("font: 18pt \".AppleSystemUIFont\";")
        self.intro_para.move(20,20)
        self.intro_para.move(100,100)

        # -------------------------------------------------------------------------------------------------


        
        # ------------------------------------------------------------------------------------------------------------
        # Page 2 Setup
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_Vlayout = QVBoxLayout(self.page_2)
        self.page_2_Vlayout.setObjectName(u"page_2_Vlayout")
        self.page_2_Vlayout.setSpacing(0)
        self.page_2_Vlayout.setContentsMargins(0, 0, 0, 0)
        
        uploader = ImageUploader()

        self.page_2_Vlayout.addWidget( uploader, stretch=1 )
        
        # -------------------------------------------------------------------------------------------------



        # ----------------------------------------------------------------------------------------
        # Page 3 setup
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")

        self.cameraSettingsPage = QVBoxLayout(self.page_3)
        self.cameraSettingsPage.setObjectName(u"cameraSettingsPage")
        self.cameraSettingsPage.setContentsMargins( 0, 0, 0, 0 )
        self.cameraSettingsPage.setSpacing( 4 )
        self.cameraSettingsPage.setMargin( 0 )

        
        # Cropping Area mdiArea
        self.mdiArea = QMdiArea(self.page_3)
        #self.mdiArea.setGeometry(QRect(10, 10, 970, 250))
        self.mdiArea.setObjectName("mdiArea_2")

        self.label_cd = QLabel(self.mdiArea)
        self.label_cd.setAlignment(Qt.AlignLeft)
        self.label_cd.setText("Cropping Dimensions")
        self.label_cd.setFont(labelfont)
        self.label_cd.adjustSize()
        self.label_cd.setStyleSheet("font: 18pt \".AppleSystemUIFont\";")
        self.label_cd.setStyleSheet("background-color: #a0a0a0")
        self.label_cd.move(10,10)


        # Viewing angles mdiArea
        self.mdiArea_2 = QMdiArea(self.page_3)
        #self.mdiArea_2.setGeometry(QRect(10, 290, 970, 140))
        self.mdiArea_2.setObjectName("mdiArea_2")

        self.label_LVA = QLabel(self.mdiArea_2)
        self.label_LVA.setAlignment(Qt.AlignLeft)
        self.label_LVA.setText("Lens Viewing Angle")
        self.label_LVA.setFont(labelfont)
        self.label_LVA.adjustSize()
        self.label_LVA.setStyleSheet("font: 18pt \".AppleSystemUIFont\";")
        self.label_LVA.setStyleSheet("background-color: #a0a0a0")
        self.label_LVA.move(10,10)
        self.label_LVA.raise_()


        # Output Dimensions mdiArea
        self.mdiArea_3 = QMdiArea(self.page_3)
        #self.mdiArea_3.setGeometry(QRect(10, 460, 970, 140))
        self.mdiArea_3.setObjectName("mdiArea_3")

        self.label_OID = QLabel(self.mdiArea_3)
        self.label_OID.setAlignment(Qt.AlignLeft)
        self.label_OID.setText("Output Image Dimensions")
        self.label_OID.setFont(labelfont)
        self.label_OID.adjustSize()
        self.label_OID.setStyleSheet("font: 18pt \".AppleSystemUIFont\";")
        self.label_OID.setStyleSheet("background-color: #a0a0a0")
        self.label_OID.move(10,10)
        self.label_OID.raise_()


        #mdi area 1 line edits 
        self.lineEdit_md11 = QLineEdit(self.mdiArea)
        self.lineEdit_md11.setText("")
        self.lineEdit_md11.setObjectName("lineEdit_md11")
        self.lineEdit_md11.move(10,100)


        self.lineEdit_md12 = QLineEdit(self.mdiArea)
        self.lineEdit_md12.setText("")
        self.lineEdit_md12.setObjectName("lineEdit_md12")
        self.lineEdit_md12.move(160,100)


        self.label_md11 = QLabel(self.mdiArea)
        self.label_md11.setAlignment(Qt.AlignLeft)
        self.label_md11.setText("x")
        self.label_md11.setStyleSheet("background-color: #a0a0a0")
        self.label_md11.move(149,102)


        self.label_iir = QLabel(self.mdiArea)
        self.label_iir.setAlignment(Qt.AlignLeft)
        self.label_iir.setText("Input Image Resolution")
        self.label_iir.setStyleSheet("background-color: #a0a0a0")
        self.label_iir.move(10,70)

        self.lineEdit_md13 = QLineEdit(self.mdiArea)
        self.lineEdit_md13.setText("")
        self.lineEdit_md13.setObjectName("lineEdit_md13")
        self.lineEdit_md13.move(10,160)

        self.label_md13 = QLabel(self.mdiArea)
        self.label_md13.setAlignment(Qt.AlignLeft)
        self.label_md13.setText("Fisheye View Diameter")
        self.label_md13.setStyleSheet("background-color: #a0a0a0")
        self.label_md13.move(10,140)

        self.label_md14 = QLabel(self.mdiArea)
        self.label_md14.setAlignment(Qt.AlignLeft)
        self.label_md14.setText("X Crop Offset")
        self.label_md14.setStyleSheet("background-color: #a0a0a0")
        self.label_md14.move(500,70)

        self.lineEdit_md14 = QLineEdit(self.mdiArea)
        self.lineEdit_md14.setText("")
        self.lineEdit_md14.setObjectName("lineEdit_md14")
        self.lineEdit_md14.move(500,100)

        self.label_md15 = QLabel(self.mdiArea)
        self.label_md15.setAlignment(Qt.AlignLeft)
        self.label_md15.setText("Y Crop Offset")
        self.label_md15.setStyleSheet("background-color: #a0a0a0")
        self.label_md15.move(500,140)

        self.lineEdit_md15 = QLineEdit(self.mdiArea)
        self.lineEdit_md15.setText("")
        self.lineEdit_md15.setObjectName("lineEdit_md15")
        self.lineEdit_md15.move(500,160)

        self.area1button = QPushButton('Enter', self.mdiArea)
        self.area1button.move(750,160)
        #area1button.clicked.connect(self.on_click)

        #area 2 edit 
        self.lineEdit_md21 = QLineEdit(self.mdiArea_2)
        self.lineEdit_md21.setText("")
        self.lineEdit_md21.setObjectName("lineEdit_md21")
        self.lineEdit_md21.move(10,90)

        self.label_md21 = QLabel(self.mdiArea_2)
        self.label_md21.setAlignment(Qt.AlignLeft)
        self.label_md21.setText("View Angle Vertical")
        self.label_md21.setStyleSheet("background-color: #a0a0a0")
        self.label_md21.move(10,70)

        self.label_md22 = QLabel(self.mdiArea_2)
        self.label_md22.setAlignment(Qt.AlignLeft)
        self.label_md22.setText("View Angle Horizontal")
        self.label_md22.setStyleSheet("background-color: #a0a0a0")
        self.label_md22.move(250,70)

        self.lineEdit_md22 = QLineEdit(self.mdiArea_2)
        self.lineEdit_md22.setText("")
        self.lineEdit_md22.setObjectName("lineEdit_md22")
        self.lineEdit_md22.move(250,90)

        self.area2button = QPushButton('Enter', self.mdiArea_2)
        self.area2button.move(750,160)

        #area 3 edit
        self.label_md31 = QLabel(self.mdiArea_3)
        self.label_md31.setAlignment(Qt.AlignLeft)
        self.label_md31.setText("HDR Image Output Resolution")
        self.label_md31.setStyleSheet("background-color: #a0a0a0")
        self.label_md31.move(10,70)

        self.lineEdit_md31 = QLineEdit(self.mdiArea_3)
        self.lineEdit_md31.setText("")
        self.lineEdit_md31.setObjectName("lineEdit_md31")
        self.lineEdit_md31.move(10,90)

        self.label_md31x = QLabel(self.mdiArea_3)
        self.label_md31x.setAlignment(Qt.AlignLeft)
        self.label_md31x.setText("x")
        self.label_md31x.setStyleSheet("background-color: #a0a0a0")
        self.label_md31x.move(149,92)

        self.lineEdit_md32 = QLineEdit(self.mdiArea_3)
        self.lineEdit_md32.setText("")
        self.lineEdit_md32.setObjectName("lineEdit_md32")
        self.lineEdit_md32.move(160,90)

        self.area3button = QPushButton('Enter', self.mdiArea_3)
        self.area3button.move(750,160)

        # Area 4 upload .rsp file region
        rsp_uploadarea = UploadFileRegion("CameraResponseFileUpload", [900, 200], fileType=2 )


        # Add widgets to Layout
        self.cameraSettingsPage.addWidget( self.mdiArea, stretch=1 )
        self.cameraSettingsPage.addWidget( self.mdiArea_2, stretch=1 )
        self.cameraSettingsPage.addWidget( self.mdiArea_3, stretch=1 )
        self.cameraSettingsPage.addWidget( rsp_uploadarea, stretch=1 )
        
        # -------------------------------------------------------------------------------------------------



        # -------------------------------------------------------------------------------------------------
        # Page 4 Setup
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")


        # Upload file regions
        # Create new layout for self.page_4
        self.calibrationPage = QVBoxLayout( self.page_4 )
        self.calibrationPage.setObjectName( "calibrationPage" )
        self.calibrationPage.setContentsMargins( 0, 0, 0, 0 )
        self.calibrationPage.setSpacing( 4 )
        self.calibrationPage.setMargin( 0 )
        

        # Vignetting region
        # Add widget: UploadFileRegionObject class object
        vc_UploadRegion = UploadFileRegion( "Vignetting", [900, 200], fileType=1 )

        # Add vignetting UploadRegion object to the QVBox
        self.calibrationPage.addWidget( vc_UploadRegion )

        # Fisheye correction region
        # Add widget: UploadFileRegionObject class object
        fc_UploadRegion = UploadFileRegion( "FisheyeCorrection", [900, 200], fileType=1 )

        # Add vignetting UploadRegion object to the QVBox
        self.calibrationPage.addWidget( fc_UploadRegion )

        # Camera factor region
        # Add widget: UploadFileRegionObject class object
        cf_UploadRegion = UploadFileRegion( "CameraFactor", [900, 200], fileType=1 )

        # Add vignetting UploadRegion object to the QVBox
        self.calibrationPage.addWidget( cf_UploadRegion )

        # Neutral Density Filter region
        # Add widget: UploadFileRegionObject class object
        nd_UploadRegion = UploadFileRegion( "NeutralDensityFilter", [900, 200], fileType=1 )

        # Add vignetting UploadRegion object to the QVBox
        self.calibrationPage.addWidget( nd_UploadRegion )

        # -------------------------------------------------------------------------------------------------


        # -------------------------------------------------------------------------------------------------
        # Page 5 setup

        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_10 = QVBoxLayout(self.page_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_5 = QLabel(self.page_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: #000;")
        self.label_5.setAlignment(Qt.AlignCenter)

        # -------------------------------------------------------------------------------------------------



        self.verticalLayout_10.addWidget(self.label_5)

        # Add pages to multi-page view stackedWidget
        self.stackedWidget.addWidget(self.page_1)
        self.stackedWidget.addWidget(self.page_2)
        self.stackedWidget.addWidget(self.page_3)
        self.stackedWidget.addWidget(self.page_4)
        self.stackedWidget.addWidget(self.page_5)


        self.verticalLayout_5.addWidget(self.stackedWidget)
        
        # self.mainWindowHLayout.addWidget(self.frame_pages)

        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"HDRI Calibration Tool", None))
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"Upload LDR images", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"Camera Settings", None))
        self.btn_page_4.setText(QCoreApplication.translate("MainWindow", u"Upload Calibration", None))
        self.btn_start_pipeline.setText(QCoreApplication.translate("MainWindow", u"GO!", None))
        self.btn_help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Welcome!", None))
        self.label_1.setAlignment(Qt.AlignHCenter)
       # self.label_2.setText(QCoreApplication.translate("MainWindow", u"LDR Image Upload Page", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Processing...", None))


    # Sets the active page based on sidebar menu button clicks
    def setActivePage( self, newActiveBtn ):
        # Set attribute
        self.activePage = newActiveBtn

        self.btn_page_1.setProperty( "isActivePage", False )
        self.btn_page_2.setProperty( "isActivePage", False )
        self.btn_page_3.setProperty( "isActivePage", False )
        self.btn_page_4.setProperty( "isActivePage", False )
        self.btn_start_pipeline.setProperty( "isActivePage", False )

        if ( newActiveBtn.objectName() == "btn_page_1" ):
            self.btn_page_1.setProperty( "isActivePage", True )
        elif  ( newActiveBtn.objectName() == "btn_page_2" ):
            self.btn_page_2.setProperty( "isActivePage", True )
        elif  ( newActiveBtn.objectName() == "btn_page_3" ):
            self.btn_page_3.setProperty( "isActivePage", True )
        elif  ( newActiveBtn.objectName() == "btn_page_4" ):
            self.btn_page_4.setProperty( "isActivePage", True )
        elif  ( newActiveBtn.objectName() == "btn_start_pipeline" ):
            self.btn_start_pipeline.setProperty( "isActivePage", True )
        else:
            print( "newActiveBtn: {}".format( newActiveBtn.objectName() ) )

        self.setButtonStyling()

        return

    
    # Set sidebar menu button styling
    def setButtonStyling( self ):
        with open( self.main_styles_path, "r" ) as stylesheet:
            self.btn_page_1.setStyleSheet( stylesheet.read() )
        with open( self.main_styles_path, "r" ) as stylesheet:
            self.btn_page_2.setStyleSheet( stylesheet.read() )
        with open( self.main_styles_path, "r" ) as stylesheet:
            self.btn_page_3.setStyleSheet( stylesheet.read() )
        with open( self.main_styles_path, "r" ) as stylesheet:
            self.btn_page_4.setStyleSheet( stylesheet.read() )
        with open( self.main_styles_path, "r" ) as stylesheet:
            self.btn_start_pipeline.setStyleSheet( stylesheet.read() )
