#!/bin/bash

echo "Installing All Required Packages"

apt update -y
apt install curl -y
apt install wget -y

echo "All Packages Installed Successfully..."