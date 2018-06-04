#!/bin/bash

echo "Raspberry Pi rebootera après l'installation."
echo "Doit être utilisé en tant que Root"
echo " "
echo "Appuyez sur ENTER pour commencer ou Ctrl+C pour arrêter..."
read

echo " "
echo "Check de la connexion internet..."
echo "=================================="
ping -c3 8.8.8.8 > /dev/null

if [ $? -eq 0 ];then
	echo "Connecté"
else
	echo "Pas de connexion, réessayez !!!"
	exit 0
fi


sudo apt-get update
sudo apt-get install libjpeg8-dev imagemagick libv4l-dev
sudo ln -s /usr/include/linux/videodev2.h /usr/include/linux/videodev.h

#Instalation de Mjpeg streamer http://blog.miguelgrinberg.com/post/how-to-build-and-run-mjpg-streamer-on-the-raspberry-pi
git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental
sudo make
sudo make install


echo "done"
cd /home/pi/drone/software/browser_streaming_robot/mjpg-streamer/mjpg-streamer-experimental
sudo ./mjpg_streamer -i "input_file.so" -o "output_http.so -w ./www"
echo "done"

sudo cp mjpg_streamer /usr/local/bin
sudo cp output_http.so input_file.so /usr/local/lib/
sudo cp -R www /usr/local/www

cd ../../

sudo apt-get install gcc build-essential cmake vlc


git clone https://bitbucket.org/DexterIndustries/raspberry_pi_camera_streamer.git
cd raspberry_pi_camera_streamer
mkdir build
cd build
cmake ../
make
sudo make install
cd ../../

rm -R raspberry_pi_camera_streamer

sudo pip install --no-deps tornado==3.2.2 sockjs-tornado==1.0.0
sudo pip3 install --no-deps tornado==3.2.2 sockjs-tornado==1.0.0


echo " "
echo "Restarting"
echo "3"
sleep 1
echo "2"
sleep 1
echo "1"
sleep 1
shutdown -r now
