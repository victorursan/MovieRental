__author__ = 'victor'

import unittest
from test.store.repository import test_repositories
from test.store.domain.Entities import test_entities
from test.store.controller import test_controllers
from test.store.domain.Validators import test_validators


all_suites = unittest.TestSuite([test_entities.suite(), test_repositories.suite(), test_controllers.suite(),
                                 test_validators.suite()])

if __name__ == '__main__':
  unittest.TextTestRunner(verbosity=2).run(all_suites)

