from pkg_resources import resource_filename

null = resource_filename(__name__, 'data/null.png')

import pyEngine2D_ddd.game_loop
import pyEngine2D_ddd.exceptions
import pyEngine2D_ddd.game_object
import pyEngine2D_ddd.screen_init