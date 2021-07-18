# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 00:49:11 2020

@author: aserafeim
"""
import inputdata as id
import math

def dislo2(dt,T,eps_dot,rho_cm,rho_wi,rho_ci):
    
    
    def sens(r,s,T):
        f=1 + r * math.pow(T-1,s)
        
        return f

    
   
    #def c_fun(r,s,T,r_m,s_m,c_0,m_0,eps_dot):
    #    m=sens(r_m,s_m)/m_0
    #    c=sens(r,s,T)*eps_dot**m/c_0
        
    def c_fun(r,s,T,c_0,eps_dot):
        #m=sens(r_m,s_m)/m_0
        c=sens(r,s,T)*c_0
    
    
        
        return c
    rho_cm=rho_cm/id.rho_0
    rho_wi=rho_wi/id.rho_0
    rho_ci=rho_ci/id.rho_0
    
    M=id.M
    c_cm_gn=id.c_cm_gn
    c_ci_ac=id.c_ci_ac
    c_wi_ac=id.c_wi_ac
    G=c_fun(id.r_G,id.s_G,T,id.G_0,eps_dot)
    m_v=c_fun(id.r_v_m,id.s_v_m,T,id.m_v_0,eps_dot)*eps_dot/id.eps_dot_0
    sigma_v=c_fun(id.r_v,id.s_v,T,1,eps_dot)*id.sigma_v_00*eps_dot**m_v
    #m_cm_gn=sens(r_cm_gn_m,s_cm_gn_m)/m_cm_gn_0
    #c_cm_gn=sens(r_cm_gn,s_cm_gn,T)*eps_dot**m_cm_gn/c_cm_gn_0
    #c_cm_an=c_fun(r_cm_an,s_cm_an,T,r_cm_an_m,s_cm_an_m,c_cm_an_0,m_cm_an_0,eps_dot)
    #c_ci_an=c_fun(r_ci_an,s_ci_an,T,r_ci_an_m,s_ci_an_m,c_ci_an_0,m_ci_an_0,eps_dot)
    #c_wi_an=c_fun(r_wi_an,s_wi_an,T,r_wi_an_m,s_wi_an_m,c_wi_an_0,m_wi_an_0,eps_dot)
    #c_cm_tr=c_fun(r_cm_tr,s_cm_tr,T,r_cm_tr_m,s_cm_tr_m,c_cm_tr_0,m_cm_tr_0,eps_dot)
    #c_wi_nc=c_fun(r_wi_nc,s_wi_nc,T,r_wi_nc_m,s_wi_nc_m,c_wi_nc_0,m_wi_nc_0,eps_dot)
    #c_ci_rm=c_fun(r_ci_rm,s_ci_rm,T,r_ci_rm_m,s_ci_rm_m,c_ci_rm_0,m_ci_rm_0,eps_dot)
    #c_wi_rm=c_fun(r_wi_rm,s_wi_rm,T,r_wi_rm_m,s_wi_rm_m,c_wi_rm_0,m_wi_rm_0,eps_dot)
    
    c_cm_an=c_fun(id.r_cm_an,id.s_cm_an,T,id.c_cm_an_0,eps_dot)
    c_ci_an=c_fun(id.r_ci_an,id.s_ci_an,T,id.c_ci_an_0,eps_dot)
    c_wi_an=c_fun(id.r_wi_an,id.s_wi_an,T,id.c_wi_an_0,eps_dot)
    c_cm_tr=c_fun(id.r_cm_tr,id.s_cm_tr,T,id.c_cm_tr_0,eps_dot)
    c_wi_nc=c_fun(id.r_wi_nc,id.s_wi_nc,T,id.c_wi_nc_0,eps_dot)
    c_ci_rm=c_fun(id.r_ci_rm,id.s_ci_rm,T,id.c_ci_rm_0,eps_dot)
    c_wi_rm=c_fun(id.r_wi_rm,id.s_wi_rm,T,id.c_wi_rm_0,eps_dot)
    
    
    #Individual mechanism as rates.

    drho_cm_gn=M * c_cm_gn*(rho_cm/math.sqrt(rho_ci + rho_wi))*eps_dot
    drho_cm_an=M * c_cm_an*rho_cm*rho_cm*eps_dot#
    drho_ci_an=M * c_ci_an*rho_cm*rho_ci*eps_dot#
    drho_wi_an=M * c_wi_an*rho_cm*rho_wi*eps_dot#
    drho_ci_ac=M * c_ci_ac*math.sqrt(rho_ci)*rho_cm*eps_dot
    drho_wi_ac=M * c_wi_ac*math.sqrt(rho_wi)*rho_cm*eps_dot
    drho_cm_tr=M * c_cm_tr*math.pow(rho_cm,1.5)*eps_dot#
    drho_wi_nc=M * c_wi_nc*math.pow(rho_ci,1.5)*rho_cm*eps_dot#
    drho_ci_rm=M * c_ci_rm*rho_ci*eps_dot#
    drho_wi_rm=M * c_wi_rm*rho_wi*eps_dot#
    
    #Evolution equations rates
    drho_wi=drho_wi_nc + drho_wi_ac- (drho_wi_an+ drho_wi_rm)
    drho_ci=drho_cm_tr + drho_ci_ac- (drho_ci_an+ drho_ci_rm+ drho_wi_nc)
    drho_cm=drho_cm_gn + drho_ci_rm+ drho_wi_rm- (2*drho_cm_an+ drho_ci_an+ drho_wi_an+ drho_ci_ac+ drho_wi_ac+ drho_cm_tr)
    
    
    #Evolution equatuion forward integration
    
    rho_wi_curr = (rho_wi + drho_wi*dt)*id.rho_0 
    rho_ci_curr = (rho_ci + drho_ci*dt)*id.rho_0 
    rho_cm_curr = (rho_cm + drho_cm*dt)*id.rho_0 
    
    # print(drho_ci)
    sigma_ci=M*id.b*G*id.a_c_0*math.sqrt(rho_ci_curr)
    sigma_wi=M*id.b*G*id.a_w_0*math.sqrt(rho_wi_curr)
    sigma=sigma_v+sigma_ci+sigma_wi
    
    
    
    return [rho_cm_curr,rho_wi_curr, rho_ci_curr, drho_wi ,drho_ci ,drho_cm, sigma]
    