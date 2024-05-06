h1MD = "08f68561ef82f475676ca182390748bf"
h2MD = "035b4e1ef1c34c7bfaeda2d947a1fd0d"


h1Sh = "282b40461e92909e11c08cd44faf35292af76a174680b68ae80d3ce4da978f1d"
h2Sh = "e3540ff73c7bc95b828ae1f2848ccb14fd14020b37acd85f0d8600709aa03b29"


i = 0
cnt = 0


for element in range(0, len(h1MD)):
    if h1MD[element]==h2MD[element]:
        cnt = cnt + 1
    i = i + 1
    


#for element in range(0, len(h1Sh)):
  #  if h1Sh[element]==h2Sh[element]:
   #     cnt = cnt + 1
    #i = i + 1
    
print(cnt)


