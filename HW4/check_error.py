from option_models.sabr import *

if __name__ == '__main__':
    strike = np.linspace(75, 125, num=25)
    forward = 100
    bsm_mc = ModelBsmCondMC(1, 0.2, 0.3, 0.25, 1, n_samples=1000)
    price_mc = bsm_mc.price(strike, forward)
    print (price_mc)
    np.std()