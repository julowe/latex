# Configuration file for notebook.

c = get_config()  #noqa

# run it twice so table of contents works
c.LatexConfig.run_times = 2
c.LatexConfig.cleanup = False
