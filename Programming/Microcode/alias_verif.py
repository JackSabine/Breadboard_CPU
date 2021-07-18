from aliases import *

ALIASES = [AAC,ACO,ACU,AIB,ARI,ARO,ASI,ASO,ASX,AUA,AUN,CCU,GAO,GBO,HT,IHI,ILI,MAHI,MALI,MI,MO,MRH,NI,PHI,PHO,PI,PLI,PLO,RAS,RBS,RI,RO,RS0,SD,SHI,SHO,SI,SLI,SLO]

REDUCED_LIST = list(set(ALIASES))

if(len(ALIASES) != len(REDUCED_LIST)):
    print("FAIL")
else:
    print("SUCCESS")

for a in ALIASES:
    print(f"{str(bin(a)):>64}")