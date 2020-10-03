test = {
  'name': 'Question fixed_data',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'fixed_data'
          >>> 'fixed_data' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'fixed_data'
          >>> # from its initial state (of ...)
          >>> fixed_data is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(fixed_data, pd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> fixed_data.shape
          (5, 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Did you make a new copy of the original data frame?
          >>> my_data is not fixed_data
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
