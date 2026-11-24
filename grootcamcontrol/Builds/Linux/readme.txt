How to build:
=============

Linux:
------

$ cd /path/to/grootcam/grootcamcontrol/Builds/Linux
$ docker build . -t ubuntu2004qt653

$ cd /path/to/grootcam/grootcamcontrol
docker run --rm -v ${PWD}:/host ubuntu2204qt653 bash /host/Builds/Linux/build.sh

The resulting archive is here:
/path/to/grootcam/grootcamcontrol/build/Grootcam.tar.xz

|-- GrootcamControl
|-- lib
|   |-- libQt6Core.so.6
|   |-- libQt6Gui.so.6
|   |-- libQt6Network.so.6
|   |-- libQt6OpenGL.so.6
|   |-- libQt6Qml.so.6
|   |-- libQt6QmlModels.so.6
|   |-- libQt6QmlWorkerScript.so.6
|   |-- libQt6Quick.so.6
|   |-- libQt6QuickControls2.so.6
|   |-- libQt6QuickControls2Impl.so.6
|   |-- libQt6QuickTemplates2.so.6
|   `-- libQt6XcbQpa.so.6
|-- plugins
|   |-- platforms
|   |   `-- libqxcb.so
|   `-- xcbglintegrations
|       `-- libqxcb-glx-integration.so
`-- qml
    |-- QtQml
    |   |-- WorkerScript
    |   |-- libqmlplugin.so
    |   |-- plugins.qmltypes
    |   `-- qmldir
    `-- QtQuick
        |-- Controls
        |   |-- Basic
        |   |-- Fusion
        |   |-- Material
        |   |-- impl
        |   |-- libqtquickcontrols2plugin.so
        |   |-- plugins.qmltypes
        |   `-- qmldir
        |-- Templates
        |   |-- libqtquicktemplates2plugin.so
        |   |-- plugins.qmltypes
        |   `-- qmldir
        |-- libqtquick2plugin.so
        |-- plugins.qmltypes
        `-- qmldir
