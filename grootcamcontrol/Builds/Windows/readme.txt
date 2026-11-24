From QtCreator, make a release build.
Copy GrootcamControl.exe to the build folder.

sudo apt install
    wget \
    build-essential \
    cmake \
    python3 \
sudo apt install mingw-w64
sudo apt install build-essential libgl1-mesa-dev python
rm -rf qtgrpc qtquickeffectmaker qthttpserver qtimageformats qtquicktimeline qtsvg qtquick3d qtquick3dphysics qt3d qtscxml qtnetworkauth qt5compat qt3d qtactiveqt qtcharts qtcoap qtconnectivity qtdatavis3d qtlanguageserver qtlocation qtmqtt qtlottie qtmultimedia qtopcua qtpositioning qtremoteobjects qtsensors qtserialbus qtserialport qtvirtualkeyboard qtwayland qttools qtwebengine qtdoc qtspeech qttranslations qtwebview qtwebchannel qtwebsockets

./configure -xplatform win32-g++ -device-option CROSS_COMPILE=/usr/bin/x86_64-w64-mingw32- -opensource -nomake tests -nomake examples -no-icu -confirm-license -no-dbus -sql-sqlite
cmake --build . --parallel
make install
