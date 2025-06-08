# Using latex with Binder

[![Binder](https://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/latex/master?filepath=index.ipynb)

Binder link to this repo & branch: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/julowe/latex/texlive-CTAN-install)

This repository demonstrates how to install latex alongside matplotlib for Binder.
This repository also makes use of [JupyterLab Latex](https://github.com/jupyterlab/jupyterlab-latex)
to render latex files in Jupyter lab. This requires a few different build components:

- `apt.txt` for apt-installing some rendering helper packages
- `environment.yml` for installing the python dependencies and jupyterlab-latex
- `postBuild` for installing a small-scheme $\TeX$ Live instance manually from [CTAN](https://ctan.org/)
  to the user's home directory,
  installing a few packages through `tlmgr`,
  and then forcing matplotlib to build the font cache
- `.jupyter/jupyter_notebook_config.py` for adding the jupyterlab-latex configuration option:
  `c.LatexConfig.run_times = 2` so that the .tex file is [typeset twice](https://github.com/jupyterlab/jupyterlab-latex?tab=readme-ov-file#customization)
  and the Table of Contents is rendered

Thanks to [m-weigand](https://github.com/m-weigand) for giving
[inspiration for this repo](https://github.com/m-weigand/binder-example-latex-mpl/blob/master/index.ipynb)!
