import importlib, importlib.util, sys, os
print('cwd:', os.getcwd())
print('sys.path[0]:', sys.path[0])
print('\n'.join(['sys.path:'] + sys.path))
spec = importlib.util.find_spec('main')
print('spec:', spec)
if spec:
    print('origin:', spec.origin)
m = importlib.import_module('main')
print('module file:', getattr(m, '__file__', None))
print('has_app:', hasattr(m,'app'))
print('dir contains app:', 'app' in dir(m))
print('\nmodule dir sample:', [n for n in dir(m) if n in ('app','__file__','get_employees','employee_db')])
print('\nsource preview:')
import inspect
try:
    print('\n'.join(inspect.getsource(m).splitlines()[:40]))
except Exception as e:
    print('could not get source:', e)
