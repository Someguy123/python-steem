from piston.steem import Steem as PistonSteem
import warnings
warnings.simplefilter('always', DeprecationWarning)


class Steem(PistonSteem):
    def __init__(self, *args, **kwargs):
        warnings.warn(
            "Please use the API compatible 'piston-lib' in future",
            DeprecationWarning
        )
        super(Steem, self).__init__(*args, **kwargs)
