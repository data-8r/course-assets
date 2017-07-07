test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your tips array doesn't contain the right things, or it isn't an array.
          >>> import numpy as np
          >>> sum(abs(tips - np.array([4.024, 7.98, 6.202]))) < .01
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
