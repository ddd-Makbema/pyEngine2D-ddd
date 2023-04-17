from pkg_resources import resource_filename

null = resource_filename(__name__, 'data/null.png')

import pyEngine2D.game_loop
import pyEngine2D.exceptions
import pyEngine2D.game_object
import pyEngine2D.screen_init