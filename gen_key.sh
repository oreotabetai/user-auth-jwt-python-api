#!/bin/sh

echo "Generating Key to ./key\n"

echo "[1/3] Make Directory"
if [ ! -d ./key ]; then
  mkdir ./key
  echo "mkdir ./key\n"
else
  echo "Already exist\n"
fi

echo "[2/3] Generate Private Key"
if [ ! -f ./key/private-key.pem ]; then
  echo "openssl genrsa 2024 > ./key/private-key.pem"
  openssl genrsa 2024 > ./key/private-key.pem
  echo "\n"
else
  echo "Already exist\n"
fi

echo "[3/3] Generate Public Key"
if [ ! -f ./key/public-key.pem ]; then
  echo "openssl rsa -pubout < ./key/private-key.pem > ./key/public-key.pem"
  openssl rsa -pubout < ./key/private-key.pem > ./key/public-key.pem
  echo "\n"
else
  echo "Already exist\n"
fi

echo "Done."
