'''
Tara Zakizaeh , Tabriz University, Physics Student
3rd new horizions School in physics - Isfahan university of technology - Sep 12,2025
project name= quantum mechine learning
Task 1: Plot all features for gluon jets
Task 2: Plot transverse momentum(pt) for jets
'''

import numpy as np
import h5py
import matplotlib.pyplot as plt
import requests
import numpy as np
import h5py
import matplotlib.pyplot as plt
git_url ='https://github.com/pierinim/tutorials/tree/master/Data/JetDataset'

def req_uest(my_web_page_link):
    my_request= requests.get(my_web_page_link)

    if my_request.status_code==200:
        print('I found that')
    else: print("not found! 404 error")

req_uest(git_url)
'''files were dowmloaded and storage on my PC, thus we will use that throughout a path in my device'''

input_file = r'T:\Python_project_iut\h5\jetImage_7_100p_0_10000.h5'
f = h5py.File(input_file)

jet_data = np.array(f.get('jets'))                    
target = jet_data[:, -6:-1]                          
data = jet_data[:, :-6]                               
featurenames = [name.decode("utf-8") for name in f["jetFeatureNames"][:]]
#featurenames_prime=list(featurenames)            

gluon_data=data[np.argmax(target,axis=1) == 0]     

while True:
    print('''
menue:
          1.ploting all features for Gloune(Task 1)
          2.ploting j-pt for all (Task 2)

''')
    
    user_answere = int(input("your answere is : "))
    if user_answere==1:
        def plt_t():
            plt.figure()
            plt.hist(gluon_data[:, i], bins=50, density=True, histtype="step", color="blue", label=featurenames[i])
            plt.yscale('log')
            plt.xlabel(featurenames[i], fontsize=12)
            plt.title(f'Feature {i} - Gluon Jets', fontsize=14)
            plt.legend('upper high')
            plt.tight_layout()
            plt.savefig(f'gluon_feature_{i}.png')
            plt.close()

        for i in range(gluon_data.shape[1]):
            plt_t()

        print("the proces was don!")
    elif user_answere==2:
        all_jet_data=jet_data[:1]
        label_jet_names=['j_g',"j_q","j_w","j_z","j_t"]
        colors=["blue","red","yellow","orange","green"]
        pt_index=featurenames.index("j_pt")
        
        plt.figure(figsize=(10,6))

        for j in range(len(label_jet_names)):
            selector=np.argmax(target, axis=1)==j
            pt_value=data[selector,pt_index]
            plt.hist(pt_value, bins=50, histtype="step", linewidth=2,
            color=colors[j], label=label_jet_names[j])
            plt.title(f"j_pt for{label_jet_names[j]} vs jet types")
            plt.legend("upper higher")
            plt.xlabel("j_pt",fontsize=14)
            plt.ylabel("density", fontsize=14)
            plt.grid(True)
            plt.tight_layout()
            plt.savefig("j_pt_all_jets.png")
            plt.savefig(f'pt_for_{label_jet_names[j]}_jet.png')
        print("j_pt ploted foe all jets")
    print('do you want to continue?(y/n)')
    second_user_answere= input(' ')
    if second_user_answere=='n':
        print('bye my friend ;)')
        break