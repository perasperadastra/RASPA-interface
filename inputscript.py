import sys
import pybel
import RASPA2
import matplotlib.pyplot as mtplot
import os 


#####################
def clear():
    os.system('clear')
###################
def index(value):
    index={}
    number=0
    for line in value:
        number=number+1
        if line.startswith('[A]'):
            index.update({line[3:]:number})
    for key in list(index.keys()):
        large=len(key)-1
        ky=key[:large]
        index[ky]=index.pop(key)
    return index

def text(value):
    text={}
    number=0
    for line in value:
        number=number+1
        text.update({line:number})
    return text

####takes input and return value to search    
def inp1(value):
    if value == 'help':
        print(' Theres no help for you here, search a doctor for help')
    try:
        value=int(value)
    except:
        value=-1
    if value > 0 and value < 18:
        con=0
    if value < 0 or value >= 18 and value == 'esc':
        print('            Index Error')
        con=1
    if value==0:
        con=5
    return  con

def inp11():
    control=1
    while control ==1:
        print('')
        val=input('Insert index for starting:  ')
        control=inp1(val)
    return int(val)


def decision(decisio):
    while decisio==2:
        print('Search more(S) |Function Help (H:menunumber:functionnumberinsubmenu) [ex: H:1:2 -> refeers menu 1 function 2] | exit (0)|')
        inputdes=input('    ')
        try:
            inputdes =='S'
        except: 
            try :
                inputdes=='F'
            except:
                try:
                    inputdes.startswith('H')
                except:
                    print('Input error')
                    continue
        if inputdes=='S':
            decisio=1
        if inputdes=='0':
            decisio=4
        if inputdes.startswith('H')==True:
            decisio=3
    return decisio , inputdes

def decision2(decisio):
    while decisio==2:
        print('Search more(S) |  exit help mode(0)|')
        inputdes=input('    ')
        try:
            inputdes =='S'
        except: 
            try :
                inputdes=='0'
            except:
                try:
                    inputdes.startswith('H')
                except:
                    print('Input error')
                    continue
        if inputdes=='S':
            decisio=1
        if inputdes=='0':
            decisio=4
    return decisio , inputdes
def help(inp):
    bor=1
    while bor==1:
        print('')
        print('')
        helping={}
        helping0={}
        printer={}
        try:
            split=inp.split(':')
        except:
            print('help mode error, select new index ')
            inp=input('   ')
            continue
        split=inp.split(':')
        try:
            (int(split[1])>0)==True
        except:
            print('help mode error, select new index ')
            inp=input('   ')
            continue
        try:
            (int(split[2])>0)==True
        except:
            print('help mode error, select new index ')
            inp=input('   ')
            continue
        menu=int(split[1])
        function=int(split[2])
        nu=0
        nm=0
        temp1=0
        temp2=0
        for line in index.keys():
            nu=nu+1
            if nu==int(menu):
                temp1=index[line]
            if nu==int(menu)+1 :
                temp2=index[line]
        nu=0
        for line in text.keys():
            nu=nu+1
            if nu >=temp1 and nu<temp2:
                if line.startswith('•'):
                    nm=nm+1
                    helping.update({line:nm})
                    helping0.update({line:nu})
                    bor=2
        nu=0
        tem2=temp2
        tem1=0
        for vl  in helping0.keys():
            nu=nu+1
            if nu==function:
                tem1=helping0[vl]
                bor=2
            if nu==function+1:
                tem2=int(helping0[vl])
                bor=2
        nu=0
        for line in text.keys():
            nu=nu+1
            if nu>=tem1 and nu< tem2:
                printer.update({line:nu})
        for line in printer.keys():
            print(line,  end= '')
        print('')
        print('')
        if bor==1:
            print('help mode error, select new index ')
            inp=input('   ')
            continue
    ###end of help//-> decision
    return

def helpdecision():
    borp=1
    while borp==1:
        spt=1
        print('New help or escape help mode (esc)')
        inputdes=input('       ')
        try:
            inputdes.startswith('esc')==True
        except:
            try:
                inputdes.starswith('H')
            except:
                print('Input error')
                continue
        if inputdes.startswith('esc')==True:
            spt=0
            borp=2
        if inputdes.startswith('H'):
            borp=2
    return spt ,  inputdes
def buclesegurodoc(value, con=0):
    print('')
    cns=1
    if con==0:
        while cns==1:
            print(value)
            print('rewrite [y / n]')
            inp=input('')
            if inp=='y':
                cns=3
            if inp=='n':
                cns=2
    if con==1:
        while cns==1:
            ins=input('Add a new '+value+'field  [y/n]')
            if ins=='y':
                cns=3
            if ins=='n':
                cns=2
            if ins!='y' and ins!='n':
                continue
    return cns
####################

#############
def submenu(inpt, other=0, ot=0):
    num=0
    num2=0
    loto=[]
    for key in index:
        num=num+1    
        if num==inpt:
            kyl=len(key)-2
            name=key[:kyl]
            if ot==0:
                print('       '+name+' Submenu:')
                print('')
            ref1=int(index[key])
            loto.insert(0, ref1)
        if num==(inpt+1):
            ref2=int(index[key])
            loto.insert(1, ref2)
    if other==1:
        name=name[:(len(name)-3)]
        submenus[name]={}
    for key , value in text.items():
        if int(value) >=loto[0] and int(value)<=loto[1]:
            if key.startswith('•'):
                num2=num2+1
                if ot==0:
                    print(str(num2)+key ,  end='')
                if other==1:
                    submenus[name][key[2:(len(key))-1]]=num2
    return

##########################initial documents needed###############
def docintro():
    print('To run a RASPA simultion you will need the following items:')
    print('')
    print('--> Input file loaded as a string (makeable in this program or loaded')
    print('        inputfile.input')
    print('')
    print('-->A structure file in .cif format (must have the same name in the input file') 
    print('        structure_name.cif')
    print('')
    print ('-->Force field inputs:')
    print('        -->pseudo_atoms.def')
    print('        -->force_field.def//force_field_mixing_rules.def:')
    print('                  force_field.def has preference over force_field_mixing_rules')
    print('                  (you can find examples of this documents in the raspa share directory)')
    print('`')
    print('-->Molecule definition file in .def format(must have the same name in the input file')
    print('')
    print('-->Just for flexible frameworks must be added zframework.def (define all bond,bends torsions...)')
    print('')
    print('The normal workflow is to first go to the /RASPA2/share/raspa/')
    print('')
    print("When a molecule/structure/framework/forcefield name is input in raspa; raspa search this file in this folder and if it's not saved it will return a error, so if you want to use files that are not part of the raspa repository you must add it previously to the folder")
    print('')
    print('But for this lite version you must copy those files into a directoy containing this python program, the texto.txt file and the RASPA file that you will use fo your simulations')
    return

def printerfunc(text):
    b=1
    while b==1:
        des=input('Make a new file or add this information to the common file? [new/old]: ')
        if des=='new':
            cond=0
            b=2
        if des=='old':
            cond=1
            b=2
    if cond==0:
        ###print in a new file
        inp=input('File name [name.format]: ')
        orig_sys = sys.stdout
        with open(inp,'w') as inp:
            sys.stdout = inp
            print(text)
        sys.stdout=orig_sys
    if cond==1:
        ######print in the same shared file
        inp=input('File name [communnamefile.format]: ')
        orig_sys = sys.stdout
        with open(inp,'a') as inp:
            sys.stdout = inp
            print(text)
        sys.stdout=orig_sys

###################################################
def easymode():
    b=1
    while b==1:
        clear()
        print('')
        print('The easy mode contains the following options:')
        print('         A)   Get Geometric Surface Area:')
        print('         B)   Get Helium void fraction:  ')
        print('         C)   Get pore size distribution:')
        print('         D)   Run a mixture of gases:')
        print('         E)   Create a script (input file):')
        print('         E.2) Create and run the script:')
        print('         F)   Run a simulation (limited parameters and assumed sensible defaults):')
        print('         0)   Exit')
        print('')
        print('')
        c=1
        while c==1:
            des=input('Choose an option: ')
            if des=='A':
                clear()
                print('         A)   Get Geometric Surface Area:')
                geomarea= getgeometricsurfacearea()
                d=1
                while d==1:
                    e=input('Save in a output file? [y/n]: ')
                    if e=='y':
                        printerfunc(geomarea)
                        d=2
                        c=2
                    if e=='n':
                        d=2
                        c=2
            if des=='B':
                clear()
                print('         B)   Get Helium void fraction:  ')    
                voidfrac=getheliumvoidfraction()
                d=1
                while d==1:
                    e=input('Save in a output file? [y/n]: ')
                    if e=='y':
                        printerfunc(voidfrac)
                        d=2
                        c=2
                    if e=='n':
                        d=2
                        c=2
                
            if des=='C':
                clear()
                print('         C)   Get pore size distribution:')
                getpore=getporesizedistribution()
                d=1
                while d==1:
                    e=input('Save in a output file? [y/n]: ')
                    if e=='y':
                        printerfunc(getpore)
                        d=2
                        c=2
                    if e=='n':
                        d=2
                        c=2
            if des=='D':
                clear()
                print('         D)   Run a mixture of gases:')        
                mixt=runmixture()
                d=1
                while d==1:
                    e=input('Save in a output file? [y/n]: ')
                    if e=='y':
                        printerfunc(mixt)
                        d=2
                        c=2
                    if e=='n':
                        d=2
                        c=2
            if des=='E':
                clear()
                print('         E)   Create a script (input file):')        
                script=createscript()
                d=1
                while d==1:
                    e=input('Save in a output file? [y/n]: ')
                    if e=='y':
                        printerfunc(script)
                        d=2
                        c=2
                    if e=='n':
                        d=2
                        c=2
            if des=='E.2':
                clear()
                print('         E.2) Create and run the script:')        
                runed, inp=runscript(0)
                d=1
                while d==1:
                    e=input('Save in a output file the simulation results? [y/n]: ')
                    if e=='y':
                        printerfunc(runed)
                        d=2
                    if e=='n':
                        d=2
                d=1
                while d==1:
                    e=input('Save in a output file the input file? [y/n]: ')
                    if e=='y':
                        printerfunc(inp)
                        d=2
                        c=2
                    if e=='n':
                        d=2
                        c=2
                        
            if des=='F':
                clear()
                print('         F)   Run a simulation (limited parameters and assumed sensible defaults):')       
                out=runn()
                d=1
                while d==1:
                    e=input('Save in a output file? [y/n]: ')
                    if e=='y':
                        printerfunc(out)
                        d=2
                        c=2
                    if e=='n':
                        d=2
                        c=2
            if des=='0':
                c=2
                b=2
    return

def fullmode():
    a=1
    while a==1:
        out=runscript(1)
        printerfunc(out)
        b=1
        while b==1:
            des=input('New simulation [y/n]: ')
            if des=='y':
                b=2
            if des=='n':
                a=2
                b=2
                
def helpmode():
    decisio=1
    while decisio>=1 and decisio<=3:
        clear()
        if decisio ==1:
            for line in index.keys():
                print(' '+line)
        inputlo=inp11()
        if inputlo==0:
            break
        clear()
        print('')
        print('')
        submenu(inputlo)
        print('')
        print('')
        decisio=2
        decisio , inputdes =decision(decisio)
        print(' ')
        clear()
        if decisio==3:
            spt=1
            while spt==1:
                help(inputdes)
                spt, inputdes=helpdecision()
                decisio=2
                if spt==0:
                    decisio , inputdes=decision2(decisio)
                
        if decisio==4:
            print('')
            print('              Ending help mode')
            print('')
    return
#####################################################33
def getgeometricsurfacearea():
    print('Define the following parameter:')
    print('            *for default option, you must introduce the exactly default ex:CrystalGenerator')
    print('')
    structurename=input('Input structure name (name.cif): ')
    structur=structurename.split('.')
    strc = next(pybel.readfile(structur[1],structurename))
    strc.unitcell.FillUnitCell(strc.OBMol)
    strc.calccharges("eqeq")
    unitcells=input('unit_cells [default=(1,1,1)]: ')
    unitcells=unitcells.split(',')
    a=unitcells[0]
    a=a[1]
    b=unitcells[1]
    c=unitcells[2]
    c=c[0]
    cycles=int(input('cycles [default=500]: '))
    forcefield=input('forcefield [default=CrystalGenerator]: ')
    srfcarea=RASPA2.get_geometric_surface_area(strc, unit_cells=(a, b, c), cycles=cycles, input_file_type="cif", units="m^2/g",forcefield=forcefield )
    print('The geometric surface area='+str(srfcarea)+'m^2/g')
    return srfcarea


def getheliumvoidfraction():
    print('Define the following parameter:')
    print('            *for default option, you must introduce the exactly default ex:CrystalGenerator')
    print('')
    structurename=input('Input structure name (name.cif): ')
    structur=structurename.split('.')
    strc = next(pybel.readfile(structur[1],structurename))
    strc.unitcell.FillUnitCell(strc.OBMol)
    strc.calccharges("eqeq")
    unitcells=input('unit_cells [default=(1,1,1)]: ')
    unitcells=unitcells.split(',')
    a=unitcells[0]
    a=a[1]
    b=unitcells[1]
    c=unitcells[2]
    c=c[0]
    cycles=int(input('cycles [default=2000]: '))
    forcefield=input('forcefield [default=CrystalGenerator]: ')
    voidfrac=RASPA2.get_helium_void_fraction(strc, unit_cells=(a, b, c), cycles=cycles, input_file_type="cif",forcefield=forcefield )
    print('The helium void fraction is '+str(voidfrac))
    return voidfrac

def getporesizedistribution():
    print('Returns a list of the form [[x1, x2, ..., xn], [y1, y2, ..., yn]], where x is the binned pore size (in Angstroms) and y is the partial pore volume (in cm^3 / g).')
    print('Define the following parameter:')
    print('            *for default option, you must introduce the exactly default ex:CrystalGenerator')
    print('')
    structurename=input('Input structure name (name.cif): ')
    structur=structurename.split('.')
    strc = next(pybel.readfile(structur[1],structurename))
    strc.unitcell.FillUnitCell(strc.OBMol)
    strc.calccharges("eqeq")
    unitcells=input('unit_cells [default=(1,1,1)]: ')
    unitcells=unitcells.split(',')
    a=unitcells[0]
    a=a[1]
    b=unitcells[1]
    c=unitcells[2]
    c=c[0]
    cycles=int(input('cycles [default=500]: '))
    forcefield=input('forcefield [default=CrystalGenerator]: ')
    bins=int(input('bin number of the histogram output [default=50]: '))
    porsedistrib=RASPA2.get_pore_size_distribution(strc, unit_cells=(a, b, c), cycles=cycles, input_file_type="cif",forcefield=forcefield, bins= bins)    
    x=porsedistrib[0]
    y=porsedistrib[1]
    mtplot.plot(x, y)
    mtplot.xlabel('Binned pore size (Angstrom)')
    mtplot.ylabel('Partial pore volume (cm^3 / g)')
    mtplot.show()

    return porsedistrib

def runmixture():
    structurename=input('Input structure name (name.cif): ')
    structur=structurename.split('.')
    strc = next(pybel.readfile(structur[1],structurename))
    strc.unitcell.FillUnitCell(strc.OBMol)
    strc.calccharges("eqeq")
    unitcells=input('unit_cells [default=(1,1,1)]: ')
    unitcells=unitcells.split(',')
    a=unitcells[0]
    a=a[1]
    b=unitcells[1]
    c=unitcells[2]
    c=c[0]
    cycles=int(input('cycles [default=500]: '))
    forcefield=input('forcefield [default=CrystalGenerator]: ')
    simulationtype=input('Simulation type [default=MonteCarlo]: ')
    print('Now you will be asked for the number ofdifferent molecules, their names and the mol fraction of each one [number of molecules and names introduce must match ]')
    nummolecules=int(input('Number of molecules to test: '))
    molecules=[]
    molfractions=[]
    control=1
    temperature=int(float(input('Temperature (K) [default=273.15]: ')))
    pressure=int(float(input('Pressure (Pa) [default=101325]: ')))
    while control==1:
        print('Want to calculate the helium void fraction or add it manully?')
        des=input('[calculate/ manual [default=1.0]:')
        if des!='calculate' and des!='manual':
            continue
        if des=='calculate':
            void=int(float(getheliumvoidfraction()))
        if des=='manual':
            void=int(float(input('Value= ')))
    for i in range(nummolecules):
        mol=input('Molecule name [name]:')
        molfr=int(float(input('Mol fraction: ')))
        molecules.append(mol)
        molfractions.append(molfr)
    
    out=RASPA2.run_mixture(strc, molecules=molecules , mol_fractions=molfractions, temperature=temperature, pressure=pressure, helium_void_fraction=void, unit_cells=(a, b, c), simulation_type=simulationtype,cycles=cycles, init_cycles="auto", forcefield=forcefield,input_file_type="cif")
    return out


def runn():
    structurename=input('Input structure name (name.cif): ')
    structur=structurename.split('.')
    strc = next(pybel.readfile(structur[1],structurename))
    strc.unitcell.FillUnitCell(strc.OBMol)
    strc.calccharges("eqeq")
    unitcells=input('unit_cells [default=(1,1,1)]: ')
    unitcells=unitcells.split(',')
    a=unitcells[0]
    a=a[1]
    b=unitcells[1]
    c=unitcells[2]
    c=c[0]
    temperature=int(float(input('Temperature (K) [default=273.15]: ')))
    presure=int(float(input('Pressure (Pa) [default=101325]: ')))
    cycles=int(input('cycles [default=2000]: '))
    forcefield=input('forcefield [default=CrystalGenerator]: ')
    simulationtype=input('Simulation type [default=MonteCarlo]: ')
    molecule=input('Molecule name [name]: ')
    frameworkname=input('Framework name [default=streamed]')
    control=1
    while control==1:
        print('Want to calculate the helium void fraction or add it manully?')
        des=input('[calculate/ manual :')
        if des!='calculate' and des!='manual':
            continue
        if des=='calculate':
            void=int(float(getheliumvoidfraction()))
            control=2
        if des=='manual':
            void=int(float(input('Value [default=1.0]= ')))
            control=2
    out=RASPA2.run(strc, molecule, temperature=temperature, pressure=presure, helium_void_fraction=void, unit_cells=(a, b, c), framework_name=frameworkname, simulation_type=simulationtype, cycles=cycles, init_cycles="auto", forcefield=forcefield,input_file_type="cif")
    return out

def createscript():
    molecule=input('Molecule name [name]: ')
    unitcells=input('unit_cells [default=(1,1,1)]: ')
    unitcells=unitcells.split(',')
    a=unitcells[0]
    a=a[1]
    b=unitcells[1]
    c=unitcells[2]
    c=c[0]
    temperature=int(float(input('Temperature (K) [default=273.15]: ')))
    presure=int(float(input('Pressure (Pa) [default=101325]: ')))
    cycles=int(input('cycles [default=2000]: '))
    forcefield=input('forcefield [default=CrystalGenerator]: ')
    simulationtype=input('Simulation type [default=MonteCarlo]: ')
    control=1
    while control==1:
        print('Want to calculate the helium void fraction or add it manully?')
        des=input('[calculate/ manual :')
        if des!='calculate' and des!='manual':
            continue
        if des=='calculate':
            void=int(float(getheliumvoidfraction()))
            control=2
        if des=='manual':
            void=int(float(input('Value [default=1.0]= ')))
            control=2
    out=RASPA2.create_script(molecule, temperature=temperature, pressure=presure, helium_void_fraction=void, unit_cells=(a, b, c), simulation_type=simulationtype, cycles=cycles, init_cycles="auto", forcefield=forcefield,input_file_type="cif")
    return out
    
def runscript(value=1):
    if value==0:
        inp=createscript()
    if value==1:
        inpufile=input('Input file name [inputnam.format]:')
        with open(inpufile, 'r') as myfile:
            inp=myfile.read()
    if value==0:
        structu=input('Structure [name.format]: ')
        out=RASPA2.run_script(inp, structu)
    if value==1:
        while value==1:
            des=input('Structure (Optional) [name.cif/None]: ')
            if des=='None':
                value=2
                out=RASPA2.run_script(inp)
            if des!=0:
                value=2
                out=RASPA2.run_script(inp, des)
    return out ,inp



 #############################
clear()
work=open('texto.txt','r')
work1=open('texto.txt','r')

#input=open('input.txt,'+')
print('           Hello this is a RASPA2 input-file creator'+'\n'+'           Take it easy :D',end='\n')
nada=input('')
print('')
print('') 
    
    
#####dictionary creator####
index=index(work)
text=text(work1)
submenus={}
####initial input#######

    #hasta aqui esta terminado y funcional en todos los aspectos   

###### incluir archivos
docintro()
print('')
print('')
print('')
print('')
nada=input()
intxt=open('input.txt', 'w+')
print('Choose between a easy mode (loading specified files and assuming sensible defaults)')
print('A full unlimited RASPA simulation (The user must buil its own input file)')
print('Or a Help mode')
count=0
print('')
print('')
while count==0:
    des1=input('Easy mode [e] / full raspa mode [r] / help mode [h] / exit [0] :   ')
    print('')
    clear()
    if des1!='e' and des1!='r' and des1 !='h' and des1!='0':
        continue
    if des1=='e':
        easymode()
        clear()
    if des1=='r':
        fullmode()
        clear()
    if des1=='h':
        helpmode()
        clear()
    if des1=='0':
        count=1










