import pandas as pd

def Ro(omega,h,u):
    return (2*omega*h/u)

def Re(nu,h,u):
    return (u*h/nu)

def Ek(nu,omega,h):
    return (nu/(omega*h**2))

def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')
