SCRIPTS_DIR=$(dirname "$0")

cd $SCRIPTS_DIR/../assets
convert icon.png -resize 256x256 -transparent white source-256.png
convert source-256.png -resize 16x16 source-16.png
convert source-256.png -resize 32x32 source-32.png
convert source-256.png -resize 64x64 source-64.png
convert source-256.png -resize 128x128 source-128.png
convert source-16.png source-32.png source-64.png source-128.png source-256.png -colors 256 icon.ico
rm source-16.png source-32.png source-64.png source-128.png source-256.png
