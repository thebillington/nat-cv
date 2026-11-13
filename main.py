import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "scripts"))

from data_loader import load_all


def define_env(env):
    env.variables["data"] = load_all()
