# Make docker image first
# cd /path/to/grootcam/grootcamcontrol/Builds/Linux
# docker build . -t ubuntu2004qt653

docker run --rm -v ${PWD}:/host ubuntu2004qt653 bash /host/Builds/Linux/build.sh
mv ./tmp/Grootcam.tar.xz .
rm -rf ./tmp
