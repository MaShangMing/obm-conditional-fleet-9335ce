import pathlib, subprocess, sys
if __name__ == '__main__':
    here = pathlib.Path(__file__).resolve().parent
    raise SystemExit(subprocess.call([sys.executable, '-B', str(here.parent/'eval_dev/selftest.py'), str(here)]))
