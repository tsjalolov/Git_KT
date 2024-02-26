mass = [1,2,6,4,7,4,2,8]
mass2 = []
i = 0
mass_len = len(mass)-1
while  mass_len + 1 > 0:
    print(mass[mass_len])
    print(mass)
    
    kichik = mass[mass_len]
    
    for j in mass:
        if mass[0] < j:
            kichik = j
    mass2.append(kichik)
    del mass[mass_len]
    mass_len = mass_len - 1
print(mass2)
        
    
