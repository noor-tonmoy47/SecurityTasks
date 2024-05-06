Using md5:

openssl dgst -md5 task7.txt
MD5(task7.txt)= 08f68561ef82f475676ca182390748bf
ghex task7.txt
flipped a bit and saved it 
openssl dgst -md5 task7.txt
MD5(task7.txt)= 035b4e1ef1c34c7bfaeda2d947a1fd0d

Bit matched : 3

Using sha256:

openssl dgst -sha256 copy.txt
SHA2-256(copy.txt)= 282b40461e92909e11c08cd44faf35292af76a174680b68ae80d3ce4da978f1d
ghex copy.txt
flipped a bit and saved it 
openssl dgst -sha256 copy.txt
SHA2-256(copy.txt)= e3540ff73c7bc95b828ae1f2848ccb14fd14020b37acd85f0d8600709aa03b29

Bit matched: 1
