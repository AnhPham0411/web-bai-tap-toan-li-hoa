import sys, importlib
from .common import merge
subj = sys.argv[1]
banks = [importlib.import_module(f'scripts.newbank.{m}').build() for m in sys.argv[2:]]
errs = [e for b in banks for e in b.errors]
if errs:
    print(len(errs), 'lỗi đáp án sai trùng:'); print('\n'.join(errs)); sys.exit(1)
merge(subj, banks)
for b in banks: print(b.ch, 'mc', len(b.mcs), 'short', len(b.sas))
