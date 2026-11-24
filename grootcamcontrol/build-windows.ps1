# Script to be run with powershell
# Specific path to the project
$envpath = "G:\Qt563\6.5.3\mingw_64\bin;G:\Qt563\Tools\mingw1120_64\bin;"
$qtpath = "G:\Qt563\6.5.3\mingw_64"
$archive = "grootcamcontrol"
$exe = "GrootcamControl.exe"

# Building and packaging
$env:Path = $envpath + $env:Path
mkdir tmp
cd tmp
qmake ..
mingw32-make -j8
mkdir $archive
cp ./release/$exe ./$archive
cp $qtpath/bin/libgcc_s_seh-1.dll ./$archive
cp $qtpath/bin/libstdc++-6.dll ./$archive
cp $qtpath/bin/libwinpthread-1.dll ./$archive
cp $qtpath/bin/Qt6Core.dll ./$archive
cp $qtpath/bin/Qt6Gui.dll ./$archive
cp $qtpath/bin/Qt6Network.dll ./$archive
cp $qtpath/bin/Qt6OpenGL.dll ./$archive
cp $qtpath/bin/Qt6Qml.dll ./$archive
cp $qtpath/bin/Qt6QmlCore.dll ./$archive
cp $qtpath/bin/Qt6QmlModels.dll ./$archive
cp $qtpath/bin/Qt6QmlWorkerScript.dll ./$archive
cp $qtpath/bin/Qt6Quick.dll ./$archive
cp $qtpath/bin/Qt6QuickControls2.dll ./$archive
cp $qtpath/bin/Qt6QuickControls2Impl.dll ./$archive
cp $qtpath/bin/Qt6QuickTemplates2.dll ./$archive
mkdir ./$archive/plugins/platforms
cp $qtpath/plugins/platforms/qwindows.dll ./$archive/plugins/platforms
mkdir ./$archive/qml
cp $qtpath/qml/builtins.qmltypes ./$archive/qml
cp $qtpath/qml/jsroot.qmltypes ./$archive/qml
cp -R $qtpath/qml/QtQml ./$archive/qml
cp -R $qtpath/qml/QtQuick ./$archive/qml
New-Item ./$archive/qt.conf
Compress-Archive -Path ./grootcamcontrol -DestinationPath ./grootcamcontrol.zip
cd ..
mv ./tmp/grootcamcontrol.zip .
Remove-Item ./tmp -Force -Recurse
