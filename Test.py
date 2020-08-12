import numpy as np

def foo(x):
    return x ** 2



def func(x):
    return np.power(x, 2)


def power_spectrum_galaxy(alpha, beta, xi, y, l, nu_tilda, nu_tilda_prime):
    """Generate galaxy power spectrum.

    Parameters
    ----------
    A: float
        A parameter
    alpha
    beta
    xi
    nu1
    nu2
    l
    nu_21

    Returns
    -------
    cl_gal: array-like
        galaxy power pecctrum as numpy array with elength equal to `nu`

    """
   # cl_gal = (A * (l / 100) ** (-alpha)) * (((nu1* nu2) / (nu_21**2)) ** (-beta))*np.exp((-1/2*xi**2)*np.log(nu1/nu2)**2)
    
     # cl_gal = (A * (l / 100) ** (-alpha)) * (((nu1* nu2) / (nu_21**2)) ** (-beta))*np.exp((-1/2*xi**2)*np.log(nu1/nu2)**2)  
    
    return cl_gal

