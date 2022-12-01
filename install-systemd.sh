#/bin/sh

INFO='\e[38;05;14m'
NC='\033[0m' # No Color

echo "Installing python requirements..."
echo -e "${INFO}pip install -r requirements.txt${NC}";
pip install -r requirements.txt
echo "Installing systemd service..."
echo -e "${INFO}cp ~/guid_waster_bot/guid_waster.service /lib/systemd/system/${NC}";
sudo cp ~/guid_waster_bot/guid_waster.service /lib/systemd/system/
echo -e "${INFO}systemctl enable guid_waster${NC}";
sudo systemctl enable guid_waster
echo -e "${INFO}systemctl daemon-reload${NC}";
sudo systemctl daemon-reload
echo -e "${INFO}systemctl start guid_waster${NC}";
sudo systemctl start guid_waster
echo -e "${INFO}systemctl status guid_waster${NC}";
sudo systemctl status guid_waster
