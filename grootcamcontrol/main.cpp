#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include "viewcontroller.h"
#include <QQmlContext>
#include "bridge.h"


int main(int argc, char *argv[])
{
    QGuiApplication app(argc, argv);

    Bridge bridge;
    ViewController viewController(&bridge);

    QObject::connect(&bridge, &Bridge::log, &viewController, &ViewController::log);
    QObject::connect(&bridge, &Bridge::angle, &viewController, &ViewController::angleInit);
    QObject::connect(&bridge, &Bridge::onlineUpdate, &viewController, &ViewController::onlineChanged);

    QQmlApplicationEngine engine;
    engine.rootContext()->setContextProperty("viewcontroller", &viewController);

    engine.load(QStringLiteral(":/main.qml"));
    if (engine.rootObjects().isEmpty())
        return -1;

    return app.exec();
}
