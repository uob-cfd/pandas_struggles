test = {
  'name': 'Question fixed_votes',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'fixed_votes'
          >>> 'fixed_votes' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'fixed_votes'
          >>> # from its initial state (of ...)
          >>> fixed_votes is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(fixed_votes, pd.Series)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(fixed_votes)
          33
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> fixed_votes.dtype.type == np.float64
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> fixed_votes.count() == len(fixed_votes) - 1
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
