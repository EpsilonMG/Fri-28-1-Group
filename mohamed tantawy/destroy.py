import os,random
def destroy_half_universe():
    folder=input('Enter folder name: ')
    l=os.listdir(folder)
    for i in range(len(l)//2):
        file=random.choice(l)
        os.remove(folder+'/'+file)
        l.remove(file)
        
        
destroy_half_universe()