import datetime
from pathlib import Path


def make_dir(name, n_try=10):
    for el in range(1, n_try + 1):
        path_ = Path(f'./{datetime.date.today()}_{name}_({el})')
        if not path_.exists():
            path_.mkdir(parents=True, exist_ok=True)
            return path_
        else:
            if any(path_.iterdir()):
                continue
            else:
                return path_
    raise RuntimeError('Количество поптыток создания папок больше 10')
  
