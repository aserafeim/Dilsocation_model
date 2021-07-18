# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 23:33:54 2020

@author: aserafeim
"""
import inputdata as id
import dislo_amir as dis
import xlsxwriter
import matplotlib.pyplot as plt
plt.close('all')
# t=0
# eps=0
# rho_cm=id.rho_cm_0*id.rho_0
# rho_wi=id.rho_wi_0*id.rho_0
# rho_ci=id.rho_ci_0*id.rho_0

# strain_l=[0]
# cm_l=[rho_cm]
# wi_l=[rho_wi]
# ci_l=[rho_ci]
# sigma_l=[0]
# time_l=[0]
drho_ci=[0]
drho_cm=[0]
drho_wi=[0]
for k in range(1):
    T_c=400
    print(T_c)
    t=0
    eps=0.004
    strain_l=[0.004]
    rho_cm=id.rho_cm_0*id.rho_0
    rho_wi=id.rho_wi_0*id.rho_0
    rho_ci=id.rho_ci_0*id.rho_0
    cm_l=[rho_cm]
    wi_l=[rho_wi]
    ci_l=[rho_ci]
    sigma_l=[0]
    time_l=[0]
    workbook = xlsxwriter.Workbook(str(T_c) + '.xlsx')
    worksheet = workbook.add_worksheet('Sheet')
    for i in range(4000):
        dt=0.01
        eps_dot=0.01
        t+=dt
        eps+=eps_dot*dt
        T=(T_c+273.15)/id.T0
        temp_list=dis.dislo2(dt,T,eps_dot,rho_cm,rho_wi,rho_ci)
        time_l.append(t)
        strain_l.append(eps)
        cm_l.append(temp_list[0])
        wi_l.append(temp_list[1])
        ci_l.append(temp_list[2])
        drho_wi.append(temp_list[3])
        drho_ci.append(temp_list[4])
        drho_cm.append(temp_list[5])
        sigma_l.append(temp_list[-1])
        rho_cm=cm_l[-1]
        rho_wi=wi_l[-1]
        rho_ci=ci_l[-1]
        # print (eps)
    print(T)
    row=0

plt.figure()
plt.plot(strain_l,sigma_l)
plt.figure()
plt.plot(strain_l,wi_l)
plt.title('Wall immobile')
plt.figure()
plt.plot(strain_l,ci_l)
plt.title('Cell immobile')
plt.figure()
plt.plot(strain_l,cm_l)
plt.title('Mobile')
plt.figure()
plt.plot(strain_l,drho_cm)
plt.title('Mobile rate')
plt.figure()
plt.plot(strain_l,drho_ci)
plt.title('Cell immbile rate')
plt.figure()
plt.plot(strain_l,drho_wi)
plt.title('wall immobile rate')
# ax.plot(Lf_real50[4],label='50 pct threshold')
# ax.legend()
    # worksheet.write_string(row,0, 'Strain')
    # worksheet.write_string(row,1, 'Stress')
    # worksheet.write_string(row,2, 'Cell mobiles')
    # worksheet.write_string(row,3, 'Cell Immobiles')
    # worksheet.write_string(row,4, 'Wall immobiles')
    # row=1
    # worksheet.write_string(row,0, '-')
    # worksheet.write_string(row,1, 'MPa')
    # worksheet.write_string(row,2, 'm-2')
    # worksheet.write_string(row,3, 'm-2')
    # worksheet.write_string(row,4, 'm-2')
    # row=2
    # for i in range(len(strain_l)):
    #     worksheet.write(row,0,strain_l[i])
    #     worksheet.write(row,1,sigma_l[i])
    #     worksheet.write(row,2,cm_l[i])
    #     worksheet.write(row,3,ci_l[i])
    #     worksheet.write(row,4,wi_l[i])
    #     row+=1
    # workbook.close()