# PanDA-NGE
Integration between PanDA and Next Generation Executer (NGE)

## Resources
* Initial [design document](https://docs.google.com/document/d/1bm8ucgfi9SHjDy0w-ZX5NIdkjk87qFClMB9jMse75uM/). Please edit/comment.
* [Presentation](https://docs.google.com/presentation/d/1xy7q3oks0dMZhfv5nJACRV-x71u0aS-jnPy0FtuKNrM/edit) summarizing the initial design document


## RP experiments on Panda-NGE-development:

  * clone RP repository, switch to branch `experiment/panda_nge`, install:
    * `virtualenv ve; source ve/bin/activate`
    * `git clone git@github.com:radical-cybertools/radical.pilot.git`
    * `git checkout experiment/panda_nge`
    * `pip install .`
    * NOTE: you will need devel branches from radical.saga and radical.utils
  * run the rest service in a terminal:
    * `./bin/panda_nge_server.py
  * run the client in another terminal:
    * `./examples/misc/panda_nge.py`
  
