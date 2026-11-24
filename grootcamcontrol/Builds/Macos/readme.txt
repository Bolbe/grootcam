Download qt opensource 6.5.3
https://download.qt.io/archive/qt/6.5/6.5.3/single/qt-everywhere-src-6.5.3.tar.xz

brew install cmake
brew install ninja

tar -xf qt-everywhere-src-6.5.3.tar.xz
cd qt-everywhere-src-6.5.3

rm -rf qtquickeffectmaker qtgrpc qtscxml qtnetworkauth qt5compat qt3d qtactiveqt qtcharts qtcoap qtconnectivity qtdatavis3d qtlanguageserver qtlocation qtmqtt qtlottie qtmultimedia qtopcua qtpositioning qtremoteobjects qtsensors qtserialbus qtserialport qtvirtualkeyboard qtwayland qttools qtwebengine qtdoc qtspeech qttranslations qtwebview qtwebchannel qtwebsockets qthttpserver
Warning: keep qtQuick3d and its dependencies (shadertools, physics) because QtQuick needs quick3d !
In the end, keep:
drwx------  31 gargamel  staff   992B Sep 25 19:00 qtbase
drwx------  23 gargamel  staff   736B Sep 25 19:00 qtdeclarative
drwx------  17 gargamel  staff   544B Sep 25 19:00 qtimageformats
drwx------  23 gargamel  staff   736B Sep 25 19:00 qtquick3d
drwx------  18 gargamel  staff   576B Sep 25 19:00 qtquick3dphysics
drwx------  14 gargamel  staff   448B Sep 25 19:00 qtquicktimeline
drwx------  14 gargamel  staff   448B Sep 25 19:00 qtshadertools
drwx------  15 gargamel  staff   480B Sep 25 19:00 qtsvg

./configure -opensource -nomake tests -nomake examples -no-icu -confirm-license -no-dbus -sql-sqlite
cmake --build . --parallel
sudo cmake --install .

cd grootcam/grootcamcontrol/

run build-macos.sh

or:

mkdir tmp
cd tmp
/usr/local/Qt-6.5.3/bin/qmake ..
make

/usr/local/Qt-6.5.3/bin/macdeployqt ./GrootcamControl.app -qmldir=/usr/local/Qt-6.5.3/qml

rm unused folder. Keep:

.
└── Contents
    ├── Frameworks
    │   ├── QtCore.framework
    │   ├── QtGui.framework
    │   ├── QtNetwork.framework
    │   ├── QtOpenGL.framework
    │   ├── QtQml.framework
    │   ├── QtQmlModels.framework
    │   ├── QtQmlWorkerScript.framework
    │   ├── QtQuick.framework
    │   ├── QtQuickControls2.framework
    │   ├── QtQuickControls2Impl.framework
    │   └── QtQuickTemplates2.framework
    ├── Info.plist
    ├── MacOS
    │   └── GrootcamControl
    ├── PkgInfo
    ├── PlugIns
    │   ├── platforms
    │   │   └── libqcocoa.dylib
    │   └── quick
    │       ├── libqtquick2plugin.dylib
    │       ├── libqtquickcontrols2basicstyleimplplugin.dylib
    │       ├── libqtquickcontrols2basicstyleplugin.dylib
    │       ├── libqtquickcontrols2fusionstyleimplplugin.dylib
    │       ├── libqtquickcontrols2fusionstyleplugin.dylib
    │       ├── libqtquickcontrols2implplugin.dylib
    │       ├── libqtquickcontrols2macosstyleplugin.dylib
    │       ├── libqtquickcontrols2materialstyleimplplugin.dylib
    │       ├── libqtquickcontrols2materialstyleplugin.dylib
    │       ├── libqtquickcontrols2plugin.dylib
    │       ├── libqtquicktemplates2plugin.dylib
    │       └── libworkerscriptplugin.dylib
    └── Resources
        ├── empty.lproj
        ├── qml
        │   ├── QtQml
        │   │   ├── WorkerScript
        │   │   ├── libqmlplugin.dylib -> ../../../PlugIns/quick/libqmlplugin.dylib
        │   │   ├── plugins.qmltypes
        │   │   └── qmldir
        │   └── QtQuick
        │       ├── Controls
        │       │   ├── Basic
        │       │   ├── Fusion
        │       │   ├── Material
        │       │   ├── macOS
        │       ├── Templates
        │       │   ├── libqtquicktemplates2plugin.dylib -> ../../../../PlugIns/quick/libqtquicktemplates2plugin.dylib
        │       │   ├── plugins.qmltypes
        │       │   └── qmldir
        │       ├── libqtquick2plugin.dylib -> ../../../PlugIns/quick/libqtquick2plugin.dylib
        │       ├── plugins.qmltypes
        │       └── qmldir
        └── qt.conf

