# vim: tabstop=4 shiftwidth=4 softtabstop=4

#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

# See http://code.google.com/p/python-nose/issues/detail?id=373
# The code below enables nosetests to work with i18n _() blocks
import __builtin__
setattr(__builtin__, '_', lambda x: x)

import os
import shutil

from heat.db.sqlalchemy.session import get_engine
import pdb


def reset_db():
    if os.path.exists('heat-test.db'):
        os.remove('heat-test.db')
    
def setup():
    import mox  # Fail fast if you don't have mox. Workaround for bug 810424

    from heat import db
    from heat.db import migration
    reset_db() 
    migration.db_sync()
    engine = get_engine()
    conn = engine.connect()

