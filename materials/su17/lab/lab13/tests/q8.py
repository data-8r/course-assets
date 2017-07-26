test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> abs(.04 - np.std([proportion_simulated_successes(100) for _ in range(1000)])) < .02
          True
          >>> abs(np.mean([abs(proportion_simulated_successes(100) - .8) for _ in range(1000)])) < .05
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
