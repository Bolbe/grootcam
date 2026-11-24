# Run this script by docker container as follow:
# docker run --rm -it -v ${PWD}:/host ubuntu2004qt653

#!/bin/bash
cd /host
echo "Create build folder and copy Qt dynamic libraries."
mkdir -p tmp/Grootcam/lib && cd tmp/Grootcam/lib

cp /usr/local/Qt-6.5.3/lib/libQt6Core.so.6.5.3 libQt6Core.so.6
cp /usr/local/Qt-6.5.3/lib/libQt6Gui.so.6.5.3 libQt6Gui.so.6
cp /usr/local/Qt-6.5.3/lib/libQt6Network.so.6.5.3 libQt6Network.so.6
cp /usr/local/Qt-6.5.3/lib/libQt6OpenGL.so.6.5.3 libQt6OpenGL.so.6
cp /usr/local/Qt-6.5.3/lib/libQt6Qml.so.6.5.3 libQt6Qml.so.6
cp /usr/local/Qt-6.5.3/lib/libQt6QmlModels.so.6.5.3 libQt6QmlModels.so.6
cp /usr/local/Qt-6.5.3/lib/libQt6QmlWorkerScript.so.6.5.3 libQt6QmlWorkerScript.so.6
cp /usr/local/Qt-6.5.3/lib/libQt6Quick.so.6.5.3 libQt6Quick.so.6
cp /usr/local/Qt-6.5.3/lib/libQt6QuickControls2.so.6.5.3 libQt6QuickControls2.so.6
cp /usr/local/Qt-6.5.3/lib/libQt6QuickControls2Impl.so.6.5.3 libQt6QuickControls2Impl.so.6
cp /usr/local/Qt-6.5.3/lib/libQt6QuickTemplates2.so.6.5.3 libQt6QuickTemplates2.so.6
cp /usr/local/Qt-6.5.3/lib/libQt6XcbQpa.so.6.5.3 libQt6XcbQpa.so.6
chmod -x *
cd ..

mkdir -p plugins/platforms && cd plugins/platforms
cp /usr/local/Qt-6.5.3/plugins/platforms/libqxcb.so .
chmod -x *
cd ../
mkdir xcbglintegrations && cd xcbglintegrations
cp /usr/local/Qt-6.5.3/plugins/xcbglintegrations/libqxcb-glx-integration.so .
chmod -x *

cd ../../
mkdir qml && cd qml
cp -r /usr/local/Qt-6.5.3/qml/QtQml .
rm -r ./QtQml/Models \
    ./QtQml/StateMachine \
    ./QtQml/XmlListModel


cp -r /usr/local/Qt-6.5.3/qml/QtQuick .
rm -r ./QtQuick/Dialogs \
    ./QtQuick/Layouts \
    ./QtQuick/LocalStorage \
    ./QtQuick/NativeStyle \
    ./QtQuick/Particles \
    ./QtQuick/Shapes \
    ./QtQuick/Timeline \
    ./QtQuick/tooling \
    ./QtQuick/Window
cd ../..

echo "Make executable binary in build folder."
/usr/local/Qt-6.5.3/bin/qmake ..
make
chrpath -r ./lib/ ./GrootcamControl
mv GrootcamControl Grootcam
echo "Compressing folder to Grootcam.tar.xz"
XZ_OPT='-9' tar -cJf Grootcam.tar.xz Grootcam

