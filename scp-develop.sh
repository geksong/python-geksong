#!/bin/sh

### scp file to remote server

cppath="/home/geksong/文档/wac/developpackage/"
remotepath="/home/appweb/update/"
#testwacserver="appweb@115.236.16.3:"
testwacserver="appweb@192.168.1.248:"

echo "输入要从$cppath push到$testwacserver$remotepath的文件名"
read cpfile
filename=${cpfile#*/}

echo "Begin push From $cppath$cpfile To $testwacserver$remotepath$filename"
scp $cppath$cpfile $testwacserver$remotepath$filename
echo "Success done"

