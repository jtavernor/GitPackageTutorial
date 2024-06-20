from .config import get_config
conf = get_config()
if conf['method_to_use'] == 'numpy':
    from .numpy_fns import my_func
elif conf['method_to_use'] == 'torch':
    from .pytorch_fns import my_func
else:
    raise ValueError('Invalid config file')