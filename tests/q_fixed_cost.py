test = {
  'name': 'Question fixed_cost',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'fixed_cost'
          >>> 'fixed_cost' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'fixed_cost'
          >>> # from its initial state (of ...)
          >>> fixed_cost is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(fixed_cost, pd.Series)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isnan(fixed_cost.loc[2])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Did you convert to a numeric type?
          >>> fixed_cost.dtype.type == np.float64
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
