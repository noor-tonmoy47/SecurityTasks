Encryption commands: (4 modes used are cbc, cfb, ecb, ofb)

openssl enc -aes-128-cbc -e -in task1.txt -out aes128cbc.bin -K 0001112223334445556677aabbccee23 -iv 45703759217584930247685944385563

openssl enc -aes-128-cfb -e -in task1.txt -out aes128cfb.bin -K 0001112223334445556677aabbccee23 -iv 45703759217584930247685944385563

openssl enc -aes-128-ecb -e -in task1.txt -out aes128ecb.bin -K 0001112223334445556677aabbccee23

openssl enc -aes-128-ofb -e -in task3.txt -out aes128ofb.bin -K 0001112223334445556677aabbccee23 -iv 45703759217584930247685944385563



Decryption commands:

openssl enc -aes-128-cbc -d -in aes128cbc.bin -out aes128cbcdecrypted.txt -K 0001112223334445556677aabbccee23 -iv 45703759217584930247685944385563

openssl enc -aes-128-cfb -d -in aes128cfb.bin -out aes128cfbdecrypted.txt -K 0001112223334445556677aabbccee23 -iv 45703759217584930247685944385563

openssl enc -aes-128-ecb -d -in aes128ecb.bin -out aes128ecbdecrypted.txt -K 0001112223334445556677aabbccee23

openssl enc -aes-128-ofb -d -in aes128ofb.bin -out aes128ofbdecrypted.txt -K 0001112223334445556677aabbccee23 -iv 45703759217584930247685944385563





here the most information was retrieved using the ofb mode

what are the implication of these differences?
