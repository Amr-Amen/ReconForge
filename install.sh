#!/bin/bash

echo "========== ReconForge Installer =========="

PROJECT_PATH=$(pwd)

echo
echo "[+] Project detected at:"
echo "$PROJECT_PATH"

sed "s|__PROJECT_PATH__|$PROJECT_PATH|g" reconforge > reconforge.tmp

mv reconforge.tmp reconforge

chmod +x reconforge

sudo cp reconforge /usr/local/bin/

echo
echo "[+] Installation completed successfully!"
echo
echo "You can now run:"
echo
echo "    reconforge"
echo
