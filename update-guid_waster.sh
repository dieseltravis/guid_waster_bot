#/bin/sh

INFO='\e[38;05;14m'
NC='\033[0m' # No Color

# Status:
#sudo systemctl status guid_waster && 
ps -eo pid,vsz,rss,comm | grep -i python3 && free -m

echo "Shutting down guid_waster..."
echo -e "${INFO}systemctl stop guid_waster${NC}";
sudo systemctl stop guid_waster
echo "Updating guid_waster..."
echo -e "${INFO}git fetch${NC}";
git fetch
echo -e "${INFO}git pull${NC}";
git pull
echo "Starting up guid_waster..."
echo -e "${INFO}systemctl start guid_waster${NC}";
sudo systemctl start guid_waster

ps -eo pid,vsz,rss,comm | grep -i python3 && free -m
sudo systemctl status guid_waster