SCRIPTS_DIR=$(dirname "$0")
PROJECT_DIR=$SCRIPTS_DIR/../
ASSETS_DIR=$PROJECT_DIR/assets/

pyinstaller \
	--noconfirm \
	--log-level=WARN \
	--onefile \
	--windowed \
	--add-data "$ASSETS_DIR/icon.png:." \
	--icon "$ASSETS_DIR/icon.ico" \
	$PROJECT_DIR/updatepls/main.py
