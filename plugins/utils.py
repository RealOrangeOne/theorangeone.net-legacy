import subprocess  # nosec
import logging
import os


logger = logging.getLogger(__file__)


def flatten_list(array):
    res = []
    for el in array:
        if isinstance(el, (list, tuple)):
            res.extend(flatten_list(el))
            continue
        res.append(el)
    return res


def run_command(detail, args, wrap=False):
    if wrap:
        run_command('', ['bash', '-c', ' '.join(flatten_list(args))])
    else:
        logger.info(detail + '...')
        subprocess.run(flatten_list(args), check=True)


def node_bin(exec):
    return os.path.join('node_modules', '.bin', exec)
