#union intersection difference program
theset={"true","false","right","left"}
setif={"right","Bcom","Bba","Bvoc","BCA"}
wset= theset.union(setif)
print(wset)

dset= theset & setif
print(dset)

cset= theset.difference(setif)
print(cset)